-- Lists all comedy shows. (var rel = relationship)
SELECT sh.title
FROM tv_shows AS sh
JOIN tv_show_genres AS rel
    ON sh.id = rel.show_id
JOIN tv_genres AS gen
    ON gen.id = rel.genre_id
WHERE gen.name = "Comedy"
ORDER BY sh.title;
