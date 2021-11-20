-- script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT
	s.title, g.genre_id
	FROM tv_shows s
	LEFT JOIN tv_show_genres  g
	ON s.id = g.show_id
	ORDER BY s.title, g.genre_id;
