import httpx
from bs4 import BeautifulSoup

URL = 'https://www.woocasino.com/promotions'
proxy_url = 'socks5://fdwahzfe:l5om4lqf7omc@64.137.42.112:5157' # сподіваюсь на момент тестування, проксі працюватиме)



def get_bonuses(url):
    response = httpx.get(url, proxy=proxy_url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    divs = soup.find_all('div', class_='promotions-single')
    result = {}
    for div in divs:
        title = div.find('h2').text.strip()
        description = div.find('p').text.strip()
        result[title] = description
    return result

bouses = get_bonuses(URL)

for t, d in bouses.items():
    print(f"{t}: {d}")