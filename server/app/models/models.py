from sqlalchemy import BigInteger, ForeignKey, text, Text, String, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
import datetime




# class School:
#     __tablename__ = 'schools'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(100))
    
# class User:
#     __tablename__ = 'users'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(String(30), unique=True)
#     school: Mapped["id"] = relationship("School", back_populates="users")
    
    
class Vstechnical_data(Base):
    __tablename__ = 'vstechnical_datas'

    id: Mapped[int] = mapped_column(primary_key=True)
    schedule: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[str] = mapped_column(String(50), nullable=False)
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.date!r})"

    def __repr__(self):
        return str(self)
    
class Vstechnical_archive(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    schedule: Mapped[str] = mapped_column(Text, nullable=False)
    date: Mapped[datetime.date] = mapped_column(nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.date!r})"

    def __repr__(self):
        return str(self)
    
    
class Codes(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    code: Mapped[str] = mapped_column(unique=True)
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.code!r})"

    def __repr__(self):
        return str(self)
    
class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    group_name: Mapped[str] = mapped_column(Text, nullable=False)
    
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.group_name!r})"

    def __repr__(self):
        return str(self)


    
    