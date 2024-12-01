import random
from models import MenuItem, Order
from utils import print_most_dish, print_menu, print_format_revenue, print_filtering_by_category
from storage import save_to_json, load_json


def handler_add_menu(restaurant):
    while True:
        id_dish = input('Введите ID блюда:')
        price = input('Введите цену:')
        if id_dish.isdigit() and price.isdigit():
            id_dish,price = int(id_dish),int(price)
            if id_dish >= 0 and price >= 0:
                name_dish = input('Введите названия блюда:')
                category = input('Введите категорию блюда (основное/закуска/десерт):').lower()
                if category in ("основное", "закуска", "десерт"):
                    availability = input('Доступ к блюду (да/нет):').lower()
                    if availability in ('да','нет'):
                        if availability == 'да':
                            availability = True
                        else:
                            availability = False
                        existing_item = next(filter(lambda item: item.id_dish == id_dish, restaurant.menu),None)
                        if existing_item:
                            print(f'Блюдо {name_dish} с ID {id_dish} уже существует.')
                        else:
                            new_dish = MenuItem(id_dish, name_dish, category, price, availability)
                            restaurant.append_menu(new_dish)
                            print(f'Блюдо {name_dish} успешно добавлено.')
                            break
                    else:
                        print('Ошибка: неправильный ввод данны.')
                else:
                    print('Ошибка: некорректная категория.')
            else:
                print('Ошибка: отрицательные данные.')
        else:
            print('Ошибка: неправильный ввод данны.')


def handler_report(restaurant):
    print(" Меню отчетов по ресторану:")
    while True:
        print('1. Отобразить все блюда.')
        print('2. Фильтрация по выручке.')
        print('3. Топ популярных блюд.')
        print('4. отчет по категориям.')
        print('5. Выход')
        input_report = input('Выбор:')
        if input_report in ('1', '2', '3', '4','5'):
            if input_report == '1':
                print_menu(restaurant)
            elif input_report == '2':
                print_format_revenue(restaurant)
            elif input_report == '3':
                print_most_dish(restaurant)
            elif input_report == '4':
                print_filtering_by_category(restaurant)
            elif input_report == '5':
                print('Выход из отображения отчетов.')
                break
        else:
            print('Ошибка: ')


def handler_exit(restaurant):
    save_to_json(restaurant)


def handler_update_manu(restaurant):
    while True:
        dishes_id = [dish.id_dish for dish in restaurant.menu]
        dishes_name = [dish.name_dish for dish in restaurant.menu]
        dishes_id_and_name = zip(dishes_id,dishes_name)
        print('Сейчас есть такие блюда: ')
        print('-' * 50)
        for item_id,item_name in dishes_id_and_name:
            print(f'    блюдо:{item_name} c ID: {item_id}')
            print('-' * 50)
        id_dish = input('Введите ID блюда которое хотите изменить:')
        name_dish = input('Введите новое или прежнее название блюда:')
        price = input('Введите новую цену блюда:')
        if id_dish.isdigit() and price.isdigit():
            id_dish,price = int(id_dish),int(price)
            if id_dish >= 0 and price >= 0:
                category = input('Введите новую категорию блюда (основное/закуска/десерт):').lower()

                if category in ("основное", "закуска", "десерт"):
                    availability = input('Доступ к блюду (да/нет):').lower()

                    if availability in ('да','нет'):

                        if restaurant.update_menu_dish(id_dish, name_dish, category, price, availability):
                            save_to_json(restaurant)
                        break
                    else:
                       print('Ошибка: неправильный ввод данны.')
                else:
                    print('Ошибка: некорректная категория.')
            else:
                print('Ошибка: отрицательные данные.')
        else:
            print('Ошибка: неправильный ввод данны.')


def handler_orders(restaurant):
    user_name = input('Введите ваше имя для оформления заказа:')
    user_id = random.randint(1, 500)

    while True:
        correct_id = True
        id_dish_list = [item.id_dish for item in restaurant.menu]
        name_dish = [dish.name_dish for dish in restaurant.menu]
        dishes = zip(id_dish_list, name_dish)
        print('Сейчас в ресторане есть такие блюда:')
        for id_dish, name_dish in dishes:
            print(f'ID: {id_dish} Блюдо: {name_dish}')

        print('Введите ID блюд, которые хотите заказать через запятую:')
        input_id = input('ID блюда:').split(',')

        id_menu_user = []

        for ids in input_id:
            ids = ids.strip()
            if not ids.isdigit():
                print(f'Ошибка: неправильный ввод ID')
                correct_id = False
                break
            else:
                id_menu_user.append(int(ids))

        check_id_menu = [id_menu for id_menu in id_menu_user if id_menu not in id_dish_list]
        if correct_id:
            if not check_id_menu:
                items = []
                for id_menu in id_menu_user:
                    item = next(filter(lambda item: item.id_dish == id_menu, restaurant.menu), None)

                    if item:
                        if item.availability:
                            items.append(item)
                        else:
                            print(f'Блюдо с ID {id_menu} не доступно.')
                    else:
                        print(f'Блюдо с ID {id_menu} не найдено в меню.')

                if items:
                    payment_method = input('Введите способ оплаты (наличными / картой): ').lower()
                    if payment_method in ("наличными", "картой"):
                        if payment_method == "наличными":
                            payment_method = 'cash'
                        else:
                            payment_method = 'card'

                        new_order = Order(user_id, user_name, items, payment_method, 'В процессе готовки')
                        restaurant.append_orders(new_order)
                        print(f'Ваш заказ под номером: {user_id} оформлен, пожалуйста, ожидайте.')
                        return
                    else:
                        print(
                            'Ошибка: неправильный способ оплаты. Пожалуйста, укажите правильный способ оплаты (наличными / картой).')
                        continue
            else:
                print(f'Следующие ID блюд не существуют: {check_id_menu}')
        else:
            print('Ошибка: неправильный ввод ID.')

def handler_view_orders(restaurant):
    while True:
        input_id_user = input(f'Введите номер заказа для получения информации: ')

        if input_id_user.isdigit():
            input_id_user = int(input_id_user)
        else:
            print('Введите корректный номер заказа.')
            continue

        id_order = next((item_ord for item_ord in restaurant.orders if item_ord.order_id == input_id_user), None)

        if id_order:
            if id_order.status in ['Оплачен', 'Отменен']:
                print(f'Заказ {input_id_user} уже {id_order.status}.')
                break

            for order in restaurant.orders:
                if order.order_id == input_id_user:
                    items = order.to_dict_order()['items']
                    print(f'Покупатель {order.user_name} с номером {order.order_id}')
                    print(f'  Вы заказали:')
                    total_money = 0
                    print('-' * 40)
                    for item in items:
                        print(f"    Блюдо: {item.get('name_dish')}")
                        print(f"    Категория блюда: {item.get('category')}")
                        print(f"    Цена блюда без налога: {item.get('price')}")
                        total_money = order.total_price
                        print('-' * 40)

                    print(f'C вас: {order.total_price} и оплата {order.payment_method}')
                    print()
                    input_payment = input('Оплатить (Да/Нет):')
                    if input_payment.lower() in ('да', 'нет'):
                        if input_payment == 'да':
                            pay_user = input(f'Укажите сумму оплаты: ')
                            print(total_money)
                            if pay_user.isdigit():
                                pay_user = int(pay_user)
                            else:
                                print('Ошибка: некорректная сумма оплаты.')
                                continue
                            if pay_user > total_money:
                                pay_user -= total_money
                                print(f'Спасибо за покупку. Ваша сдача: {round(pay_user,2)}')
                                order.update_status('Оплачен')
                                print('Приходите еще раз.')
                                return

                            elif pay_user == total_money:
                                print(f"Спасибо за покупку.")
                                order.update_status('Оплачен')
                                print('Приходите еще раз.')
                                return

                            else:
                                print('Вам не хватает средств для оплаты вашего заказа.')
                                input_try = input('Попробовать еще раз (Да/Нет):')
                                if input_try.lower() == 'да':
                                    continue

                                else:
                                    print('Неправильный ввод, попробуйте еще раз.')
                                    continue

                        else:
                            print(f'Ваш заказ под номером {input_id_user} отменен.')
                            order.update_status('Отменен')
                            return

                    else:
                        print('Ошибка при оплате.')
                        continue

        else:
            print(f'Номер заказа: {input_id_user} не существует.')
            break


def handler_show_orders(restaurant):
    print('Отображение информации по клиентам:\n')
    print('-' * 40)

    in_progress_status_orders = []
    paid_status_orders = []
    canceled_status_orders =[]

    def user_order(ord):
        print(f" Номер заказа: {ord.get('order_id')}", end=' |')
        print(f"  Клиент: {ord.get('user_name')}")

        for item_menu in ord.get('items'):
            print('-' * 40)
            print(f'   ID блюда: {item_menu.get("id_dish")}')
            print(f'   Название блюда: {item_menu.get("name_dish")}')
            print(f'   Категория блюда: {item_menu.get("category")}')
            print(f'   Цена блюда: {item_menu.get("price")}')
            print(f'   Наличие блюда: {item_menu.get("availability")}')
        print('-' * 40)
        print(f'   Способ оплаты: {ord.get("payment_method")}')
        print(f"   Итог заказа: {ord.get('total_price')}")
        print('-' * 50)

    for orders_show in restaurant.orders:
        orders = orders_show.to_dict_order()

        if orders.get('status') == 'В процессе готовки':
            in_progress_status_orders.append(orders)

        elif orders.get('status') == 'Отменен':
            canceled_status_orders.append(orders)

        elif orders.get('status') == 'Оплачен':
            paid_status_orders.append(orders)


    if in_progress_status_orders:
        print('Клиенты с заказами в процессе готовки:')
        for order in in_progress_status_orders:
            user_order(order)

    if canceled_status_orders:
        print('Клиенты с отмененными заказами:')
        for order in canceled_status_orders:
            user_order(order)

    if paid_status_orders:
        print('Клиенты с оплаченными заказами:')
        for order in paid_status_orders:
            user_order(order)



def handler_update_status_orders(restaurant):
    print('Добро пожаловать в обновление статуса заказов.')
    print('Укажите ваш номер заказа')
    id_user = input('Ваш номер заказа: ')

    if id_user.isdigit():
        id_user = int(id_user)
    else:
        print('Некорректный номер заказа.')
        return

    idx = next(filter(lambda item_ord: item_ord.order_id == id_user, restaurant.orders), None)

    if idx:
        for order_2 in restaurant.orders:
            if order_2.order_id == id_user:

                if order_2.status in ['Отменен', 'Оплачен']:
                    print('Ваш заказ уже был обработан.')
                    return

        while True:
            print('1. Отменить заказ.')
            print('2. Выход.')
            order_choice = input('Ваш выбор: ')

            if order_choice in ('1', '2'):
                if order_choice == '1':
                    for status_order in restaurant.orders:
                        if status_order.order_id == id_user:
                            status_order.update_status('Отменен')
                            print('Ваш заказ был отменен.')
                            return
                else:
                    print('Выход из обновления статуса заказов.')
                    break
            else:
                print("Пожалуйста, выберите (1 или 2).")
    else:
        print(f'Такого номера заказа {id_user} не существует.')

