# 🎬 Cinematic Recommender Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)

A sophisticated, content-based movie recommendation web application. This engine analyzes the metadata of thousands of films and instantly suggests 5 highly similar movies based on your selection, dynamically fetching official high-resolution posters via the TMDB API.

**🔗 [Experience the Live Application Here](PASTE_YOUR_STREAMLIT_LINK_HERE)**

---

## 🧠 How the Engine Works

This is not a simple genre-matching tool; it utilizes Natural Language Processing (NLP) to understand the "DNA" of a movie. 

1. **Data Preprocessing:** Built using the TMDB 5000 Movies Dataset. The text data (overviews, genres, keywords, cast, and crew) was extracted, cleaned, and merged into a single "tags" column for every movie.
2. **Text Vectorization:** Used Scikit-Learn's `CountVectorizer` to convert these text tags into mathematical vectors, ignoring standard English stop words.
3. **Similarity Matrix:** Calculated the **Cosine Similarity** between these vectors. The model measures the multidimensional angle between movies to determine how closely related they are, creating a 5000x5000 similarity matrix.
4. **API Integration:** When a recommendation is generated, the app queries the TMDB API in real-time to fetch the official poster artwork using the unique movie ID.

---

## 🛠️ Technical Stack

* **Core Logic:** Python, Pandas, NumPy
* **Machine Learning:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
* **Web Scraping/API:** `requests` module, TMDB Developer API
* **Frontend UI:** Streamlit (Custom CSS for dark cinematic theming)
* **Deployment:** Streamlit Community Cloud

---

## 💡 Overcoming Deployment Challenges: The 100MB Limit
During cloud deployment, the generated `similarity.pkl` model file was **176.22 MB**, which triggered a hard rejection from GitHub's 100 MB file limit. 

Instead of relying on costly Git Large File Storage (LFS), I wrote a custom Python compression script to cast the matrix data types from standard `float64` down to `float16`. **This reduced the file size by 75% (down to ~45 MB)**, allowing for seamless cloud deployment with zero loss in recommendation accuracy.

---

## 📸 Application Interface
*(Optional: Take a screenshot of your live web app, drag and drop the image right here, and delete this line!)*

---

## 🚀 Run it Locally

To experiment with the code on your own machine:

**1. Clone the repository**
```bash
git clone [https://github.com/Yash23061103/Movie-Recommender-System.git](https://github.com/Yash23061103/Movie-Recommender-System.git)
cd Movie-Recommender-System
2. Install dependencies

pip install -r requirements.txt

3. API Key Configuration

* Create a free account at The Movie Database (TMDB).

* Generate a Developer API Key (v3 auth).

* Open app.py and replace the placeholder string in the fetch_poster() function with your new key.

4. Launch the application
streamlit run app.py
