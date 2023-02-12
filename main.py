from config import OPERATIONS_URL
from utils import get_data


def main():
    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(info)

if __name__ == "__main__":
    main()
