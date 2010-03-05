-- Exported definition from 2009-04-19T20:03:48
-- Class ratemycourses.model.VisitIdentity
-- Database: sqlite
CREATE TABLE visit_identity (
    id INTEGER PRIMARY KEY,
    visit_key VARCHAR (40) NOT NULL UNIQUE,
    user_id INT
)
