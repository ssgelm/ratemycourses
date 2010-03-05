-- Exported definition from 2009-04-19T20:03:48
-- Class ratemycourses.model.User
-- Database: sqlite
CREATE TABLE tg_user (
    id INTEGER PRIMARY KEY,
    user_name VARCHAR (16) NOT NULL UNIQUE,
    email_address VARCHAR (255) NOT NULL UNIQUE,
    display_name VARCHAR (255),
    created TIMESTAMP,
    realname BOOLEAN
)
