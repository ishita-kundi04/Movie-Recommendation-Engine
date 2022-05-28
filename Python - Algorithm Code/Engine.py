#Discription : Build a movie Recommendation Engine

#import the libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#Load the data
from google.colab import files
uploaded = files.upload()
# Need to uplaod IMDB-Movie-Data.csv

#store the data
df = pd.read_csv('IMDB-Movie-Data.csv')
#Show the first 3 rows of data
df.head(3)

# Get a count of the number of rows/movies in the data set and the number of columns
df.shape

# Create a list of important columns for the recommendation engine
columns = ['Actors', 'Director', 'Genre', 'Title']

# Show the data 
df[columns].head(3)

# Check for any missing values in imp columns
df[columns].isnull().values.any()

# Create a function to combine the values of the important columns into a single string
def get_important_features(data):
  important_features = []
  for i in range(0, data.shape[0]):
    important_features.append(data['Actors'][i]+' '+data['Director'][i]+' '+data['Genre'][i]+' '+data['Title'][i])

  return important_features


# Create a column to hold the combined strings
df['important_features'] = get_important_features(df)

#Show the data
df.head(3)

# Convert the text to a matrix of token counts
cm = CountVectorizer().fit_transform(df['important_features'])

# Get the cosine similarity matrix from the count matrix
cs = cosine_similarity(cm)

# Print the cosine similarity matrix
print(cs)

# Get the shape of the cosine similarity matrix
cs.shape

# Get the title of the movie that the user likes
title = 'Guardians of the Galaxy'

# Find the movies id
movie_id = df[df.Title == title]['Rank'].values[0] 

print(movie_id)

# Create a list of enumerations for the similarity score [ (movie_id, similarity score) , (...) ]
scores = list(enumerate(cs[movie_id]))

# Sort the list
sorted_scores = sorted(scores, key = lambda x: x[1], reverse = True)
sorted_scores = sorted_scores[1:]

# Print the sorted scores
print(sorted_scores)

# Create a loop to print the first 7 similar movies
j = 0
print('The 7 most recommended movies to', title, 'are:\n')
for item in sorted_scores:
  movie_title = df[df.Rank == item[0]]['Title'].values[0]
  print(j+1, movie_title)
  j = j+1
  if j>6:
    break

