1.	User Registration and Authentication

Register a New User
	•	URL: /api/auth/register/
	•	Method: POST
	•	Description: Registers a new user and returns an authentication token.
	•	Parameters:
	•	username (required): User’s username.
	•	email (required): User’s email address.
	•	password (required): User’s password.

User Login
	•	URL: /api/auth/login/
	•	Method: POST
	•	Description: Logs in a user and returns a JWT authentication token.
	•	Parameters:
	•	username (required): User’s username.
	•	password (required): User’s password.

Token Refresh
	•	URL: /api/auth/refresh/
	•	Method: POST
	•	Description: Returns a new authentication token using a refresh token.
	•	Parameters:
	•	refresh (required): The refresh token obtained during login.

2.	Movie Management

List All Movies
	•	URL: /api/movies/
	•	Method: GET
	•	Description: Returns a list of all movies.

Get Movie Details
	•	URL: /api/movies/<int:pk>/
	•	Method: GET
	•	Description: Returns details of the movie with ID pk.

Search for Movies
	•	URL: /api/movies/search/
	•	Method: GET
	•	Parameters:
	•	q (required): Keyword to search by title, director, or genre.

Toggle Favorite Status
	•	URL: /api/movies/<int:pk>/favorite/
	•	Method: POST
	•	Description: Toggles the “favorite” status for the movie with ID pk.

List Movie Categories
	•	URL: /api/movies/categories/
	•	Method: GET
	•	Description: Returns a list of movie genres and up to 5 movies from each genre.

Most Liked Movies
	•	URL: /api/movies/most-liked/
	•	Method: GET
	•	Description: Returns the most liked movies (movies marked as “favorite” the most).

Newest Movies
	•	URL: /api/movies/newest/
	•	Method: GET
	•	Description: Returns the 5 newest movies (based on release date).

Add a New Movie
	•	URL: /api/movies/
	•	Method: POST
	•	Description: Adds a new movie to the database.
	•	Parameters:
	•	title (required): Title of the movie.
	•	description (required): Description of the movie.
	•	release_date (required): Release date of the movie (format: YYYY-MM-DD).
	•	director (required): Director of the movie.
	•	genre (required): Genre of the movie.
	•	cover_image (optional): Cover image of the movie.
	•	favorite (optional): Whether the movie is marked as a favorite (default: false).
	•	user (optional): The user who added the movie.

Update a Movie
	•	URL: /api/movies/<int:pk>/
	•	Method: PUT
	•	Description: Updates an existing movie in the database.
	•	Parameters:
	•	title (required): Title of the movie.
	•	description (required): Description of the movie.
	•	release_date (required): Release date of the movie.
	•	director (required): Director of the movie.
	•	genre (required): Genre of the movie.
	•	cover_image (optional): Cover image of the movie.
	•	favorite (optional): Whether the movie is marked as a favorite (default: false).
	•	user (optional): The user who added the movie.
	
3. User Management

List All Users
	•	URL: /api/users/
	•	Method: GET
	•	Description: Returns a list of all users in the system.