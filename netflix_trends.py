import pandas as pd

# 1. Ingest the Data
file_path = 'netflix_titles.csv'
media_data = pd.read_csv(file_path)

# 2. Data Cleaning & Transformation
# Dropping rows with missing critical data
cleaned_data = media_data.dropna(subset=['release_year', 'rating', 'duration'])

# 3. Exploratory Data Analytics (EDA)
# Query 1: Count of content produced per year
content_by_year = cleaned_data['release_year'].value_counts().sort_index(ascending=False).head(10)

# Query 2: Breakdown of TV Shows vs Movies
content_type_split = cleaned_data['type'].value_counts()

print("Top 10 Most Recent Years of Content Production:\n", content_by_year)
print("\nContent Type Distribution:\n", content_type_split)
