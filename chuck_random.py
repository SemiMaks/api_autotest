import requests


class Test_new_joke():
    """Запрос новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Запрос случайной шутки"""

        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успешно получен ответ ресурса!")
        else:
            print("Провал!")

        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна!")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck присутствует!")
        else:
            print("Chuck отсутствует!")


random_joke = Test_new_joke()

random_joke.test_create_new_random_joke()
