import requests
import json
import urllib
from bs4 import BeautifulSoup

baseURL = "https://mangasusuku.xyz/"
prox = "https://mangasusuku-xyz.translate.goog/"
proxq = "?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=id"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "sucuri_cloudproxy_uuid_5efbb9a1e=42bd93cd1cce9bc091398a318bf30bd5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

def home(request):
    response = requests.get(baseURL, headers=headers)
    data = response.text.replace(prox, baseURL).replace(proxq, "")
    soup = BeautifulSoup(data, "html.parser")

    obj = {}
    # obj["url"] = request.build_absolute_uri()
    obj["populer"] = []
    mangas = soup.find(class_='popconslide').find_all("div", class_="bs")
    for manga in mangas:
        obj["populer"].append({
            'name': manga.find("a")['title'],
            'thumb': manga.find("img")['src'],
            'chapter': manga.find("div", class_="epxs").text,
            'url': manga.find("a")['href']
        })

    return obj

if __name__ == "__main__":
    print(json.dumps(home(requests), indent=2))