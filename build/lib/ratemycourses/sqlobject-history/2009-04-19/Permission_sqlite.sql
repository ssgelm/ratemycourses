-- Exported definition from 2009-04-19T20:03:48
-- Class ratemycourses.model.Permission
-- Database: sqlite
CREATE TABLE permission (
    id INTEGER PRIMARY KEY,
    permission_name VARCHAR (16) NOT NULL UNIQUE,
    description VARCHAR (255)
)
