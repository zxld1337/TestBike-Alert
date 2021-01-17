import requests
from bs4 import BeautifulSoup
import time
import webbrowser

# The site - Az oldal amit néz
URL = 'https://bolha.testbike.hu/dh-fr-ossztelos'
# User Agent
headers = {"User-Agent": 'Mozilla/5.0} # its has to be your own

# Function that activates when a new bike is available - Funkció ami akkor lép életbe ha van új bicó. 
def OpenTB():
    tb = "https://bolha.testbike.hu/dh-fr-ossztelos"
    # Opens the site - Megnyitja az oldalt
    webbrowser.open(tb)

one = 1
# Loop which looks at how this number of ads is - Loop ami megnézi hogy változótt-e a hirdetések száma
while True:
    # Retrieves information from that web page - Lekéri az infót az adott weblapról
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # Finds how many ads are available - Megkeresi mennyi hirdetés érhető el
    title = soup.find(class_="d_inline_m m_right_17").get_text()
    hirdetes = (title[6:9])
    Hdb = int(hirdetes)

    if 1 == one:
        Hszam = int(hirdetes)
        one += 1
    # If changed, open the page - Ha váltózott nyissa meg az oldalt
    if Hdb > Hszam:
        print("Új bicó elérhető!")
        print(f"Hirdetések száma: {hirdetes}")
        OpenTB()
    # If not print the following text -  Ha nem, irja ki a az adott szöveget
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        ido = current_time

        print(f"\nNincs új hirdetés. Hirdetések száma {hirdetes}. Idő {ido} ")
        print(f"Hdb: {Hdb}, Hszam: {Hszam}")

    Hszam = int(hirdetes)
    time.sleep(60)
