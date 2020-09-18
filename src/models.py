from sqlalchemy import Column, String, Date, DateTime, Integer, func
from src.db import Base
from dataclasses import dataclass
import datetime

@dataclass
class TourGroups(Base):
    __tablename__ = "TourGroups"
    id: int
    name: str
    tags: str
    review: str
    place: str
    price: str
    createdAt: datetime.datetime
    deletedAt: datetime.datetime

    id = Column(Integer, primary_key=True, comment="旅團代號")
    name = Column(String(100), nullable=False, comment="旅團名")
    tags = Column(String(100), nullable=True, comment="旅團標籤的對照ID")
    review = Column(String(10), nullable=False,
                    server_default="5", comment="評分")
    place = Column(String(100), nullable=False, comment="地點")
    price = Column(String(100), nullable=True, comment="旅團價格的對照ID")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")
    deletedAt = Column(DateTime, nullable=True, comment="刪除時間")

    def __repr__(self):
        return "<TourGroups: {}, {}, {}, {}>".format(self.id, self.name, self.createdAt, self.place)


@dataclass
class Tags(Base):
    __tablename__ = "Tags"
    id: int
    name: str
    createdAt: datetime.datetime

    id = Column(Integer, primary_key=True, comment="標籤代號")
    name = Column(String(50), nullable=False, unique=True, comment="標籤名")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")

    def __repr__(self):
        return "<Tags: {}, {}>".format(self.id, self.name)


@dataclass
class Price(Base):
    __tablename__ = "Price"
    id: int
    price: str
    startDate: datetime.date
    createdAt: datetime.datetime

    id = Column(Integer, primary_key=True, comment="價格代號")
    price = Column(String(50), nullable=False, comment="價格")
    startDate = Column(Date, nullable=False, comment="出發日期")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")

    def __repr__(self):
        return "<Price: {}, {}, {}>".format(self.id, self.price, self.startDate)
