CREATE TABLE passengers(
    id serial PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers(name, flight_id) VALUES ('Alice', 1),
('Bob', 1),
('Charlie', 2),
('Dave', 2),
('Erin', 4),
('Frank', 6),
('Grace', 6);