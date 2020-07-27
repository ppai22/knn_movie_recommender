import json
import pandas as pd


# Load dataset to a data frame
data = pd.read_csv(r'movie_metadata.csv')
# Create a new data frame with relevant columns only
df = data[['genres', 'movie_title', 'imdb_score', 'movie_imdb_link']].copy()
# Fetch genres of all movies
genres_all_movies = [df.loc[i]['genres'].split('|') for i in df.index]
# Find the list of genres of all movies in alphabetical order
genres = sorted(list(set([item for sublist in genres_all_movies for item in sublist])))


# Initialize lists for movie data as well as titles
full_data = list()
movie_titles = list()
# Iterate over the data frame
for i in df.index:
    # Append movie title and the index of the movie
    movie_titles.append((df.loc[i]['movie_title'].strip(), i, df.loc[i]['movie_imdb_link'].strip()))
    # Add list of genres of the movies (1/0) to movie data
    movie_data = [1 if genre in df.loc[i]['genres'].split('|') else 0 for genre in genres]
    # Add IMDb score of the movie to the movie data
    movie_data.append(df.loc[i]['imdb_score'])
    # Add record of movie to main data list
    full_data.append(movie_data)


# Create JSON files for data and movie titles for faster load to the Recommmender
data_dump = r'data.json'
titles_dump = r'titles.json'
with open(data_dump, 'w+', encoding='utf-8') as f:
    json.dump(full_data, f)
with open(titles_dump, 'w+', encoding='utf-8') as f:
    json.dump(movie_titles, f)
