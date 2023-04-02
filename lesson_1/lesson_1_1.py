import requests
import json

# 1. Посмотреть документацию к API GitHub, разобраться как вывести список 
# репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

URL = 'https://api.github.com/users/'
DEFAULTUSER = 'KulikovIK'
USERREPOS = []


def get_data(url: str) -> json:
    response = requests.get(url)
    if response.status_code == 200:
        print('Получен ответ')
        return response.json()


def get_url() -> str:
    username = input('Введите имя пользователя: ')
    username = username if username else DEFAULTUSER

    return URL + f'{username}/repos'


def get_repo_names(repos: json) -> USERREPOS:
    for repo in repos:
        USERREPOS.append(repo['name'])
    return USERREPOS


def main():
    url = get_url()
    repos = get_data(url)
    USERREPOS = get_repo_names(repos)

    with open('lesson_1_1_repo.json', 'w') as result:

        json.dump(USERREPOS, result, indent=2)


if __name__ == '__main__':
    main()
