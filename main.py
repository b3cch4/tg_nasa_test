import os, requests
from datetime import datetime
from urllib.parse import urlparse, unquote


payload_apod = {'start_date': '2022-05-18',
            'end_date': '2022-05-18', #Взял интервал по одному дню
            'api_key': 'ql1pnWkzzifmIEKTQkbLse2beYOMOToFbmNYCYQL'}
api_key = 'ql1pnWkzzifmIEKTQkbLse2beYOMOToFbmNYCYQL'
url_apod = 'https://api.nasa.gov/planetary/apod'
url_spacex = 'https://api.spacexdata.com/v4/launches'
url_epic = 'https://api.nasa.gov/EPIC/api/natural?api_key=ql1pnWkzzifmIEKTQkbLse2beYOMOToFbmNYCYQL'
path_spacex = "images/spacex"
path_apod = "images/apod"
path_epic = "images/epic"


def get_extension(url):
    '''Функция, возвращающая расширение файла'''
    ext = (
        os.path.splitext(
            os.path.split(
                urlparse(
                    unquote(url)
                ).path
            )[-1]
        )[-1]
    )[1:]
    return ext


def downl_img_to_fold(url, path, serial_number):
    '''Функция загружает фотографии по ссылке, полученной в качестве аргумента <url>'''
    filename = f'{path}/{serial_number}.{get_extension(url)}'
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url_spacex, path_spacex):
    '''Получает и загружает фотографии последнего запуска шатла.'''
    responce = requests.get(url_spacex)
    for item in reversed(responce.json()):
        if item['links']['flickr']['original'] != []:
            list_of_spacex_links = item['links']['flickr']['original']
            break
    for serial_number, link in enumerate(list_of_spacex_links):
        print(link)
        downl_img_to_fold(link, path_spacex, serial_number)


def fetch_nasa_apod_images(url_apod, payload, path_apod):
    '''Функция загружает фотографии NASA из раздела =APOD='''
    response = requests.get(url_apod, params=payload)
    for serial_number, response in enumerate(response.json()):
        downl_img_to_fold(response['url'], path_apod, serial_number)


def fetch_nasa_epic_images(url_epic, path_epic, api_key):
    '''Функция загружает фотографии NASA из раздела =EPIC='''
    response = requests.get(url_epic)
    response.raise_for_status()
    list_of_epic = []
    for item_responce in response.json():
        name = item_responce.get('image')
        date_time = datetime.fromisoformat(response.json()[0].get('date'))
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        day = date_time.strftime("%d")
        epic_url = 'https://api.nasa.gov/EPIC/archive/natural'
        list_of_epic.append(
            f'{epic_url}/{year}/{month}/{day}/png/{name}.png?api_key={api_key}'
        )
    for serial_number, item_url in enumerate(list_of_epic):
        downl_img_to_fold(item_url, path_epic, serial_number)
        
        
def main():
    fetch_spacex_last_launch(url_spacex, path_spacex)
    fetch_nasa_apod_images(url_apod, payload_apod, path_apod)
    fetch_nasa_epic_images(url_epic, path_epic, api_key)
    
    
if __name__ == '__main__':
    main()
