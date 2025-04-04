import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_google(query, num_results=10):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": num_results
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for result in data.get("organic_results", []):
        title = result.get("title", "")
        link = result.get("link", "")
        results.append({"title": title, "link": link})

    return results

def extract_emails_from_site(url):
    try:
        html = requests.get(url, timeout=5).text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        emails = set()
        for word in text.split():
            if "@" in word and "." in word:
                clean_email = word.strip("(),<>\"\'")
                if len(clean_email) < 100:
                    emails.add(clean_email)
        return list(emails)
    except:
        return []
