-- Lists all the cities of California in the database
SELECT cities.`id`, cities.`name`
FROM cities, states 
WHERE states.`name` = "California"
    AND cities.`state_id` = states.`id`
ORDER BY cities.`id` ASC;
