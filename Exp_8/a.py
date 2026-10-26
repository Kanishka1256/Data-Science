from bs4 import BeautifulSoup
import pandas as pd

# Read the permitted, locally saved HTML file
with open("reviews.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

# Update these selectors to match the source HTML
review_blocks = soup.select(".review")

records = []

for block in review_blocks:
    review_element = block.select_one(".review-text")
    rating_element = block.select_one(".rating")
    title_element = block.select_one(".review-title")

    review_text = (
        review_element.get_text(" ", strip=True)
        if review_element else ""
    )

    rating_text = (
        rating_element.get_text(" ", strip=True)
        if rating_element else ""
    )

    title = (
        title_element.get_text(" ", strip=True)
        if title_element else ""
    )

    if review_text:
        records.append({
            "title": title,
            "review": review_text,
            "rating": rating_text
        })

df = pd.DataFrame(records)

df.to_csv("product_reviews.csv", index=False, encoding="utf-8-sig")

print(df.head())
print("Total reviews extracted:", len(df))
print("Saved to product_reviews.csv")
