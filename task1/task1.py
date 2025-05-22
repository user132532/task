import sys

def main():
    # Проверяем, что передано ровно два аргумента
    if len(sys.argv) != 3:
        print("Ошибка: Необходимо указать два аргумента - n и m")
        return

    try:
        # Преобразуем аргументы в целые числа
        n = int(sys.argv[1])
        m = int(sys.argv[2])

        # Проверяем, что n и m положительные
        if n <= 0 or m <= 0:
            print("Ошибка: n и m должны быть положительными числами")
            return

        path = []
        current = 1
        visited = set()

        while current not in visited:
            path.append(current)
            visited.add(current)
            current = ((current + m - 2) % n) + 1

        # Выводим результат
        print(''.join(map(str, path)))

    except ValueError:
        print("Ошибка: Аргументы должны быть целыми числами")

if __name__ == "__main__":
    main()