from data_frame import generate_data_frame
from openai import OpenAI

OPENAI_API_KEY = "<OpenAI API Key>"
client = OpenAI(api_key=OPENAI_API_KEY)

df = generate_data_frame('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_electronics_0')

# Generate GPT-based summary
top_titles = "\n".join([f"{i+1}. {row['title']} (${row['price_value']}, {row['rating']}⭐, {row['customerReviewCount']} reviews)"
                            for i, row in df.iterrows()])
ai_prompt = f"""
Given the following Amazon best sellers in the Electronics category:

{top_titles}

Summarize the trends in this list. Mention anything about pricing, ratings, review volume, and any common product features.
"""

try:
    ai_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": ai_prompt}],
        temperature=0.5,
        max_tokens=200
    )
    ai_summary = ai_response.choices[0].message.content.strip()
except Exception as e:
    print(e)
    ai_summary = None

print("\n AI-Generated Trend Summary:\n")
print(ai_summary)
