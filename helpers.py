import hashlib

my_virtual_coins = 0

leaderboard = {"ana": 10, "maria": 20, "alex": 22, "ion": 14, "dan": 17, "andrei": 33, "cristi": 2,
               "diana": 12, "george": 1, "irinuca": 2, "marius": 2, "ghita": 1, "marin": 0}


def hash_password(password):
    # function for hashing the password
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password
