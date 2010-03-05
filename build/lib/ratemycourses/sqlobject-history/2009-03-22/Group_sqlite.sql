-- Exported definition from 2009-03-22T19:44:23
-- Class ratemycourses.model.Group
-- Database: sqlite
CREATE TABLE tg_group (
    id INTEGER PRIMARY KEY,
    group_name VARCHAR (16) NOT NULL UNIQUE,
    display_name VARCHAR (255),
    created TIMESTAMP
);
CREATE TABLE user_group (
group_id INT NOT NULL,
user_id INT NOT NULL
);
CREATE TABLE group_permission (
group_id INT NOT NULL,
permission_id INT NOT NULL
)
