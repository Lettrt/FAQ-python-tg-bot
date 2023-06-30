
import requests
import csv
from bs4 import BeautifulSoup
import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


def get_html(url: str) -> str:
    HEADERS = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=HEADERS, verify=False)
    return response.content


def scraper(html: str, url: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="serp-item")
    result = []
    for item in items:
        result.append({
            'Company': item.find('a', {'class': 'serp-item__title'}).get_text(strip=True),
            'Job': item.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).get_text(strip=True),
            'Type': item.find('div', class_="bloko-h-spacing-container bloko-h-spacing-container_base-0").get_text(strip=True),
        })
    return result


def save_csv(filename, items):
    with open(filename, 'w', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(['Вакансия', 'Компания', "Опыт"])
        for item in items:
            writer.writerow([item['Company'], item['Job'], item['Type']])
    return 'Finish'

def send_senior(message):
    category = 'jobs2'
    url = 'https://hh.ru/search/vacancy?text=Python+senior&from=suggest_post&salary=&area=2760&ored_clusters=true'
    html = get_html('{}/{}'.format(url, category))
    parser = scraper(html=html, url=url)
    save_csv(f'{category}.csv', parser)
    with open('jobs2.csv', encoding='UTF-8') as file:
        read = csv.DictReader(file)
        for i in read:
            bot.send_message(message.chat.id, f'Компания - {i["Компания"]}\nВакансия - {i["Вакансия"]}\nТребуемый опыт - {i["Опыт"]}')
