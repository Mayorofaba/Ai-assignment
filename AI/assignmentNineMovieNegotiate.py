""" Movie Night Negotiator
Topics: Sets · Lists · Conditions

You and two friends each have a list of 8 movies you actually want to watch. Convert each to a set. Find: movies all three agree on, movies only you want, movies only two people want (and which two), and the best "compromise pick" ranked by most agreed-upon."""
# Movie lists for you and your two friends
your_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings", "Fight Club", "Forrest Gump", "The Stranger Things"]
motion_movies = ["Inception", "The Matrix", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings", "Fight Club", "Forrest Gump", "The Shawshank Redemption"]
victor_movies = ["Inception", "The Matrix", "Interstellar", "The Dark                  Knight", "Pulp Fiction", "The Lord of the Rings", "Fight Club", "The Godfather"]    
# Convert lists to sets
your_movies_set = set(your_movies)  
motion_movies_set = set(motion_movies)
victor_movies_set = set(victor_movies)
# Movies all three agree on
common_movies = your_movies_set.intersection(motion_movies_set, victor_movies_set)
# Movies only you want  
only_you_want = your_movies_set.difference(motion_movies_set.union(victor_movies_set))
# Movies only two people want
only_two_want = (your_movies_set.intersection(motion_movies_set) - victor_movies_set).union(your_movies_set.intersection(victor_movies_set) - motion_movies_set).union(motion_movies_set.intersection(victor_movies_set) - your_movies_set)
# Best compromise pick ranked by most agreed-upon
from collections import Counter                     
all_movies = your_movies + motion_movies + victor_movies
movie_counts = Counter(all_movies)          
compromise_pick = movie_counts.most_common(1)[0][0]
# Output results                
print("Movies all three agree on:", common_movies)
print("Movies only you want:", only_you_want)       
print("Movies only two people want:", only_two_want)
print("Best compromise pick:", compromise_pick) 
