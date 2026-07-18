import json
import time
import random
import requests
from bs4 import BeautifulSoup
import lxml

# Настройки
INPUT_FILE = 'all_datas.json'
OUTPUT_FILE = 'all_datas_updated.json'
SAVE_EVERY = 50  # Сохранять промежуточный результат каждые 50 записей

# 1. Настройка заголовков (Headers) и куки (Cookies)
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}

COOKIES = {
    '__ddg9_': '31.173.120.187',
    '__ddg1_': '90AZAXVc5KYivR4qwn9l',
    'display': 'desktop',
    'crypted_hhuid': 'BBA088D49E06011D60A6804DD478605A4BDD112B18DA96D7F922CDCD3103E4BB',
    '_xsrf': 'da4a0fcf6b37829bdaa2bd563de00cf0',
    'hhtoken': 'iYfJ0Nls5EmP9dOHk81Rs9qNAoR5',
    'hhuid': '8XZPoPJynxKDIWpbhlc_Pw--',
    'hhrole': 'anonymous',
    'GMT': '3',
    'TZ': 'Europe%2FMoscow',
    'HOSTILE_ON': '0',
    'iap.uid': '841bb9841ac040348dee5533b5c0b94d',
    '__zzatgib-w-hh': 'MDA0dBA=Fz2+aQ==',
    'regions': '1',
    'redirect_host': 'hh.ru',
    'region_clarified': 'hh.ru',
    '_ibc': 'False',
    'uxs_uid': 'a9a31bd0-82b0-11f1-8fc8-07629bc8f60f',
    '__ddg8_': 'xiSGGnI7li5EyoMa',
    '__ddg10_': '1784391519',
    'gsscgib-w-hh': 'Bj8XyBUQAfZ1D6T4rfNixTFYLXiqe1ncuQzlqrXq0vV5422yL8jD9MzVC/1jXWHHr2URwBRye3nVFTWVy8iWZR95GMnpPh3scGfEbeeq0E7emqFMYNX9EwKSKnjFnxdqC7+DoV/9SuvA/lG8etnNQ39tDVDwxrRCNBWobJCC1mgusS6wQuo4OZmGphG7kP4yVval4uUnryrClaAK30vUVRbT75Yia2BbMG1YNedULfq4uhDl7N4EoGd290KiIFS6u/Dx42mavCkqeIST0CBzIChLha8=',
    'cfidsgib-w-hh': 'uvtnLGP4RQkSANPcj63v/dgkYoqiUNyAUBIYmochfbz8oIxZCmrQh9F5lkg2WHo1m2X+dpnbQXmyfIA1KMzfH2kk+S09QtVhAQeo57UGa/YRN7aJDFoORfrO4lB5JEb3lIB//atgO7E8xz2tCt12Ph9CXG4xEiXX1V0NhA==',
    'device_magritte_breakpoint': 'xs',
    'device_breakpoint': 'xs',
    'fgsscgib-w-hh': 'bwJHdf5b17c4b0c22729d34bcfc6464e58439b21'
}

def main():
    # Пробуем загрузить уже обновленный файл, если он есть
    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            restored_data = json.load(f)
        print(f"Загружен файл {OUTPUT_FILE} (продолжаем работу).")
    except FileNotFoundError:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            restored_data = json.load(f)
        print(f"Загружен файл {INPUT_FILE} (начинаем с нуля).")

    total_count = len(restored_data)
    print(f"Всего записей: {total_count}\n")

    session = requests.Session()
    session.headers.update(HEADERS)
    session.cookies.update(COOKIES)

    for i, o in enumerate(restored_data, 1):
        link = f"https://hh.ru/vacancy/{o['vacancyId']}"
        
        # Если описание уже спарсено (и оно не пустое) — пропускаем
        if o.get('vacancy-description'):
            print(f"[{i}/{total_count}] Пропуск (уже собрано): {link}")
            continue

        try:
            response = session.get(link, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml")
                vacancy_div = soup.find('div', class_='vacancy-description')

                if vacancy_div:
                    clean_text = vacancy_div.get_text(separator="\n", strip=True)
                    o['vacancy-description'] = clean_text
                    status_msg = "Успешно"
                else:
                    # Блок не найден — просто логируем и идем дальше
                    status_msg = "Блок не найден (другая верстка/капча) — пропускаем"
                    o['vacancy-description'] = "ОШИБКА_ПАРСИНГА" # Помечаем, чтобы не пытаться парсить ее снова при перезапуске
                    
            elif response.status_code == 404:
                status_msg = "Вакансия удалена (404) — пропускаем"
                o['vacancy-description'] = "ВАКАНСИЯ_УДАЛЕНА"
                
            else:
                status_msg = f"Ошибка {response.status_code}"
                if response.status_code == 403:
                    print(f"[{i}/{total_count}] {link} -> {status_msg}")
                    print("ОСТАНОВКА: Получен 403 Forbidden. IP забанен.")
                    break # Прерываем цикл только при жестком бане
                
        except Exception as e:
            status_msg = f"Ошибка сети: {type(e).__name__}"
        
        print(f"[{i}/{total_count}] {link} -> {status_msg}")
        
        # Промежуточное сохранение
        if i % SAVE_EVERY == 0:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
                json.dump(restored_data, outfile, ensure_ascii=False, indent=4)
            print(f"--- [ЧЕКПОИНТ] Данные сохранены ({i}/{total_count}) ---")

        # Плавающая пауза
        time.sleep(random.uniform(2.0, 4.0))

    # Финальное сохранение
    print("\nСохранение финального файла...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        json.dump(restored_data, outfile, ensure_ascii=False, indent=4)
    print("Готово!")

if __name__ == "__main__":
    main()