import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        songs = []
        for row in reader:
            row["id"] = int(row["id"])
            for field in (
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if user_prefs.get("genre") == song["genre"]:
        score += 30
        reasons.append("matching genre")

    if user_prefs.get("mood") == song["mood"]:
        score += 25
        reasons.append("matching mood")

    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    score += 20 * energy_similarity
    reasons.append("similar energy")

    if "likes_acoustic" in user_prefs or "acoustic" in user_prefs:
        likes_acoustic = user_prefs.get(
            "likes_acoustic", user_prefs.get("acoustic", False)
        )
        is_acoustic = song["acousticness"] >= 0.6
        if is_acoustic == likes_acoustic:
            score += 15
            reasons.append("matching acoustic preference")

    if "valence" in user_prefs:
        valence_similarity = 1 - abs(song["valence"] - user_prefs["valence"])
        score += 10 * valence_similarity
        reasons.append("similar valence")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = [
        (song, score, reasons)
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    # Same as below:
    # scored_songs = []
    # for song in songs:
    #     score, reasons = score_song(user_prefs, song)
    #     scored_songs.append((song, score, reasons))

    top_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
    return [
        (song, score, ", ".join(reasons))
        for song, score, reasons in top_songs
    ]
