from sqlalchemy import Column, String, Date, DateTime, Integer, func
from src.db import Base


class TourGroups(Base):
    __tablename__ = "TourGroups"
    id = Column(Integer, primary_key=True, comment="旅團代號")
    name = Column(String(100), nullable=False, comment="旅團名")
    tags = Column(String(100), nullable=True, comment="旅團標籤的對照ID")
    review = Column(String(10), nullable=False,
                    server_default="5", comment="評分")
    place = Column(String(100), nullable=False, comment="地點")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")
    deletedAt = Column(DateTime, nullable=True, comment="刪除時間")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<TourGroups: {}, {}, {}, {}>".format(self.id, self.name, self.createdAt, self.place)


class Tags(Base):
    __tablename__ = "Tags"
    id = Column(Integer, primary_key=True, comment="標籤代號")
    name = Column(String(50), nullable=False, unique=True, comment="標籤名")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Tags: {}, {}>".format(self.id, self.name)


class Price(Base):
    __tablename__ = "Price"
    id = Column(Integer, primary_key=True, comment="價格代號")
    groupId = Column(Integer, nullable=False, comment="旅團代號")
    startDate = Column(Date, nullable=False, comment="出發日期")
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment="建立時間")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Price: {}, {}>".format(self.id, self.groupId, self.startDate)
