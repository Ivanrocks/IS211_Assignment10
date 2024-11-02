-- Drop the existing music database if it exists to start fresh
DROP DATABASE IF EXISTS music;

-- Create a new database named 'music'
CREATE DATABASE music;

-- Switch to the 'music' database for subsequent operations
USE music;

-- Create the 'artists' table to store artist information
CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each artist, auto-incremented
    artist_name CHAR(200) NOT NULL              -- Name of the artist, cannot be null
);

-- Create the 'albums' table to store album information
CREATE TABLE albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each album, auto-incremented
    album_name CHAR(255) NOT NULL,               -- Name of the album, cannot be null
    artist_id INT,                                -- Foreign key reference to the artist who created the album
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE  -- Link to the artists table with cascade delete
);

-- Create the 'songs' table to store song information
CREATE TABLE songs (
    song_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each song, auto-incremented
    song_name CHAR(200) NOT NULL,                 -- Name of the song, cannot be null
    album_id INT NOT NULL,                         -- Foreign key reference to the album this song belongs to
    track_number INT NOT NULL,                     -- Track number of the song on the album, cannot be null
    duration INT NOT NULL,                         -- Duration of the song in seconds, cannot be null
    FOREIGN KEY (album_id) REFERENCES albums(album_id) ON DELETE CASCADE  -- Link to the albums table with cascade delete
);

-- Insert random values into the Artists table
INSERT INTO artists (artist_name) VALUES
('The Beatles'),
('Elvis Presley'),
('Beyoncé'),
('Adele'),
('Queen');

-- Insert random values into the Albums table
INSERT INTO albums (album_name, artist_id) VALUES
('Abbey Road', 1),        -- The Beatles
('Elvis Presley', 2),     -- Elvis Presley
('Lemonade', 3),          -- Beyoncé
('25', 4),                -- Adele
('A Night at the Opera', 5);  -- Queen

-- Insert random values into the Songs table
INSERT INTO songs (song_name, album_id, track_number, duration) VALUES
('Come Together', 1, 1, 259),      -- The Beatles - Abbey Road
('Jailhouse Rock', 2, 1, 158),     -- Elvis Presley - Elvis Presley
('Formation', 3, 1, 232),           -- Beyoncé - Lemonade
('Hello', 4, 1, 295),               -- Adele - 25
('Bohemian Rhapsody', 5, 1, 354);  -- Queen - A Night at the Opera
