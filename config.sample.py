import os

mysql = {
    "username": "",
    "password": "",
    "host": "",
    "database": "",
}


class Config:
    DEBUG = True
    JSON_AS_ASCII = False

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{NAME}?charset=utf8mb4".format(
        USER=mysql["username"],
        PASSWORD=mysql["password"],
        HOST=mysql["host"],
        NAME=mysql["database"]
    )
