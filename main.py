from fastapi import FastAPI
from routers import contact


app = FastAPI()
app.include_router(contact.router)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
