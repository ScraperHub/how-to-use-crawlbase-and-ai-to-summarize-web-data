from web_data import crawl_amazon_best_sellers_products
import pandas as pd

def generate_data_frame(url: str):
    products_json = crawl_amazon_best_sellers_products(url)
    df = pd.DataFrame(products_json)

    df["rating"] = df["customerReview"].str.extract(r"(\d+(?:\.\d+)?)").astype(float).fillna(0)
    df["price_value"] = df["price"].str.replace("$", "").astype(float)
    df["category"] = "Streaming Devices"

    return df

if __name__ == "__main__":

    df = generate_data_frame('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_electronics_0')
    print(df)
