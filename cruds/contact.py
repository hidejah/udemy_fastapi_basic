from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from datetime import datetime

import models.contact as contact_model  # ORMモデル
import schemas.contact as contact_schema  # スキーマモデル


async def create_contact(
    db: AsyncSession, contact: contact_schema.ContactCreate
) -> contact_model.Contact:
    """
    DBに新規保存
    引数：
        db：DBセッション
        contact：作成するコンタクトのデータ
    戻り値：
        作成されたORMモデル
    """
    contact_data = contact.model_dump()
    if (
        contact_data["url"] is not None
    ):  # urlフィールドが存在し、Noneでない場合は文字列に変換
        contact_data["url"] = str(contact_data["url"])

    db_contact = contact_model.Contact(**contact_data)  # db保存はsqlalchemyのモデル

    db.add(db_contact)  # 追加
    await db.commit()  # コミット(反映)
    await db.refresh(db_contact)  # 最新に反映
    return db_contact


# 一覧表時(sqlalchemyを使ってDBから情報取得)
async def get_contact_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:
    result: Result = await db.execute(
        select(
            contact_model.Contact.id,
            contact_model.Contact.name,
            contact_model.Contact.created_at,
        )
    )
    return result.all()


# 詳細表示
# idを指定して条件を取得。where句でidを指定
# idが存在しない可能性もあるので、Noneも返り値の方に設定
async def get_contact(db: AsyncSession, id: int) -> contact_model.Contact | None:
    query = select(contact_model.Contact).where(contact_model.Contact.id == id)
    result: Result = await db.execute(query)
    return result.scalars().first()  # scalars()単一の値を取得、first()最初の要素を取得


# 更新
async def update_contact(
    db: AsyncSession,
    contact: contact_schema.ContactCreate,  # 更新したい情報
    original: contact_model.Contact,  # DB保存済みの情報
) -> contact_model.Contact:
    original.name = contact.name
    original.email = contact.email
    if original.url is not None:  # urlは文字列に変換
        original.url = str(contact.url)
    original.gender = contact.gender
    original.message = contact.message
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


# 削除
async def delete_contact(
    db: AsyncSession,
    original: contact_model.Contact,  # DB保存済みの情報
) -> None:
    await db.delete(original)
    await db.commit()
