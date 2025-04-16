from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, HttpUrl  # 追加


# 一覧表示用モデル
class ContactList(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    created_at: datetime

    class Config:
        from_attributes = True


# ベースモデル(BaseModelを継承)
class ContactBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr  # mail
    url: HttpUrl | None = Field(default=None)  # urlか空
    gender: int = Field(strict=True, ge=0, le=2)  # 必須 0,1,2
    message: str = Field(max_length=200)
    is_enabled: bool = Field(default=False)

    class Config:
        from_attributes = True


# 詳細表示用モデル(ContactBaseを継承)
class ContactDetail(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# 保存用モデル(ContactBaseを継承)
class ContactCreate(ContactBase):
    pass
