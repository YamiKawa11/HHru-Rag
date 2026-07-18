import requests
import json
cookies = {
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
    'device_magritte_breakpoint': 'xs',
    'device_breakpoint': 'xs',
    'gsscgib-w-hh': 'Ry7AUdotrOyQEKgUKr4aM3tB61ojRk8Mk36MknVF8m4wohQLZTtUMnJSbdmVszKpCEJ4qeZrVf6/qtGNJbD/fVskInhWHdffSlCm/AWtLjoAX1GA9eyihG7+jWJrW1A0h7+nPGQwsXdhiV8J4MOOEMvh6/Sk5l8H8So3fjv3LziPcF/yuE7vJybLLbQODsEzu+pNJ6oEiMyG2ZkvWXJGYgmkS85oZbnwcAyvZx5hrAcfZt2vDjwhF/osF8Xys0TJhb9q4fcRdiR+9AuhBlQjuJ2jGV8=',
    'cfidsgib-w-hh': 'GGUd3uJSiVH0jbQrNtUIx2+JsJJU1raLQRrDTBdMIPjrOK4cYr/JQmXrCNbOTMX4C8GFlbZgghN1vZpBb1BTuhmKxdVH6t6VbJja8XqocUQJG/9cacHaZ+ivVVAsx6L4qzdE2sub2WYa5ppFOay7QQVoFvpnOWxv4A7/kQ==',
    'cfidsgib-w-hh': 'GGUd3uJSiVH0jbQrNtUIx2+JsJJU1raLQRrDTBdMIPjrOK4cYr/JQmXrCNbOTMX4C8GFlbZgghN1vZpBb1BTuhmKxdVH6t6VbJja8XqocUQJG/9cacHaZ+ivVVAsx6L4qzdE2sub2WYa5ppFOay7QQVoFvpnOWxv4A7/kQ==',
    'gsscgib-w-hh': 'Ry7AUdotrOyQEKgUKr4aM3tB61ojRk8Mk36MknVF8m4wohQLZTtUMnJSbdmVszKpCEJ4qeZrVf6/qtGNJbD/fVskInhWHdffSlCm/AWtLjoAX1GA9eyihG7+jWJrW1A0h7+nPGQwsXdhiV8J4MOOEMvh6/Sk5l8H8So3fjv3LziPcF/yuE7vJybLLbQODsEzu+pNJ6oEiMyG2ZkvWXJGYgmkS85oZbnwcAyvZx5hrAcfZt2vDjwhF/osF8Xys0TJhb9q4fcRdiR+9AuhBlQjuJ2jGV8=',
    '__ddg10_': '1784383726',
    '__ddg8_': '7nh6LlKOo7qJQoTc',
    'fgsscgib-w-hh': '9WzQ585c833d032a89749edd43189a405467bf36',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9',
    'baggage': 'sentry-trace_id=8b9a023c21dd4075a3793758a923c0ed,sentry-sample_rand=0.560031,sentry-environment=production,sentry-release=xhh%4026.29.5,sentry-public_key=0cc3a09b6698423b8ca47d3478cfccac,sentry-transaction=%2Fvacancies%2F%7Bcatalog_path%3Apath%7D,sentry-sample_rate=0.001,sentry-sampled=false',
    'priority': 'u=1, i',
    'referer': 'https://hh.ru/vacancies/programmist?page=1&search_session_id=3b8b90d0-7fea-4c02-af8f-bbc63a54b7ce',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Brave";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'sentry-trace': '8b9a023c21dd4075a3793758a923c0ed-9400e00e047da0cc-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'x-gib-fgsscgib-w-hh': '9WzQ585c833d032a89749edd43189a405467bf36',
    'x-gib-gsscgib-w-hh': 'Ry7AUdotrOyQEKgUKr4aM3tB61ojRk8Mk36MknVF8m4wohQLZTtUMnJSbdmVszKpCEJ4qeZrVf6/qtGNJbD/fVskInhWHdffSlCm/AWtLjoAX1GA9eyihG7+jWJrW1A0h7+nPGQwsXdhiV8J4MOOEMvh6/Sk5l8H8So3fjv3LziPcF/yuE7vJybLLbQODsEzu+pNJ6oEiMyG2ZkvWXJGYgmkS85oZbnwcAyvZx5hrAcfZt2vDjwhF/osF8Xys0TJhb9q4fcRdiR+9AuhBlQjuJ2jGV8=',
    'x-hhtmfrom': 'vacancy_search_list',
    'x-hhtmfromlabel': '',
    'x-hhtmsource': '',
    'x-is-spa': 'true',
    'x-requested-with': 'XMLHttpRequest',
    'x-static-version': '26.29.5',
    'x-xsrftoken': 'da4a0fcf6b37829bdaa2bd563de00cf0',
    # 'cookie': '__ddg9_=31.173.120.187; __ddg1_=90AZAXVc5KYivR4qwn9l; display=desktop; crypted_hhuid=BBA088D49E06011D60A6804DD478605A4BDD112B18DA96D7F922CDCD3103E4BB; _xsrf=da4a0fcf6b37829bdaa2bd563de00cf0; hhtoken=iYfJ0Nls5EmP9dOHk81Rs9qNAoR5; hhuid=8XZPoPJynxKDIWpbhlc_Pw--; hhrole=anonymous; GMT=3; TZ=Europe%2FMoscow; HOSTILE_ON=0; iap.uid=841bb9841ac040348dee5533b5c0b94d; __zzatgib-w-hh=MDA0dBA=Fz2+aQ==; regions=1; redirect_host=hh.ru; region_clarified=hh.ru; _ibc=False; uxs_uid=a9a31bd0-82b0-11f1-8fc8-07629bc8f60f; device_magritte_breakpoint=xs; device_breakpoint=xs; gsscgib-w-hh=Ry7AUdotrOyQEKgUKr4aM3tB61ojRk8Mk36MknVF8m4wohQLZTtUMnJSbdmVszKpCEJ4qeZrVf6/qtGNJbD/fVskInhWHdffSlCm/AWtLjoAX1GA9eyihG7+jWJrW1A0h7+nPGQwsXdhiV8J4MOOEMvh6/Sk5l8H8So3fjv3LziPcF/yuE7vJybLLbQODsEzu+pNJ6oEiMyG2ZkvWXJGYgmkS85oZbnwcAyvZx5hrAcfZt2vDjwhF/osF8Xys0TJhb9q4fcRdiR+9AuhBlQjuJ2jGV8=; cfidsgib-w-hh=GGUd3uJSiVH0jbQrNtUIx2+JsJJU1raLQRrDTBdMIPjrOK4cYr/JQmXrCNbOTMX4C8GFlbZgghN1vZpBb1BTuhmKxdVH6t6VbJja8XqocUQJG/9cacHaZ+ivVVAsx6L4qzdE2sub2WYa5ppFOay7QQVoFvpnOWxv4A7/kQ==; cfidsgib-w-hh=GGUd3uJSiVH0jbQrNtUIx2+JsJJU1raLQRrDTBdMIPjrOK4cYr/JQmXrCNbOTMX4C8GFlbZgghN1vZpBb1BTuhmKxdVH6t6VbJja8XqocUQJG/9cacHaZ+ivVVAsx6L4qzdE2sub2WYa5ppFOay7QQVoFvpnOWxv4A7/kQ==; gsscgib-w-hh=Ry7AUdotrOyQEKgUKr4aM3tB61ojRk8Mk36MknVF8m4wohQLZTtUMnJSbdmVszKpCEJ4qeZrVf6/qtGNJbD/fVskInhWHdffSlCm/AWtLjoAX1GA9eyihG7+jWJrW1A0h7+nPGQwsXdhiV8J4MOOEMvh6/Sk5l8H8So3fjv3LziPcF/yuE7vJybLLbQODsEzu+pNJ6oEiMyG2ZkvWXJGYgmkS85oZbnwcAyvZx5hrAcfZt2vDjwhF/osF8Xys0TJhb9q4fcRdiR+9AuhBlQjuJ2jGV8=; __ddg10_=1784383726; __ddg8_=7nh6LlKOo7qJQoTc; fgsscgib-w-hh=9WzQ585c833d032a89749edd43189a405467bf36',
}

params = {
    'page': '49',
    'search_session_id': '3b8b90d0-7fea-4c02-af8f-bbc63a54b7ce',
}
all_datas = []
for i in range(40):
    params['page'] = str(i)
    response = requests.get('https://hh.ru/vacancies/programmist', params=params, cookies=cookies, headers=headers)
    parsed_data = json.loads(response.text)
    datas = parsed_data['vacancySearchResult']['vacancies']
    all_datas+=datas

json_string = json.dumps(all_datas, ensure_ascii=False)
open('all_datas.json', 'w', encoding='utf-8').write(json_string)
