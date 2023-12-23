from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
article_text = []
article_upvotes = []
article_links = []
soup = BeautifulSoup(response.text, 'html.parser')

news_list = soup.find_all('span', class_= "titleline")

for news in news_list:
    print(news.a.get_text())
    print(news.a.get('href')+'\n')
    article_text.append(news.a.get_text())
    article_links.append(news.a.get('href'))

upvotes_count = soup.find_all('span', class_= "score")


for upvotes in upvotes_count:
    print(upvotes.get_text())
    article_upvotes.append(upvotes.get_text().split()[0])


print("The ariticle with maximum upvotes is: "+ article_text[article_upvotes.index(max(article_upvotes))] + "--> with "+ f"{max(article_upvotes)} upvotes.")