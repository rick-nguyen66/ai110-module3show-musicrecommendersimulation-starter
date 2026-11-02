# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

VibeMatch recommends songs that are similar to a user's favorite genre, mood,
energy level, acoustic preference, and valence. It is designed for classroom
exploration, not for real-world decisions or production use.

---

## 3. How the Model Works  

The model gives each song a score out of 100. It adds points for matching
genre, mood, and acoustic preference. It also gives more points when energy
and valence are close to the user's targets. Songs with the highest scores
become the recommendations.

---

## 4. Data  

The catalog contains 18 songs from genres such as pop, lofi, rock, jazz,
classical, country, EDM, and reggae. It includes features such as energy,
tempo, valence, danceability, and acousticness. The small dataset does not
represent every genre, language, culture, artist, or type of listener.

---

## 5. Strengths  

The model is easy to understand because each recommendation has clear
reasons. It works well when a user's genre and mood appear in the catalog,
such as the pop, lofi, and rock test profiles. It also responds clearly to
changes in energy and acoustic preferences.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The catalog is small and some genres have only one song, so common labels may
be favored over less represented styles. Exact genre and mood matches have
large weights, which can create a filter bubble. The model also ignores tempo
and danceability, uses only one genre and mood per user, and does not add
variety or discovery recommendations.

---

## 7. Evaluation  

I tested the three standard profiles (`High-Energy Pop`, `Chill Lofi`, and
`Deep Intense Rock`) and three adversarial profiles (`Conflicting Energetic
Sad User`, `Boundary Values User`, and `Unknown Genre User`). I compared the
top-five rankings, scores, and explanation reasons. The expected genre and
mood matches generally ranked first. A surprising result was that the
`Unknown Genre User` still received high-energy recommendations because the
energy, valence, and acoustic scores continued to contribute even without a
genre match. The `Boundary Values User` also received ambient and classical
songs, showing that matching one label can outweigh the user's extreme
numeric preferences.

Pairwise comparisons:

- **High-Energy Pop vs. Chill Lofi:** Pop returned energetic pop songs, while
  Lofi shifted to low-energy acoustic songs because genre, mood, and energy
  preferences changed.
- **High-Energy Pop vs. Deep Intense Rock:** Both favored high-energy tracks,
  but Pop ranked `Sunrise City` and Rock ranked `Storm Runner` because the
  genre and mood matches changed.
- **High-Energy Pop vs. Conflicting Energetic Sad User:** Both favored
  energetic songs, but the conflicting user's missing mood match lowered
  scores and left `Storm Runner` first through its genre match.
- **High-Energy Pop vs. Boundary Values User:** Pop favored bright,
  energetic songs, while the boundary profile favored low-energy ambient and
  classical songs because its energy target changed to 0.0.
- **High-Energy Pop vs. Unknown Genre User:** Pop's exact genre and mood
  matches produced a much higher score for `Sunrise City`; the unknown
  profile instead relied mainly on the euphoric mood match and numeric
  similarity.
- **Chill Lofi vs. Deep Intense Rock:** Lofi ranked acoustic, low-energy
  songs, while Rock ranked intense, high-energy songs because both the genre,
  mood, and energy targets were different.
- **Chill Lofi vs. Conflicting Energetic Sad User:** Lofi produced near-perfect
  scores from matching genre and mood, while the conflicting profile had no
  mood match and therefore scored substantially lower.
- **Chill Lofi vs. Boundary Values User:** Both favored acoustic songs, but
  Lofi ranked lofi tracks through exact genre and mood matches, while the
  boundary profile ranked ambient and classical tracks through its labels and
  low-energy target.
- **Chill Lofi vs. Unknown Genre User:** Lofi's known genre and mood produced
  high scores for several songs; the unknown profile lost the genre points
  and shifted toward the euphoric EDM track.
- **Deep Intense Rock vs. Conflicting Energetic Sad User:** Both put
  `Storm Runner` first because of the rock and high-energy preferences, but
  the conflicting user's sad mood had no match, reducing its score.
- **Deep Intense Rock vs. Boundary Values User:** Rock favored intense,
  high-energy music, whereas the boundary profile favored low-energy
  ambient/classical music because the energy targets were opposite.
- **Deep Intense Rock vs. Unknown Genre User:** Rock's exact rock and intense
  matches made `Storm Runner` dominant; the unknown profile instead selected
  `Electric Skyline` through its euphoric mood and high numeric similarity.
- **Conflicting Energetic Sad User vs. Boundary Values User:** The
  conflicting profile favored high-energy rock, while the boundary profile
  favored low-energy ambient music because their energy targets and genre
  labels differed.
- **Conflicting Energetic Sad User vs. Unknown Genre User:** Both lacked a
  useful mood or genre combination, but the known rock preference put
  `Storm Runner` first for the conflicting user, while the euphoric mood
  match put `Electric Skyline` first for the unknown user.
- **Boundary Values User vs. Unknown Genre User:** The boundary profile
  shifted toward low-energy acoustic songs, while the unknown profile shifted
  toward high-energy EDM because their energy, valence, and mood targets
  were very different.

---

## 8. Future Work  

Future versions could use tempo and danceability, and let users choose
several genres or moods. The model could limit repeated artists and reserve
some recommendations for new genres. More songs and real listening feedback
would also make the results more useful.

---

## 9. Personal Reflection  

I learned that small changes in feature weights can change the ranking a lot.
I was surprised that a user with an unknown genre could still receive strong
recommendations from mood and numeric features. This showed me that music
apps can reflect the limits and biases of their data and scoring rules.
