from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, HttpUrl  # 追加


class Contact(BaseModel):  # 継承
    id: int
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr  # mail
    url: HttpUrl | None = Field(default=None)  # urlか空
    gender: int = Field(strict=True, ge=0, le=2)  # 必須 0,1,2
    message: str = Field(max_length=200)
    is_enabled: bool = Field(default=False)
    created_at: datetime
