from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
file = open('./story/grimm.txt', 'w')  

BASE_URL = "https://www.cs.cmu.edu/~spok/grimmtmp/001.txt"

for NUM in range(1, 210):
    if NUM < 10:
        page = '00'+ str(NUM)
    elif NUM < 100:
        page = '0'+ str(NUM)
    else:
        page = str(NUM)
    PAGE_URL = 'https://www.cs.cmu.edu/~spok/grimmtmp/' + page + '.txt' 
    print(PAGE_URL)
    try:
        page = urlopen(PAGE_URL)
    except Exception as e:
        print(e) 
        continue    # skip 404 errors 
    soup = BeautifulSoup(page.read(), 'html.parser')
    file.write(soup.text + ' \n')
file.close()
            
