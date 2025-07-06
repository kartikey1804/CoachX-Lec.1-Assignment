from bs4 import BeautifulSoup


with open("file.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

print(soup.title.text)

# print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))