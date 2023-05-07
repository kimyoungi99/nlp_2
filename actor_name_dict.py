import pandas as pd

def get_dict():
    people_data = pd.read_csv("people.csv")
    return {row["tmdb_id"]: row["name"] for _, row in people_data.iterrows()}

def get_reversed():
    people_data = pd.read_csv("people.csv")
    return {row["name"]: row["tmdb_id"] for _, row in people_data.iterrows()}