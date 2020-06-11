CREATE TABLE teachers(
    id SERIAL PRIMARY KEY,
    teacher_name VARCHAR NOT NULL,
    course_id INTEGER REFERENCES courses
);