# SQL query to create the database
create_database_query = """
CREATE DATABASE AreYouStillWatching_db;
"""

# SQL query to create the final table
create_table_query = """
CREATE TABLE final (
    id SERIAL PRIMARY KEY,
    Type VARCHAR(30),
    Title VARCHAR(255),
    Country VARCHAR(255),
    Date_Added DATE,
    Year INT,
    Rating VARCHAR(10),
    Age VARCHAR(5),
    IMDb FLOAT,
    Rotten_Tomatoes VARCHAR(5)
);
"""


