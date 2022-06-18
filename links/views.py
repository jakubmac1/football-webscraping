from django.shortcuts import render
# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.template.response import TemplateResponse
from collections import OrderedDict
from django.http import HttpResponse

'''def leagues(request, slug):
    return TemplateResponse(request, 'links/leagues.html', {})'''


def index(request):
    return render(request, 'links/main.html')


def ekstraklasa(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/ekstraklasa,1.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})


def liga1(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/i-liga,2.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})


def liga2(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/ii-liga,3.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})


def liga3(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,43145.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})

def liga4(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,42149.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})

def liga5(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,42173.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})

def liga6(request):

    url = 'https://www2.laczynaspilka.pl/rozgrywki/nizsze-ligi,42877.html?round=0'
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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})

def liga7(request):

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

    matches = played | not_played
    '''for key, value in matches.items():
        print(key, ' : ', value)'''

    matches2 = {}
    for key in reversed(matches):
        matches2[key] = matches[key]

    return render(request, 'links/index.html', {"matches2" : matches2})


'''def get_link_data(request):
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

    matches = played | not_played
    for key, value in matches.items():
        print(key, ' : ', value)
    context = matches

    return render(request, 'links/index.html', context)'''

