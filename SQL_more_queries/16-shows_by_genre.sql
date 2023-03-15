-- Lists all shows and all genres linked with null records. (var rel = relationship)
SELECT sh.title, gen.name
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS rel
    ON sh.id = rel.show_id
LEFT JOIN tv_genres AS gen
    ON gen.id = rel.genre_id
ORDER BY sh.title, gen.name;
