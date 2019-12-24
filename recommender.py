from Classifier import KNearestNeighbours
import json
from operator import itemgetter
import test_movies


# Load data and movies list from corresponding JSON files
with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)


# Create dummy target variable for the KNN Classifier
target = [0 for item in movie_titles]
# Test point with movie data < Change the movie with macro provided in test_movies.py or add your own >
test_point = test_movies.AVENGERS_INFINITY_WAR
# Instantiate object for the Classifier
model = KNearestNeighbours(data, target, test_point, k=10)
# Run the algorithm
model.fit()

# Distances to most distant movie
max_dist = sorted(model.distances, key=itemgetter(0))[-1]
# Print list of 10 recommendations < Change value of k for a different number >
for i in model.indices:
    print(movie_titles[i][0] + ' ----> ' + str(model.distances[i][0]))
