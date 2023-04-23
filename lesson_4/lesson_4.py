import json
import time
from bs4 import BeautifulSoup as bs
import sqlite3
import requests
import uuid






def get_response(url: str, headers: dict) -> requests.models.Response:

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response
    
    print('Нет ответа от сервера')
    exit()


def get_soup(response: requests.models.Response) -> list:

    soup = bs(response.text, 'html.parser')

    quotes_soup = soup.find_all('div', attrs={'class': 'quote'})

    try:
        is_have_next = soup.find('li', attrs={'class': 'next'}).find('a')['href']

    except AttributeError:
        is_have_next = 'stop'

    return quotes_soup, is_have_next


def make_dict(quote) -> dict:

    quote_text = quote.find('span', attrs={'class': 'text'}).text
    quote_author = quote.find('small', attrs={'class': 'author'}).text
    quote_tags = list(map(lambda tag: tag.text, quote.find_all('a', attrs={'class': 'tag'})))
        
    return {
            'quote_text': quote_text,
            'quote_author': quote_author,
            'quote_tags': quote_tags
            }

def make_db(connection, cursor):
    make_db_query = """
    CREATE TABLE IF NOT EXISTS quotes(
        id VARCHAR(36) PRIMARY KEY,
        quote_text TEXT,
        quote_author VARCHAR(25),
        quote_tags TEXT
    )
    """
    cursor.execute(make_db_query)
    connection.commit()

def inser_data(connection, cursor, data):
    insert_db_quote = """
        INSERT INTO quotes VALUES(
            ?, ?, ?, ?
        )
    """

    values = (
        str(uuid.uuid1()),
        data.get('quote_text'),
        data.get('quote_author'),
        str(data.get('quote_tags'))
        )
    
    cursor.execute(insert_db_quote, values)
    connection.commit()


def main():

    url = 'https://quotes.toscrape.com'

    headers = {
        'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'
    }

    result = []

    is_have_next = ''

    connection = sqlite3.connect('sqlite.db')
    cursor = connection.cursor()

    make_db(connection, cursor)
    
    while True:

        response = get_response(url + is_have_next, headers)

        quotes_soup, is_have_next = get_soup(response)

        for guote in quotes_soup:
            data = make_dict(guote)
            inser_data(connection, cursor, data)
            
            result.append(
                data.copy()
            )
        
        if is_have_next == 'stop':
            break
    
        time.sleep(1)



    with open('result.json', 'w') as file:
        json.dump(result, file, indent=2)


if __name__ == '__main__':
    main()