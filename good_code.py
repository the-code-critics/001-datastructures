"""
GOOD CODE:

Uses a dictionary that maps user names to the set of their movies.
Loading will be slower then the bad code example, but the common use cases
of finding the movies for a user and extracting the movies shared by two
users are much, much faster.
"""


def load_db(filepath):
    from csv import reader
    with open(filepath) as csvfile:
        return {r[0]: set(r[1:]) for r in reader(csvfile)}


def movies(user, db):
    return db.get(user, None)


def shared(user1, user2, db):
    return movies(user1, db) & movies(user2, db)


db = load_db('movies.csv')
print(db)

print(movies('user42', db))
print(shared('user42', 'user13', db))
