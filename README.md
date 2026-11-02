# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Real-world recommendation systems combine signals such as user behavior, preferences, and the attributes of each song to predict what someone may enjoy next. Our version focuses on a simple, explainable content-based approach: it compares song features like genre, mood, energy, and tempo with a user's taste profile, then scores and ranks songs by how closely they match.

---

## How The System Works

The simulation will use a transparent content-based design: each song is represented by descriptive musical features, and the recommender compares those features with the user's preferences. It will calculate a match score for each song and rank the highest-scoring songs as recommendations.

The objects will use these features:

- `Song`: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`
- `UserProfile`: preferred `genre`, preferred `mood`, and target values for `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`


## Algorithm Recipe

For each song, calculate a score out of 100:

- Add **30 points** when the song's genre matches the user's favorite genre.
- Add **25 points** when the song's mood matches the user's favorite mood.
- Add up to **20 points** for energy similarity:
  `20 * (1 - abs(song.energy - target_energy))`.
- Add **15 points** when the song's acousticness matches the user's acoustic
  preference (acoustic songs have `acousticness >= 0.6`).
- Add up to **10 points** for valence similarity, using the same normalized
  difference approach as energy.

Rank all songs by score from highest to lowest and return the top `k` songs.
The explanation should list the matching features that contributed to each
recommendation.

### Potential Biases

This approach may favor genres and moods that are more common in the small
catalog, while underrepresenting less common styles. Because genre and mood
receive the largest weights, songs with matching labels can outrank songs that
may be a better overall fit. The system also relies on simplified numerical
features and does not account for lyrics, culture, language, listening history,
or the diversity of a user's taste. These limitations can lead to repetitive
recommendations and should be considered when evaluating the results.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Top recommendations:

Sunrise City - Score: 74.60
Because: matching genre, matching mood, similar energy

Gym Hero - Score: 47.40
Because: matching genre, similar energy

Rooftop Lights - Score: 44.20
Because: matching mood, similar energy

Night Drive Loop - Score: 19.00
Because: similar energy

Storm Runner - Score: 17.80
Because: similar energy

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

The recommender may create filter bubbles because it heavily prioritizes exact genre and mood matches, while the energy-gap calculation favors songs closest to a user’s target energy and may ignore users whose preferences are uncommon in the catalog. It also uses rigid labels, ignores tempo and danceability, applies a binary acoustic preference, and provides no diversity or exploration mechanism, so users may repeatedly receive similar songs instead of discovering different artists, genres, or moods.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

