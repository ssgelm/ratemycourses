-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Course
-- Database: sqlite
CREATE TABLE course (
    id INTEGER PRIMARY KEY,
    dept VARCHAR (255),
    num VARCHAR (255),
    name VARCHAR (255) NOT NULL UNIQUE,
    description TEXT,
    instructor_comments TEXT,
    created TIMESTAMP
);
CREATE TABLE course_tag (
course_id INT NOT NULL,
tag_id INT NOT NULL
)
