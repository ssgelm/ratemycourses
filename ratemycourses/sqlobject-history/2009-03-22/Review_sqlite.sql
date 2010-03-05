-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Review
-- Database: sqlite
CREATE TABLE review (
    id INTEGER PRIMARY KEY,
    score INT,
    num_liked INT,
    num_rated INT,
    professor VARCHAR (255),
    contents TEXT,
    created TIMESTAMP,
    reviewer_id INT CONSTRAINT reviewer_id_exists REFERENCES tg_user(id) ,
    course_id INT CONSTRAINT course_id_exists REFERENCES course(id) 
)
