from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLiteの非同期対応
DB_URL = "sqlite+aiosqlite:///fastapi-app.db"
# 非同期エンジンの生成
# echo=True 実行されるSQL文を表示(本番環境ではFalseにする)
engine = create_async_engine(DB_URL, echo=True)
# DBテーブルのベースクラス
Base = declarative_base()

# DBセッションオブジェクトを生成
"""
sessionmaker：DBセッションを作成
autocommit=False：コミットするまでDBに反映されない
autoflush=False：セッションの変更が即時実行されない
bind=engine：DBセッションが扱うDBエンジン指定
class_：扱うセッションクラスの指定
"""
db_session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


async def get_db():
    async with db_session() as session:
        yield session
