"""import requests
from django.shortcuts import render
from bs4 import BeautifulSoup


# url = 'https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_5?qid
# =1654868229&s=electronics&sr=1-5&th=1'
url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,42879.html?round=0'


def get_link_data(request):
    url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,42879.html?round=0'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.193 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    played = {}
    not_played = {}
    for teams, time in zip(soup.find_all('div', class_="teams grid-38 grid-mt-48 grid-msw-48"),
                           soup.find_all('div', class_="season__game-data grid-4 grid-mt-8 grid-msw-12 grid-ms-48")):
        day = time.find('span', class_="day").get_text()
        month = time.find('span', class_="month").get_text()
        hour = time.find('span', class_="hour").get_text()
        team = teams.find('a', class_='team').get_text()
        team_versus = teams.find('a', class_='team versus').get_text()
        score = teams.find('span', class_="score")

        if score:
            score_text = score.get_text().strip()
            played[team, score_text, team_versus] = (day, month, hour)

        else:
            not_played[team, "vs", team_versus] = (day, month, hour)

    #print(played)
    #print(not_played)
    matches = played | not_played
    #print(matches)
    for key, value in matches.items():
        print(key, ' : ', value)

    return render(request, 'links/index.html', matches)

"""

mydict = {" 1.1 " " 1.2 " " 1.3 ": " aA " " aB " " aC ",
          " 2.1 " " 2.2 " " 2.3 ": " bA " " bB " " bC ",}

for key, values in mydict.items():
    print(key, values)

x=mydict.items()



