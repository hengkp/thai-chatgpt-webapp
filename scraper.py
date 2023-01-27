import requests
from bs4 import BeautifulSoup

# List of websites to scrape
websites = ["https://www.bbc.com/thai", "https://www.matichon.co.th/", "https://www.siamrath.co.th/"]

# Initialize an empty list to store the text data
text_data = []

# Loop through the websites
for website in websites:
    # Send a GET request to the website
    response = requests.get(website)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the text data from the article tags
    articles = soup.find_all("article")
    for article in articles:
        text_data.append(article.text)

# Save the text data to a file
with open("thai_text_data.txt", "w") as file:
    for data in text_data:
        file.write(data)
