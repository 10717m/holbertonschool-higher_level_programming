-- Lists all shows that do not have a genre linked
-- Shows title and NULL for genre_id
-- Uses LEFT JOIN to include shows with no genre, and filters only those

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

