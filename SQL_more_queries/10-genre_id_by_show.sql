-- Lists all shows that have at least one genre linked
SELECT sh.title, g.genre_id
FROM tv_shows AS sh
JOIN tv_show_genres AS g
    ON sh.id = g.show_id
ORDER BY sh.title, g.genre_id;
