import keys
import values
from datetime import datetime
import hashlib

import pymongo
from pymongo import MongoClient


class Database:

    def __init__(self):
        client = MongoClient(keys.MONGO_AUTH)
        self.db = client['KPITctf']
        self.users = self.db['users']
        self.stages = self.db['stages']

        self.users.create_index([('user_id', pymongo.TEXT)], unique=True)
        self.stages.create_index([('num', pymongo.ASCENDING)], unique=True)

    def add_user(self, user_id, username):

        if self.users.find_one({'user_id': user_id}) is None:
            user = {
                'user_id': user_id,
                'username': username,
                'stage': 0,
                'registration time': datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
            }
            self.users.insert_one(user)
            return user_id
        else:
            return 0

    def next_stage(self, user_id, flag):
        user_stage = self.users.find_one({'user_id': user_id})['stage']
        if user_stage == values.LAST_STAGE:
            return 2  # Already finished
        user_flag_hash = hashlib.md5(flag.encode())
        real_flag_hash = self.stages.find_one({'num': user_stage + 1})['flag_hash']

        if user_flag_hash == real_flag_hash:
            self.users.update_one({'user_id': user_id}, {'stage': user_stage + 1})
            return 1  # Flag is correct

        return 0  # Flag is incorrect

    def user_exists(self, user_id):
        if self.users.find_one({'user_id': user_id}) is None:
            return False
        else:
            return True





if __name__ == "__main__":
    ...
