import sys
import math

def main():
    # Проверяем, что передано ровно два аргумента
    if len(sys.argv) != 3:
        print("Ошибка: Необходимо указать два аргумента - файл окружности и файл точек")
        return

    try:
        # Получаем пути к файлам
        circle_file = sys.argv[1]
        points_file = sys.argv[2]

        # Считываем данные из файла окружности
        with open(circle_file, 'r') as f:
            x_center = float(f.readline())
            y_center = float(f.readline())
            radius = float(f.readline())

        # Считываем координаты точек из файла
        with open(points_file, 'r') as f:
            for line in f:
                if line.strip() == "": continue
                x, y = map(float, line.strip().split())
                distance = math.hypot(x - x_center, y - y_center)

                # Определяем положение точки относительно окружности
                if abs(distance - radius) < 1e-9:
                    print(0)
                elif distance < radius:
                    print(1)
                else:
                    print(2)

    except FileNotFoundError:
        print("Ошибка: Указанный файл не найден")
    except ValueError:
        print("Ошибка: Неверный формат данных в файле")

if __name__ == "__main__":
    main()