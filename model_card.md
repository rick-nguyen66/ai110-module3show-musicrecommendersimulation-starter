# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

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

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
