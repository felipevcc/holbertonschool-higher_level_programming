-- Lists all genres of the show "Dexter". (var rel = relationship)
SELECT gen.name
FROM tv_genres AS gen
JOIN tv_show_genres AS rel
    ON gen.id = rel.genre_id
JOIN tv_shows AS sh
    ON sh.id = rel.show_id
WHERE sh.title = "Dexter"
ORDER BY gen.name;
