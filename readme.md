# 🎬 Hybrid Movie Recommendation System (Netflix-Style)

This project implements a **real-world Hybrid Recommendation System** similar to Netflix and Amazon.  
It combines **Collaborative Filtering** and **Content-Based Filtering** to recommend personalized movies to users.  
Additionally, a **Streamlit Web App** is included for **interactive movie recommendations**.

---

## 📌 Problem Type
- **Machine Learning Category:** Supervised Learning  
- **Problem Formulation:** Recommendation / Ranking Problem  
- **Not Classification or Pure Unsupervised**

---

## 🚀 Project Overview

Modern recommendation systems do not rely on a single technique.  
This project uses a **Hybrid approach**, which is the **most widely used method in industry today**.

### Hybrid =  
- Collaborative Filtering (user behavior)  
- Content-Based Filtering (movie features)  
- Final score = weighted combination of both

---

## 🧠 How the System Works

1. User–movie interaction data is collected from ratings  
2. Similar movies are found using **item-based collaborative filtering**  
3. Movie content similarity is calculated using **TF-IDF on genres**  
4. Both scores are combined to generate a final ranking  
5. Already watched movies are excluded  
6. Top-N movies are recommended to the user  
7. **Streamlit Web App Features:**
   - **Enter User ID**: Select the user for whom recommendations are generated  
   - **Select a Movie**: Pick a reference movie for better personalization  
   - **Collaborative vs Content Weight (α)**: Adjust the balance between collaborative and content-based filtering  
   - **Get Recommendations**: App displays top-N recommended movies instantly  

---

## 📂 Dataset

**MovieLens Dataset (Real-world, Industry Standard)**  
Files used:
- `ratings.csv` – user ratings for movies  
- `movies.csv` – movie titles and genres  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- TF-IDF Vectorizer  
- Cosine Similarity  
- Streamlit  
- Jupyter Notebook  

---

## 🧩 Recommendation Techniques Used

### 1️⃣ Collaborative Filtering (Item-Based)
- Uses user rating patterns
- Finds similar movies based on user behavior

### 2️⃣ Content-Based Filtering
- Uses movie genres
- Applies NLP (TF-IDF) to compute similarity

### 3️⃣ Hybrid Strategy
Final Score:


This approach helps handle:
- Cold start problem  
- Better personalization  
- Higher recommendation accuracy  

---

## 📊 Streamlit Web App

The Streamlit App allows **interactive movie recommendations**:

1. **Enter User ID** – choose a valid user from the dataset  
2. **Select a Movie** – the movie to base recommendations on  
3. **Adjust α Slider** – balance between collaborative filtering and content-based filtering  
4. **Click “Recommend Movies”** – top-N movies will be displayed immediately  

Example Output:

