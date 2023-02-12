from config import OPERATIONS_URL, FILTERED_EMPTY_FROM, COUNT_LAST_VALUES
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("Вывод данных:\n")
    for item in data:
        print(item, end="\n\n")

if __name__ == "__main__":
    main()
