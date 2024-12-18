import pandas as pd
import requests
import time
import os

# Load the refined keywords from the CSV file
keywords_df = pd.read_csv("{local_file_location}")
keywords = keywords_df["Keyword"].tolist()

# NY Times API configuration
api_key = "8XJAMdZ2ESk2cy3vFePtUuomemCCzGxY"  # Replace with your NY Times API key
url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Output file
output_file = "nyt_articles_progressive_final_2.csv"


# Function to fetch articles for a specific keyword and page
def fetch_articles(keyword, start_date, end_date, page=0):
    params = {
        "q": keyword,
        "begin_date": start_date,
        "end_date": end_date,
        "page": page,
        "api-key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:  # Rate limit exceeded
        print(f"Rate limit exceeded for keyword '{keyword}', page {page}. Waiting 12 seconds...")
        time.sleep(12)
        return fetch_articles(keyword, start_date, end_date, page)  # Retry after waiting
    else:
        print(f"Failed to fetch articles for keyword '{keyword}', page {page}. Status code: {response.status_code}")
        return None


# Initialize the output file with headers if it doesn't exist
if not os.path.exists(output_file):
    pd.DataFrame(columns=[
        "keyword", "headline", "abstract", "pub_date", "section_name",
        "type_of_material", "document_type", "news_desk", "snippet",
        "lead_paragraph", "source", "word_count", "uri", "web_url",
        "byline", "keywords"
    ]).to_csv(output_file, index=False)

# Fetch articles for all keywords, date ranges, and pages
start_date = "20240101"  # Example start date (YYYYMMDD)
end_date = "20241201"  # Example end date (YYYYMMDD)

for keyword in keywords:
    print(f"Fetching articles for keyword: {keyword}")
    for page in range(0, 10):
        articles = fetch_articles(keyword, start_date, end_date, page)
        if articles:
            docs = articles.get("response", {}).get("docs", [])
            if not docs:  # Break if no more articles on this page
                print(f"No more articles for keyword '{keyword}' on page {page}.")
                break
            new_data = []
            for doc in docs:
                new_data.append({
                    "keyword": keyword,
                    "headline": doc.get("headline", {}).get("main", ""),
                    "abstract": doc.get("abstract", ""),
                    "pub_date": doc.get("pub_date", ""),
                    "section_name": doc.get("section_name", ""),
                    "type_of_material": doc.get("type_of_material", ""),
                    "document_type": doc.get("document_type", ""),
                    "news_desk": doc.get("news_desk", ""),
                    "snippet": doc.get("snippet", ""),
                    "lead_paragraph": doc.get("lead_paragraph", ""),
                    "source": doc.get("source", ""),
                    "word_count": doc.get("word_count", ""),
                    "uri": doc.get("uri", ""),
                    "web_url": doc.get("web_url", ""),
                    "byline": doc.get("byline", {}).get("original", ""),
                    "keywords": ", ".join([kw["value"] for kw in doc.get("keywords", [])])
                })
            # Append new data to the CSV file
            pd.DataFrame(new_data).to_csv(output_file, mode='a', header=False, index=False)
            print(f"Appended {len(new_data)} articles for keyword '{keyword}', page {page}.")
        else:
            print(f"Stopping fetch for keyword '{keyword}' at page {page}.")
            break
        time.sleep(12)  # Wait 12 seconds to avoid hitting the rate limit

print(f"Progressively fetched articles saved to '{output_file}'.")
