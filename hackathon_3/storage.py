import pickle
import os

class Storage:
    FILE_NAME = 'employees_data.pkl'

    @staticmethod
    def save(employees):
        with open(Storage.FILE_NAME, 'wb') as f:
            pickle.dump(employees, f)

    @staticmethod
    def load():
        if not os.path.exists(Storage.FILE_NAME):
            return []
        with open(Storage.FILE_NAME, 'rb') as f:
            return pickle.load(f)