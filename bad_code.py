"""
BAD CODE

The problem is in the data structure. Loading the movie database as a list
of lists causes the function movies() to find the movies of a user to be
of linear complexity O(1) and the function shared() to find shared movies to be
of quadratic complexity O(m*m).

The good code has constant complexity O(1) for movies() and
linear complexity O(m) for shared(). For a very small movie database the
difference will be small but for a larger database it will be dramatic.
"""


def load_db(filepath):
    from csv import reader
    with open(filepath) as csvfile:
        return list(reader(csvfile))


def movies(user, db):
    for row in db:
        if row[0] == user:
            return row[1:]
    return None


def shared(user1, user2, db):
    _shared = []
    for movie1 in movies(user1, db):
        for movie2 in movies(user2, db):
            if movie1 == movie2:
                _shared.append(movie1)
    return _shared


db = load_db('movies.csv')
print(db)

print(movies('user42', db))
print(shared('user42', 'user13', db))
