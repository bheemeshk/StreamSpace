__author__ = 'bheem'


import pandas as pd


unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)


rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames)

print users[:5]
print ratings[:5]
print movies[:5]

data = pd.merge(pd.merge(ratings, users), movies)

print data[:10]


mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')

print mean_ratings[:5]


ratings_by_title = data.groupby('title').size()
print ratings_by_title
print '---------------------------'

print ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]


print type(active_titles), active_titles