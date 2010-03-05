-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Permission
-- Database: sqlite
CREATE TABLE permission (
    id INTEGER PRIMARY KEY,
    permission_name VARCHAR (16) NOT NULL UNIQUE,
    description VARCHAR (255)
)
