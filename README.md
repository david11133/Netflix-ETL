# Netflix ETL Project

## Introduction

This ETL project integrates multiple Netflix data sources from Kaggle into a single PostgreSQL table for streamlined analysis and management.

## Extract

The data sources consist of CSV files obtained from Kaggle.com, containing information about movies and TV shows available on popular streaming services. The CSV files were manually downloaded and stored in the Data Branch folder of the repository.

### Data Sources:
| Source No. | Link with Description | Source Last Updated | Download Date | File name in Resources folder |
|------------|-----------------------|---------------------|---------------|-------------------------------|
| 1          | List of TV shows on multiple streaming services | 2020-05-25 | 2021-03-06 | tv_shows_all_streaming.csv |
| 2          | List of Movies on multiple streaming services | 2020-05-22 | 2021-03-06 | movies_all_streaming.csv |
| 3          | List of TV shows and Movies on Netflix | 2021-01-18 | 2021-03-06 | netflix_titles.csv |

## Transform

Transformations were planned using an Excel file (ETL_Netflix_Major.xlsx) to comply with business rules for the final database table. Transformations included dropping unnecessary data columns, converting dates from object/string types to datetime types, and renaming columns for consistency.

### Transformations:
- Extracted only Netflix titles for TV shows and movies.
- Joined TV shows and movies data to Netflix titles data based on title name and year of release.
- Removed rows with null values.

## Load

Two dataframes were created in pandas to merge data from Source 3 to Sources 1 and 2. These dataframes were then appended to the same table in PostgreSQL. A schema file (AreYouStillWatching_schema.sql) to set up the database and the 'final' table is provided.

The psycopg2 module was used to connect to the database and append the dataframes to the 'final' table. An audit report was generated to track the duration of each ETL phase and the number of dropped titles. The final table was also saved as a CSV file in the Output folder.


