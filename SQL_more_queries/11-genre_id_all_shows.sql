-- Lists all shows with null records
SELECT sh.title, g.genre_id
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS g
    ON sh.id = g.show_id
ORDER BY sh.title, g.genre_id;
