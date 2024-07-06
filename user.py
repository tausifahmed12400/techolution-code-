import json

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {"name": self.name, "user_id": self.user_id}

class UserManager:
    def __init__(self, storage_file='users.json'):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.storage_file, 'r') as file:
                return [User(**user) for user in json.load(file)]
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.storage_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def add_user(self, name, user_id):
        if self.user_id_exists(user_id):
            print(f"User ID {user_id} is already taken, please use another user ID.")
            return False
        self.users.append(User(name, user_id))
        self.save_users()
        return True

    def user_id_exists(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return True
        return False

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")

    def search_users(self, **kwargs):
        results = self.users
        for key, value in kwargs.items():
            results = [user for user in results if getattr(user, key) == value]
        return results
