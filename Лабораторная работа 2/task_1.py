# TODO Напишите функцию для поиска индекса товара

def index(a, b):
    i = 0
    d = None
    for c in b:
        if c == a:
            d = i
            break
        i += 1
    return d

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(find_item, items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
