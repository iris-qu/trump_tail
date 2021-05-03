from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

# 2000-2021.txt
# 1950-1999.txt
# 1900-1949.txt
# 1851-1899.txt

titleFile = open('./data/2019-2021_title.txt', 'w')
contentFile = open('./data/2019-2021_content.txt', 'w')

BASE_URL = "https://www.nytimes.com/sitemap"

for year in range(2019, 2022):
    # eg. output https://www.nytimes.com/sitemap/2017
    YEAR_URL = BASE_URL + '/' + str(year)
    for month in range(1, 10):
        if month < 10:
            strMonth = '0' + str(month)
        else:
            strMonth = str(month)
        # eg. output https://www.nytimes.com/sitemap/2017/01
        MONTH_URL = YEAR_URL + '/' + strMonth
        for date in range(1, 31):
            # eg. outputhttps://www.nytimes.com/sitemap/2017/01/31
            if date < 10:
                strDate = '0' + str(date)
            else:
                strDate = str(date)
            DATE_URL = MONTH_URL + '/' + strDate + '/'
            print(DATE_URL)
            try:
                page = urlopen(DATE_URL)
            except Exception as e:
                print(e)
                continue    # skip 404 errors
            soup = BeautifulSoup(page.read(), 'html.parser')
            ul = soup.find('ul', {'class': 'css-cmbicj'})
            lists = ul.findChildren("li", recursive=False)
            for li in lists:
                link = li.findChild("a", recursive=False, href=True)
                if "Trump" not in link.text:
                    continue
                print(DATE_URL)
                print(link.text)

                titleFile.write(link.text + '\n')
                try:
                    newsPage = urlopen(link['href'])
                except Exception as e:
                    print(e)
                    continue    # skip 404 errors
                newsSoup = BeautifulSoup(newsPage.read(), 'html.parser')
                summary = newsSoup.find('p', {'id': 'article-summary'})
                if summary:
                    contentFile.write(summary.text + '\n')
                newsContents = newsSoup.findAll('p', {'class': 'css-axufdj'})
                for c in newsContents:
                    contentFile.write(c.text + '\n')

titleFile.close()
contentFile.close()
