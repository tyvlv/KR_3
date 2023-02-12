import requests
from datetime import datetime
from pprint import pprint

def get_data(url):
    """Получает данные по адресу URL"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "Данные получены успешно\n"
        return None, f"Ошибка в получении данных. Status_code:{response.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "Ошибка в получении данных. Нет связи с сервером\n"
    except requests.exceptions.JSONDecodeError:
        return None, "Ошибка в получении данных. Не удалось декодировать в формат json\n"


def get_filtered_data(data, filtered_empty_from=False):
    """Выбирает данные со статусом перевода EXECUTED"""
    filtered_data = []
    for item in data:
        if "state" in item and item["state"] == "EXECUTED":
            if filtered_empty_from:
                if "from" in item:
                    filtered_data.append(item)
                continue
            filtered_data.append(item)
    return filtered_data


def get_last_values(data, count_last_values):
    """Сортирует данные по дате и выбирает последние N транзакций"""
    data = sorted(data, key=lambda item: item["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    """Форматирует данные в требуемое представление"""
    formatted_data = []
    for item in data:
        date = datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = item["description"]
        from_info, from_bill = "", ""
        if "from" in item:
            sender = item["from"].split()
            from_bill = sender.pop(-1)
            from_info = " ".join(sender)
            from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
        to = f"{item['to'].split()[0]} **{item['to'][-4:]}"
        operation_amount = f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to}
{operation_amount}""")

    return formatted_data