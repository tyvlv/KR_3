import requests


def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "Данные получены успешно"
        return None, f"Ошибка в получении данных. Status_code:{response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "Ошибка в получении данных. Нет связи с сервером"
    except requests.exceptions.JSONDecodeError:
        return None, "Ошибка в получении данных. Не удалось декодировать в формат json"
