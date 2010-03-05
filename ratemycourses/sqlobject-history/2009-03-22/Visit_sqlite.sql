-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Visit
-- Database: sqlite
CREATE TABLE visit (
    id INTEGER PRIMARY KEY,
    visit_key VARCHAR (40) NOT NULL UNIQUE,
    created TIMESTAMP,
    expiry TIMESTAMP
)
