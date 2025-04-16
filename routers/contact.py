from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema  # 追加(後ほどデータモデルも扱うので)
import cruds.contact as contact_crud  # DB保存関数
from database import get_db  # DBセッション取得関数


router = APIRouter()


# 一覧表示
@router.get("/contacts", response_model=list[contact_schema.ContactList])  # 一覧表示
async def get_contact_all(db: AsyncSession = Depends(get_db)):
    # Read処理を実行
    return await contact_crud.get_contact_all(db)


# 保存(第二引数にモデルを設定)
@router.post("/contacts", response_model=contact_schema.ContactCreate)
async def create_contact(
    body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    return await contact_crud.create_contact(db, body)


# 詳細表示
@router.get("/contacts/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db, id)  # 関数実行
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


# 更新
@router.put("/contacts/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(
    id: int, body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    # 存在するかどうかのチェック
    contact = await contact_crud.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_crud.update_contact(db, body, original=contact)


# 削除
@router.delete("/contacts/{id}", response_model=None)
async def delete_contact(id: int, db: AsyncSession = Depends(get_db)):
    # 存在するかどうかのチェック
    contact = await contact_crud.get_contact(db, id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    # 存在していたら実行
    return await contact_crud.delete_contact(db, original=contact)


def get_message():
    message = "Hello World!"
    print(f"get_messageが実行されたよ：{message}")
    return message


@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"エンドポイントにアクセスがあったよ{message}")
    return {"message": message}
