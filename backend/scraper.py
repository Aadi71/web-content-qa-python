import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except Exception as e:
        raise Exception(f"Error scraping {url}: {str(e)}")
