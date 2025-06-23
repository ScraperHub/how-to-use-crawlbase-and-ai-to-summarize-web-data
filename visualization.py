from data_frame import generate_data_frame
import matplotlib.pyplot as plt

df = generate_data_frame('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_electronics_0')

plt.figure(figsize=(10, 5))
plt.barh(df["title"], df["customerReviewCount"], color='skyblue')
plt.xlabel("Review Count")
plt.title("Amazon Best Sellers: Number of Reviews")
plt.tight_layout()
plt.savefig("reviews_bar_chart.png")
plt.show()

# Scatter: Rating vs Review Count
plt.figure(figsize=(6, 5))
plt.scatter(df["rating"], df["customerReviewCount"], s=100, c=df["price_value"], cmap="cool", alpha=0.8)
for i, row in df.iterrows():
    plt.text(row["rating"] + 0.01, row["customerReviewCount"], f'{i+1}', fontsize=9)
plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.title("Rating vs Review Volume (Color: Price)")
plt.colorbar(label="Price ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("rating_vs_reviews.png")
plt.show()

# Save structured data
df.to_csv("amazon_best_sellers_summary.csv", index=False)
