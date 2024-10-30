CREATE TABLE 'langs' (
    'lang_id' INTEGER NOT NULL,
    'lang_name' TEXT NOT NULL,
    PRIMARY KEY("lang_id" AUTOINCREMENT)
)

INSERT INTO 'langs' ('lang_id', 'lang_name') VALUES (1, 'Arabic')

INSERT INTO 'langs' ('lang_name') VALUES ('Arabic')
INSERT INTO 'langs' ('lang_name') VALUES ('English')

