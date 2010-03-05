-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.VisitIdentity
-- Database: sqlite
CREATE TABLE visit_identity (
    id INTEGER PRIMARY KEY,
    visit_key VARCHAR (40) NOT NULL UNIQUE,
    user_id INT
)
