
create database AreYouStillWatching_db;


create table final (
	id serial PRIMARY KEY,
	Type VARCHAR(30),
	Title VARCHAR(255),
	Country VARCHAR(255),
	Date_Added date,
	Year Int,
	Rating VARCHAR(10),
	Age VARCHAR(5),
	IMDb float,
	Rotten_Tomatoes VARCHAR(5)
);