import requests # type: ignore
import csv

key = "27efc51e4de84a94b1c1979e753b9e37"
url = "https://newsapi.org/v2/top-headlines?sources=lequipe&apiKey=" + key

response = requests.get(url)
dictionary = response.json()

# Extract the last ten news articles
articles = dictionary.get("articles", [])[:10]

# Define the CSV file name
csv_file = "last_ten_news.csv"

# Write the articles to the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Title", "Description", "URL", "Published At"])
    
    # Write the article details
    for article in articles:
        writer.writerow([article.get("title"), article.get("description"), article.get("url"), article.get("publishedAt")])

print(f"Last ten news articles have been saved to {csv_file}")