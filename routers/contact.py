from datetime import datetime
from fastapi import APIRouter
import schemas.contact as contact_schema  # 追加(後ほどデータモデルも扱うので)


router = APIRouter()


@router.get("/contacts", response_model=list[contact_schema.Contact])  # 一覧表示
async def get_contact_all():
    # pass
    # 試しにデータを登録
    dummy_date = datetime.now()
    return [
        contact_schema.Contact(
            id=1,
            name="山田",
            email="yamada@test.com",
            url="http://test.com",
            gender=1,
            message="テスト",
            is_enabled=False,
            created_at=dummy_date,
        )
    ]


# 保存
# 第二引数にモデルを設定
@router.post("/contacts", response_model=contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


# 詳細表示
@router.get("/contacts/{id}", response_model=contact_schema.Contact)
async def get_contact(id: int):
    return contact_schema.Contact(id)


# 更新
@router.put("/contacts/{id}", response_model=contact_schema.Contact)
async def update_contact(id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


# 削除
@router.delete("/contacts/{id}", response_model=contact_schema.Contact)
async def delete_contact(id: int):
    return
