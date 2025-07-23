import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset
df = pd.read_csv("C:/Users/Rimuru/Desktop/Intern/Codesoft/Task_4/movies.csv")
# Make sure this CSV exists
df['genre'] = df['genre'].fillna('')

# TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute cosine similarity
cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation logic
def get_recommendations(title):
    if title not in df['title'].values:
        return []

    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# GUI
def recommend():
    movie = entry.get().strip()
    if not movie:
        messagebox.showerror("Input Error", "Please enter a movie title")
        return

    recommendations = get_recommendations(movie)
    if not recommendations:
        messagebox.showinfo("No Match", f"No recommendations found for '{movie}'")
    else:
        result_text.set('\n'.join(recommendations))

# GUI Setup
root = tk.Tk()
root.title("🎬 Movie Recommendation System")
root.geometry("400x300")

tk.Label(root, text="Enter Movie Title:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Get Recommendations", font=("Arial", 12), command=recommend).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 11), justify=tk.LEFT).pack(pady=10)

tk.Button(root, text="Quit", command=root.quit).pack()

root.mainloop()