from requests.exceptions import RequestException
import json
import requests

def crawl_amazon_best_sellers(url: str) -> str:
    API_TOKEN = "<Crawlbase Normal requests token>"
    API_ENDPOINT = "https://api.crawlbase.com/"

    params = {
        "token": API_TOKEN,
        "url": url,
        "scraper": 'amazon-best-sellers'
    }

    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()

    json_string_content = response.text
    json_data = json.loads(json_string_content)

    if json_data["original_status"] != 200:
        raise Exception[f"Unable to crawl '{url}'"]
    
    return json_data["body"]

def crawl_amazon_best_sellers_products(url: str) -> str:
    products = []

    try:
        json_data = crawl_amazon_best_sellers(url)
        products.extend(json_data["products"])
        next_page = json_data.get("pagination", {}).get("nextPage") or -1
        while next_page > 0:
            json_data = crawl_amazon_best_sellers(f"{url}?pg={next_page}")
            products.extend(json_data["products"])
            next_page = json_data.get("pagination", {}).get("nextPage") or -1
    except RequestException as e:
        print(f"Request failed: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

    return products

if __name__ == "__main__":

    products_json = crawl_amazon_best_sellers_products('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_electronics_0')
    print(json.dumps(products_json, indent=2))
