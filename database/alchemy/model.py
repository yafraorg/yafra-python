# coding: utf-8
import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
class Company(Base):
    __tablename__ = 'company'
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str]
    eventdate: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    eventdesc: Mapped[Optional[str]]
    fkPerson: Mapped[int] = mapped_column(ForeignKey("user.id"))
    person = relationship(u'User')
