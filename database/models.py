from sqlalchemy import MetaData, String
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base
import datetime

metadata_obj = MetaData()


class CodeTable(Base):
    __tablename__ = "helsi_work"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str]
    code: Mapped[str] = mapped_column(String(100))
    date: Mapped[str] = mapped_column(String(30))

