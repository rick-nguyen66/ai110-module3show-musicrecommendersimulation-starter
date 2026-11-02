"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# Normal profiles make it easy to compare the recommender's behavior for
# different listening goals without rewriting the preference dictionary.
USER_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.95,
        "likes_acoustic": False,
        "valence": 0.9,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "likes_acoustic": True,
        "valence": 0.6,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.95,
        "likes_acoustic": False,
        "valence": 0.35,
    },
}

# These profiles are deliberately unusual. They help reveal how the fixed
# weights behave when preferences conflict or fall outside the catalog.
ADVERSARIAL_PROFILES = {
    "Conflicting Energetic Sad User": {
        "genre": "rock",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": False,
        "valence": 0.1,
    },
    "Boundary Values User": {
        "genre": "ambient",
        "mood": "serene",
        "energy": 0.0,
        "likes_acoustic": True,
        "valence": 1.0,
    },
    "Unknown Genre User": {
        "genre": "hyperpop",
        "mood": "euphoric",
        "energy": 0.8,
        "likes_acoustic": False,
        "valence": 1.0,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv") 

    for profile_group, profiles in (
        ("Standard profiles", USER_PROFILES),
        ("Adversarial profiles", ADVERSARIAL_PROFILES),
    ):
        print(f"\n{profile_group}:\n")
        for profile_name, user_prefs in profiles.items():
            print(f"{profile_name}:")
            recommendations = recommend_songs(user_prefs, songs, k=5)
            for rank, (song, score, explanation) in enumerate(
                recommendations, start=1
            ):
                print(f"{rank}. {song['title']} - Score: {score:.2f}")
                print(f"   Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
