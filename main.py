import sys # For args

class Record:
    def __init__(self, order_id, order_date, product_name, product_cat, sell_count, piece_price, summary_price):
        self.order_id = order_id
        self.order_date = order_date
        self.product_name = product_name
        self.product_cat = product_cat
        self.sell_count = int(sell_count)
        self.piece_price = float(piece_price)
        self.summary_price = float(summary_price)

    def __str__(self):
        return f'(Номер заказа: {self.order_id}, Дата заказа: {self.order_date}, Название товара: {self.product_name}, Категория товара: {self.product_cat}, Количество продаж: {self.sell_count}, Цена за единицу: {self.piece_price}, Общая стоимость: {self.summary_price})'

if len(sys.argv) < 2 or not sys.argv[1]:
    print("Введите путь к файлу с данными в качестве аргумента")
    exit()

lines = None
try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except (FileNotFoundError):
    print("Файл не найден")
    exit()

records = list()
for line in lines: 
    s = line.split(',')
    if len(s) == 7:
        try:
            records.append(Record(*s))
        except (ValueError):
            # TODO
            print("Wrong type, skip record")
    else:
        # TODO
        pass

for r in records:
    print(r)
