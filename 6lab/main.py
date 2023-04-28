from collections import defaultdict
import json

HASH_TABLE_CAPACITY = 19


class HashTable:
    def __init__(self):
        self.data = defaultdict(list)
        self.capacity = HASH_TABLE_CAPACITY
        self.length = 0

    def __str__(self):
        return json.dumps(self.data, indent=4, ensure_ascii=False)

    def add_element(self, key, value):
        hash_key = self.__get_hash(key)
        for element in self.data[hash_key]:
            if element["key"] == key:
                element["value"] = value
                return
        self.length += 1
        if self.length == self.capacity:
            self.__rehash_keys()
        self.data[hash_key].append({'key': key, 'value': value})

    def delete_element(self, key):
        self.length -= 1
        hash_key = self.__get_hash(key)
        self.data[hash_key] = list(filter(lambda element: element["key"] != key, self.data[hash_key]))

    def search_element(self, key):
        elements = self.__get_value(key)
        value = next(filter(lambda element: element["key"] == key, elements))
        return value

    def __get_value(self, key):
        hash_key = self.__get_hash(key)
        try:
            value = self.data[hash_key]
        except KeyError:
            return None
        return value

    def __get_hash(self, key):
        value = ord(key[0]) * 1 + ord(key[1]) * 2 + ord(key[2]) * 3
        return value % self.capacity

    def __rehash_keys(self):
        self.capacity += HASH_TABLE_CAPACITY
        new_data = defaultdict(list)
        for elements in self.data.values():
            for element in elements:
                hashed_key = self.__get_hash(element["key"])
                new_data[hashed_key].append(element)
        self.data = new_data


def main():
    hash_table = HashTable()

    hash_table.add_element("Россия", "Москва")
    hash_table.add_element("Россия", "Владивосток")
    hash_table.add_element("Германия", "Баруссия")
    hash_table.add_element("Германия", "Берлин")
    hash_table.add_element("Италия", "Рим")
    hash_table.add_element("Италия", "Сицилия")
    hash_table.add_element("Китай", "Пекин")
    hash_table.add_element("Китай", "Ганконг")
    hash_table.add_element("Франция", "Брест")
    hash_table.add_element("Франция", "Париж")
    hash_table.add_element("Беларусь", "Слоним")
    hash_table.add_element("Украина", "Киев")
    hash_table.add_element("Польша", "Варшава")
    hash_table.add_element("Испания", "Мадрид")
    hash_table.add_element("Финляндия", "Хельсинки")
    hash_table.add_element("Япония", "Токио")
    hash_table.add_element("Индия", "Нью-Дели")
    hash_table.add_element("Иран", "Тегеран")
    hash_table.add_element("Казахстан", "Астана")
    hash_table.add_element("Индонезия", "Джакарта")
    hash_table.add_element("Турция", "Анкара")
    hash_table.add_element("Монголия", "Улан-Батор")
    hash_table.add_element("Авганистан", "Кабул")

    while True:
        print("Add - press 1")
        print("Delete - press 2")
        print("Search - press 3")
        print("Print - press 4")

        print("To exit - press 0")
        choose = input("Enter choise: ")
        match choose:
            case "1":
                key = input("Enter key: ")
                data = input("Enter data: ")
                hash_table.add_element(key, data)
            case "2":
                key = input("Enter key: ")
                hash_table.delete_element(key)
            case "3":
                key = input("Enter key: ")
                print(hash_table.search_element(key))
            case "4":
                print(hash_table)
            case "0":
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
