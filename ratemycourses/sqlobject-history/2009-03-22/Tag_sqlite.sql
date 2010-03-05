-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Tag
-- Database: sqlite
CREATE TABLE tag (
    id INTEGER PRIMARY KEY,
    name VARCHAR (255) NOT NULL UNIQUE,
    created TIMESTAMP
)
