import json
import sys

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def build_value_map(values_data):
    return {item["id"]: item["value"] for item in values_data.get("values", [])}

def fill_values(data, value_map):
    if isinstance(data, dict):
        if "id" in data and data["id"] in value_map:
            data["value"] = value_map[data["id"]]
        for key in data:
            fill_values(data[key], value_map)
    elif isinstance(data, list):
        for item in data:
            fill_values(item, value_map)

def main():
    if len(sys.argv) != 4:
        print("Usage: python task3.py <values.json> <tests.json> <report.json>")
        return

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    # Загрузка данных
    values = load_json(values_path)
    tests = load_json(tests_path)

    # Создаем маппинг id -> value
    value_map = build_value_map(values)

    # Заполняем значения в структуре tests
    fill_values(tests, value_map)

    # Сохраняем результат
    save_json(tests, report_path)
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()