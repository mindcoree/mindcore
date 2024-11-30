def print_menu(restaurant):
    for item in restaurant.menu:
        availability = 'Доступен' if item.availability else 'Нет в наличии'
        print(F'Номер блюда: {item.id_dish}')

        print(f"Названия блюда: {item.name_dish}")

        print(f"Категория блюда: {item.category}")

        print(f"Цена блюда: {item.price} тг")

        print(F"Статус: {availability}")

        print("-" * 40)


def print_format_revenue(restaurant):
    print('Отчет по выручке:')
    total_revenue = sum(order.total_price for order in restaurant.orders if order.status == 'Оплачен')
    expected_profit = sum(order.total_price for order in restaurant.orders if order.status == 'В процессе готовки')
    print(f'  Общая выручка: {total_revenue} тг')
    print(f'  Ожидаемая прибыль: {expected_profit} тг')


def print_most_dish(restaurant):
    item_count = {}
    for order in restaurant.orders:
        for item in order.list_menu:
            item_count[item.name_dish] = item_count.get(item.name_dish,0)+1

    most_dish = sorted(item_count.items(), key=lambda x: x[1], reverse=True)

    for index,(name_dish,count_dish) in enumerate(most_dish,start=1):
        print(f"{index} место. {name_dish} - количество заказов {count_dish}.")


def print_filtering_by_category(restaurant):
    category_data = {}

    for order in restaurant.orders:
        for menu in order.list_menu:
            category = menu.category

            if category not in category_data:
                category_data[category] = {
                    "total_dish": 0,
                    "popular_items": {}
                }

            category_data[category]["total_dish"] += 1

            category_data[category]['popular_items'][menu.name_dish] = \
            (category_data[category]['popular_items'].get(menu.name_dish,0) + 1)


    print('Отчет по категориям:')
    for category, data in category_data.items():
        popular_dish = sorted(data["popular_items"].items(), key=lambda x: x[1], reverse=True)

        print(f"Категория: {category}")

        print(f"  Общее количество блюд: {data['total_dish']}")

        print(f"  Топ популярных блюд по категории:")

        for index, (name_dish, count) in enumerate(popular_dish, start=1):
            print(f"    {index}. {name_dish} - {count} заказов")

        print('-' * 40)






