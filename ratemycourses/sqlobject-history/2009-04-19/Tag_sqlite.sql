-- Exported definition from 2009-04-19T20:03:48
-- Class ratemycourses.model.Tag
-- Database: sqlite
CREATE TABLE tag (
    id INTEGER PRIMARY KEY,
    name VARCHAR (255) NOT NULL UNIQUE,
    created TIMESTAMP
)
