-- Exported definition from 2009-04-19T20:03:48
-- Class ratemycourses.model.Visit
-- Database: sqlite
CREATE TABLE visit (
    id INTEGER PRIMARY KEY,
    visit_key VARCHAR (40) NOT NULL UNIQUE,
    created TIMESTAMP,
    expiry TIMESTAMP
)
