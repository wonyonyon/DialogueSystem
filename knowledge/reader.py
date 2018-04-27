import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def read_location():
    file_path = os.path.join(BASE_DIR, 'location.txt')
    with open(file_path,'r') as f:
        locations = [loc.strip() for loc in f]

    return locations

def read_genres():

    file_path = os.path.join(BASE_DIR, 'genre.yaml')
    with open(file_path, 'rb') as f:
        genres = yaml.load(f)

    return genres