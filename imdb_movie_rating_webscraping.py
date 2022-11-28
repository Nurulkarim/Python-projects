from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Top Rated Movies IMDB'
sheet.append(['Movie Rank','Movie Name','Year of Release','Casting','Movie Rating'])

source=requests.get("https://www.imdb.com/chart/top/")
if source.status_code==200:
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody',class_='lister-list').find_all('tr')
    # print(len(movies))

    
    for movie in movies:
        name=movie.find('td',class_='titleColumn').a.text
        cast=movie.find('td',class_='titleColumn').a['title']
        rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        year=movie.find('td',class_='titleColumn').span.text.strip('()')
        rate=movie.find('td',class_='ratingColumn imdbRating').strong.text
        
        # print(rank,name,year,cast,rate)
        sheet.append([rank,name,year,cast,rate])
        
excel.save('Top Rated Movies IMDB.xlsx')
        
        

