class Memory:
    def __init__(self):
        self.memory = []

    def __call__(self):
        print("Decimal: ")
        for element in self.memory:
            print(self.to_decimal(element.copy()), end=' ')
        print("\nBinary: ")
        for element in self.memory:
            print(element)

    @staticmethod
    def __word_comparison(word_1: list, word_2: list, sort_flag: bool) -> bool:
        result = {"g": False, "l": False}
        for i in range(len(word_1)):
            result_g = result["g"] or (word_1[i] == 0 and word_2[i] == 1 and not result["l"])
            result_l = result["l"] or (word_1[i] == 1 and word_2[i] == 0 and not result["g"])
            result["g"], result["l"] = result_g, result_l
        if result["l"]:
            return sort_flag
        if result["g"]:
            return not sort_flag

    def sort(self, sort_flag: bool):
        for i in range(len(self.memory)):
            for j in range(len(self.memory) - i - 1):
                if self.__word_comparison(self.memory[j], self.memory[j + 1], sort_flag):
                    self.memory[j], self.memory[j + 1] = self.memory[j + 1], self.memory[j]

    def match_search(self, value: int) -> int:
        binary_value = self.to_binary(value)
        match_counter = [0] * len(self.memory)
        for i in range(len(self.memory)):
            for j in range(len(self.memory[i])):
                if self.memory[i][j] == binary_value[j]:
                    match_counter[i] += 1
        max_counter = max(match_counter)
        index_of_max_counter = match_counter.index(max_counter)
        return self.to_decimal(self.memory[index_of_max_counter].copy())

    @staticmethod
    def to_binary(x: int) -> list:
        binary_x = []
        x = abs(x)
        while x:
            binary_x.insert(0, x % 2)
            x //= 2
        for i in range(8 - len(binary_x)):
            binary_x.insert(0, 0)
        return binary_x

    @staticmethod
    def to_decimal(binary_x: list) -> int:
        x = 0
        binary_x.reverse()
        for i in range(0, len(binary_x)):
            x += binary_x[i] * 2 ** i
        return x

    def insert(self, value: int) -> None:
        element = self.to_binary(value)
        self.memory.append(element)


def main():
    memory = Memory()
    values = [13, 7, 15, 1, 56, 93, 60, 33, 11, 12]
    for value in values:
        memory.insert(value)
    memory()

    while 1:
        print("--------------------------")
        print("Match Search - press 1")
        print("Sort - press 2")
        print("To exit - press 0")
        choose = input("Enter choise: ")
        match choose:
            case "1":
                word_to_search = int(input("Enter the number: "))
                print(f"Decimal: {word_to_search}, binary: {memory.to_binary(word_to_search)}")
                result = memory.match_search(word_to_search)
                print(f"Match search: decimal {result}, binary {memory.to_binary(result)}")
            case "2":
                print("1 - greater, 2 - less")
                x = int(input())
                if x == 1:
                    memory.sort(True)
                elif x == 2:
                    memory.sort(False)
                memory()
            case "0":
                break
            case _:
                print("Invalid input")


if __name__ == '__main__':
    main()
