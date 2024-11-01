from sqlmodel import SQLModel, Session, create_engine
from fastapi import Depends
from models import Base
from typing import Annotated

engine = create_engine("sqlite:///app.db")

async def init_db():
    SQLModel.metadata.create_all(engine)

# def get_db_1():
#     with Session(engine) as session:
#         yield Session

async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


session_dependency = Annotated[Session, Depends(get_db)]