CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR NOT NULL,
    course_id INTEGER REFERENCES courses
);