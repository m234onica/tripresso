USE tripressoDB;
CREATE TABLE tourGroups(
    id                  INT                 NOT NULL,                                   -- COMMENT "旅團代號"
    title               VARCHAR(100)        NOT NULL,                                   -- COMMENT "旅團名"
    tags                VARCHAR(100),                                                   -- COMMENT "旅團標籤的對照ID"
    review              FLOAT               NOT NULL    DEFAULT     5,                  -- COMMENT "評分"
    place               VARCHAR(100)        NOT NULL,                                   -- COMMENT "地點"
    createdAt           DATETIME            NOT NULL    DEFAULT     CURRENT_TIMESTAMP,  -- COMMENT "建立時間"
    deletedAt           DATETIME,                                                       -- COMMENT "刪除時間"
  PRIMARY KEY( id )
);

CREATE TABLE tags(
  id                    INT                 NOT NULL,                                   -- COMMENT "標籤代號"
  name                  VARCHAR(100)        NOT NULL,                                   -- COMMENT "標籤名"
  createdAt             DATETIME            NOT NULL    DEFAULT     CURRENT_TIMESTAMP,  -- COMMENT "建立時間"
  PRIMARY KEY( id )
);

CREATE TABLE price(
  id                    INT                 NOT NULL,                                   -- COMMENT "價格代號"
  groupId               INT                 NOT NULL,                                   -- COMMENT "旅團代號"
  StartDate             DATE                NOT NULL,                                   -- COMMENT "出發日期"
  createdAt             DATETIME            NOT NULL    DEFAULT     CURRENT_TIMESTAMP,  -- COMMENT "建立時間"
  PRIMARY KEY( id )
);