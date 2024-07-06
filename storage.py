import json

class StorageManager:
    @staticmethod
    def load_from_file(filename, default):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
