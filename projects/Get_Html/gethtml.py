from bs4 import BeautifulSoup
import requests
c = True
while c:
  url =input('Enter The Url Here: ')
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  print(soup.prettify())
  cc = input('''
  
    Do You Want To Scrap Another WebSite (Y/N): ''')
  if cc.lower() == 'n':
    print('Thanks..!')
    c = False