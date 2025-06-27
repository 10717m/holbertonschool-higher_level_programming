-- Lists all cities along with their state names from the database hbtn_0d_usa
-- Each record displays: cities.id - cities.name - states.name
-- Sorted by cities.id in ascending order

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

