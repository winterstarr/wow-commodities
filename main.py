from api import get_data
from write import save_data


def main():
    data = get_data()
    save_data(data)


if __name__ == '__main__':
    main()
