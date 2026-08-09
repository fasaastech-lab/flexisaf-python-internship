import json
import csv
from datetime import datetime


def save_data(students, filename="fees.json"):
    # Save students dictionary to JSON file
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)


def load_data(filename="fees.json"):
    # Load students dictionary from JSON file
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

