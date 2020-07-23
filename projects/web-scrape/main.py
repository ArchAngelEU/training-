import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd 
import string
import re




# Starting Request: 


def get_content():
    

    location  = input ('Please enter a location to look for prices: ').replace(" ", "")
    
    # Sets up the request a URL goes here for the Zoopla website. 
  
    request = requests.get(f'https://www.zoopla.co.uk/for-sale/property/{location}/?identifier={location}&page_size=100&q={location}%20&search_source=refine&radius=0&pn='
    ,headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = bs(request.content, "html.parser")
    pages = (soup.find('div', {'class': 'paginate'}).text)
    prop = (soup.find_all("div",{"class": "listing-results-wrapper"}))
            
    items_list = []    

    # Loops through all the pages of the search and fetches the data.
                
    for page in range (1, len(pages)):
        
        base_url = requests.get(f'https://www.zoopla.co.uk/for-sale/property/basildon/?identifier=basildon&page_size=100&q=basildon%20&search_source=refine&radius=0&pn={page}')
        content = base_url.content
        soup = bs(content, 'html.parser')
        items = soup.find_all('div', {'class': 'listing-results-wrapper'})

        for item in prop:
                            
            items = {}    
            
            # Fetches the infomation that we need and the puts this data into a dataframe
            # Which is then outputted to a CSV which cab later be further maniplated.   
            
            a = (item.find('a', {"class": "listing-results-price"}).text.replace('\n', '').replace(" ", ""))
            items['price'] = re.sub('[abcdefghijklmnopqurtGOuvwrxysz]', "", a)
            items['address'] = item.find_all("a", {"class": "listing-results-address"})[0].text
                
            try:   
                items['beds'] =  item.find("span", {"class": "num-icon num-beds"}).text
                items['reception'] = item.find("span", {"class": "num-icon num-reception"}).text
                items['bathrooms'] = item.find("span", {"class": "num-icon num-baths"}).text
            except:
                items['beds']=None 
                items['reception']=None
                items['bathrooms']=None
            
                
            items['contact_number'] = item.find('div', {"class": "listing-results-attr"}).find('p')
            
            items_list.append(items)
            
      # Adding list of dictonarys to a dataframe   
      
 
    dataframe = pd.DataFrame(items_list)
    dataframe.to_csv(f'{location}.csv')
    


get_content()








