-- Lists all shows with their genre_id (if any)
-- Uses LEFT JOIN to include shows with no genre
-- Sorted by title then genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

