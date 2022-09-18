import keys
from datetime import datetime

import pymongo
from pymongo import MongoClient


class Database:

    def __init__(self):
        client = MongoClient(keys.MONGO_AUTH)
        self.db = client['KPITctf']
        self.users = self.db['users']
        self.stages = self.db['stages']

        self.users.create_index(['user_id', pymongo.TEXT], unique=True)
        self.stages.create_index(['num', pymongo.ASCENDING], unique=True)

    def add_user(self, user_id, username):

        if self.users.find_one({'user_id': user_id}) is None:
            user = {
                'user_id': user_id,
                'username': username,
                'stage': 1,
                'registration time': datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
            }
            self.users.insert_one(user)
            return user_id
        else:
            return 0

    def next_stage(self, user_id, flag_hash):
        user_stage = self.users.find_one({'user_id': user_id})


if __name__ == "__main__":
    ...
