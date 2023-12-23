from bs4 import BeautifulSoup

with open("C:/Users/prana/OneDrive/Desktop/Python Code/Side-Projects/Web Scraping/Beautiful Soup/website.html",encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.a) #type: ignore

anchor_tags = soup.find_all('a')

# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

a_tags = soup.find_all("li a")
print(a_tags)

#If attribute is defined then we can use .get("attribute")