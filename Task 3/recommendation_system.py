import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommendation(movies, user_profile):
    """
    Recommends movies based on content-based filtering.

    Parameters:
    - movies: A numpy array where each row represents a movie's features.
    - user_profile: A numpy array representing the user's preferences.

    Returns:
    - Recommended movie indices.
    """
    similarity = cosine_similarity(movies, user_profile.reshape(1, -1))
    recommended_movie_indices = similarity.flatten().argsort()[::-1]
    return recommended_movie_indices

def collaborative_filtering(ratings, user_ratings):
    """
    Recommends movies based on collaborative filtering.

    Parameters:
    - ratings: A numpy array where each row represents a user's ratings for movies.
    - user_ratings: A numpy array representing the current user's ratings.

    Returns:
    - Recommended movie indices.
    """
    # Compute movie similarity
    movie_similarity = cosine_similarity(ratings.T)

    # Avoid division by zero by adding a small constant (e.g., 1e-10) to the denominator
    sum_similarity = np.array([np.abs(movie_similarity).sum(axis=1)]).T
    sum_similarity[sum_similarity == 0] = 1e-10  # Replace zeros to avoid division by zero

    # Predict ratings
    predicted_ratings = movie_similarity.dot(user_ratings) / sum_similarity
    
    # Recommend movies with the highest predicted ratings
    recommended_movie_indices = predicted_ratings.flatten().argsort()[::-1]
    return recommended_movie_indices

def main():
    # Content-Based Filtering Data
    movies = np.array([
        [1, 0, 1],  # Movie 1: Action, Comedy
        [0, 1, 1],  # Movie 2: Drama, Comedy
        [1, 1, 0],  # Movie 3: Action, Drama
        [0, 0, 1],  # Movie 4: Comedy
    ])
    user_profile = np.array([1, 1, 0])  # Likes Action and Comedy

    # Get recommendations
    content_recommendations = content_based_recommendation(movies, user_profile)
    print("Content-Based Recommendations:", content_recommendations)

    # Collaborative Filtering Data
    ratings = np.array([
        [5, 0, 4, 0],  # User 1
        [3, 0, 0, 2],  # User 2
        [4, 0, 0, 5],  # User 3
    ])
    user_ratings = np.array([5, 0, 4, 0])  # Current user's ratings

    # Get recommendations
    collab_recommendations = collaborative_filtering(ratings, user_ratings)
    print("Collaborative Filtering Recommendations:", collab_recommendations)

if __name__ == "__main__":
    main()
