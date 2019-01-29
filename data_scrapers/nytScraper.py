from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

# 2000-2019.txt
# 1950-1999.txt
# 1900-1949.txt
# 1851-1899.txt

file = open('./data/2000-2019.txt', 'w')  

BASE_URL = "https://spiderbites.nytimes.com/"

for year in range(2000, 2019):
    YEAR_URL = BASE_URL + str(year) + '/articles_' + str(year) + '_' # eg. output https://spiderbites.nytimes.com/2017/articles_2017_
    for month in range(1, 13): 
        if month < 10:
            strMonth = '0' + str(month)
        else:
            strMonth = str(month)
        MONTH_URL = YEAR_URL + strMonth + '_0000' # eg. output https://spiderbites.nytimes.com/2017/articles_2017_01_0000
        for part in range(1, 10):
            PART_URL = MONTH_URL + str(part) + '.html' # eg. output https://spiderbites.nytimes.com/2017/articles_2017_01_00001.html
            print(PART_URL)
            try:
                page = urlopen(PART_URL)
            except Exception as e:
                print(e) 
                continue    # skip 404 errors 
            print(PART_URL)
            soup = BeautifulSoup(page.read(), 'html.parser')
            ul = soup.find('ul', {'id': 'headlines'})
            lists = ul.findChildren("li" , recursive=False)
            for li in lists:
                link = li.findChild("a", recursive=False)
                file.write(link.text + '\n')
file.close()
            
