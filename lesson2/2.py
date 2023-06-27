import json


def write_order_to_json(item, quantity, price, buyer, date):
    OBJ = json.load(open('orders.json', 'r'))
    items = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    OBJ['orders'].append(items)
    json.dump(OBJ, open('orders.json', 'w'), ensure_ascii=False)


write_order_to_json('ЗС', '222', '46464', 'Ivanov', '27.03.2023')
write_order_to_json('принтер', '222', '46464', 'Ivanov', '27.03.2023')
