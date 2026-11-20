import pandas as pd
import matplotlib.pyplot as plt


movies = pd.read_csv(r"C:\Users\nexte\Downloads\archive (1)\netflix_movies_detailed_up_to_2025.csv")
tvshows = pd.read_csv(r"C:\Users\nexte\Downloads\archive (1)\netflix_tv_shows_detailed_up_to_2025.csv")

count_movies = len(movies)
count_tv = len(tvshows)

print(f"Movies: {count_movies}")
print(f"TV Shows: {count_tv}")


fig, ax = plt.subplots(figsize=(6,4))
ax.bar(['Movie', 'TV Show'], [count_movies, count_tv], color=['skyblue','orange'])

ax.set_title('Number of Movies VS TV Shows on Netflix')
ax.set_xlabel('Type')
ax.set_ylabel('Count')
ax.grid(axis='y', alpha=0.3) 

plt.tight_layout()
plt.savefig('Movies_VS_TVshows.png', dpi=300) 
plt.show()