import requests
from bs4 import BeautifulSoup
import time
import webbrowser

# The site - Az oldal amit néz
URL = 'https://bolha.testbike.hu/dh-fr-ossztelos'
# User Agent
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/206.190.33.156 Safari/537.36'}

# Funkció ami akkor lép életbe ha van új termék. 
def OpenTB():
    tb = "https://bolha.testbike.hu/dh-fr-ossztelos"
    # Megnyitja az oldalt
    webbrowser.open(tb)

one = 1
# Loop ami megnézi hogy változótt e a hirdetések száma
while True:
    # Lekér minden infót az adott weblaprol
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # Megkeresi mennyi hirdetés érhető el
    title = soup.find(class_="d_inline_m m_right_17").get_text()
    hirdetes = (title[6:9])
    Hdb = int(hirdetes)

    if 1 == one:
        Hszam = int(hirdetes)
        one += 1
    # Ha váltózott nyissa meg az oldalt
    if Hdb > Hszam:
        print("Új bicó elérhető!")
        print(f"Hirdetések száma: {hirdetes}")
        OpenTB()
    # Ha nem, print
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        ido = current_time

        print(f"\nNincs új hirdetés. Hirdetések száma {hirdetes}. Idő {ido} ")
        print(f"Hdb: {Hdb}, Hszam: {Hszam}")

    Hszam = int(hirdetes)
    time.sleep(60)
