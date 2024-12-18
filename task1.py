import requests
from bs4 import BeautifulSoup

url = "https://go.slotimo.com/login/"

headers = {
    "accept": "text/html,applicatigiton/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "cookie": "rbzsessionid=004b02513e4d0b4a016d17256cb8b893; ASPSESSIONIDQADCTQRB=BPHIOANDKMGFKFDJHOLDCAJH; SLO_GWPT_Show_Hide_tmp=0; SLO_wptGlobTipTmp=0; rbzid=FKSBtYF/Q4Oo+/qBgIcIzY6hdVkVVjYGnnuxCw1U6ELxprUlp78dNvhZpGnCWr4Qq80ieIJMCiumZR6Dk3foEBpjhTh5BZ4zvTL2F1+D00eFy+lwr6fD6Gedijh5cMSFeqkptxSGh/ZEc20nfqith2BYlxHw0X+be3Io6oHZdDIZ+JrVRhMitur74JiF+/MKb50sSuKX4w//NGx8pisKYORqj18uYdMr+Hv73iXEk0+KDtl0boT+li+wAtvSLzzj",
    "host": "go.slotimo.com",
    "referer": "https://go.slotimo.com/login/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
} # без хедерів не підгружає

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.find('div', class_='login-form').prettify())