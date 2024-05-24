import sys # For args

class Record:
    def __init__(self, order_id, order_date, product_name, product_cat, sell_count, piece_price, summary_price):
        self.order_id = order_id.strip()
        self.order_date = order_date.strip()
        self.product_name = product_name.strip()
        self.product_cat = product_cat.strip()
        self.sell_count = int(sell_count)
        self.piece_price = float(piece_price)
        self.summary_price = float(summary_price)

    def __str__(self):
        return f'(Номер заказа: {self.order_id}, Дата заказа: {self.order_date}, Название товара: {self.product_name}, Категория товара: {self.product_cat}, Количество продаж: {self.sell_count}, Цена за единицу: {self.piece_price}, Общая стоимость: {self.summary_price})'

class Records:
    def __init__(self, records):
        self.rows = records

    def summary_income(self):
        return sum(x.summary_price for x in self.rows)

    def most_sold_product(self):
        product_count = {}
        for record in self.rows:
            if record.product_name in product_count:
                product_count[record.product_name] += record.sell_count
            else:
                product_count[record.product_name] = record.sell_count
        return max(product_count.items(), key=lambda item: item[1])

    def highest_revenue_product(self):
        revenue = {}
        for record in self.rows:
            if record.product_name in revenue:
                revenue[record.product_name] += record.summary_price
            else:
                revenue[record.product_name] = record.summary_price
        return max(x[1] for x in revenue.items())

    def detailed_report(self):
        total_income = self.summary_income()
        product_details = {}
        for record in self.rows:
            if record.product_name not in product_details:
                product_details[record.product_name] = {"units_sold": 0, "total_revenue": 0}
            product_details[record.product_name]["units_sold"] += record.sell_count
            product_details[record.product_name]["total_revenue"] += record.summary_price
        
        for name, details in product_details.items():
            details["revenue_share"] = (details["total_revenue"] / total_income) * 100
        
        return total_income, product_details

def ask_yn(prompt):
    ans = ""
    while ans != "y" and ans != "n":
        ans = input(f"{prompt} (y/n): ")
    return ans == "y"


if len(sys.argv) < 2 or not sys.argv[1]:
    print("Введите путь к файлу с данными в качестве аргумента")
    exit()

lines = None
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Файл не найден")
    exit()

records = []
offset = 1 if ask_yn("Присутствует ли в файле заголовочная строка?") else 0
for line in lines[offset:]:
    s = line.strip().split(",")
    if len(s) == 7:
        try:
            records.append(Record(*s))
        except ValueError:
            print(f"ВНИМАНИЕ: Данные строки в неверном формате, пропуск; Строка: {line}")
    else:
        print(f"ВНИМАНИЕ: Данные строки в неверном формате, пропуск; Строка: {line}")

records = Records(records)

total_income = records.summary_income()
most_sold = records.most_sold_product()
highest_revenue = records.highest_revenue_product()
total_income, report = records.detailed_report()

print(f"Общая выручка: {total_income}")
print(f"Наибольшее количество продаж: {most_sold}")
print(f"Наибольшая выручка с товара: {highest_revenue}")
print("Отчёт по товарам:")
for product, details in report.items():
    print(f"{product}: Продано единиц - {details["units_sold"]}, Общая выручка - {details["total_revenue"]:.2f}, Доля от общей выручки - {details["revenue_share"]:.2f}%")

