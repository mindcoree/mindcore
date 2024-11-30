from utils import print_menu
from controllers import (handler_exit,
                         handler_orders,
                         handler_view_orders,
                         handler_update_status_orders)


def client(restaurant):
    print('Добро пожаловать в ресторан')
    while True:
        print('1. Меню блюд')
        print('2. Заказать блюдо.')
        print('3. Рассчитать общую стоимость заказа.')
        print('4. Обновление статусов заказов.')
        print('5. Выход.')
        client_choice = input('Ваш выбор:')
        if client_choice in ('1','2','3','4','5'):
            if client_choice == '1':
                print_menu(restaurant)
            elif client_choice == '2':
                handler_orders(restaurant)
            elif client_choice == '3':
                handler_view_orders(restaurant)
            elif client_choice == '4':
                handler_update_status_orders(restaurant)
            elif client_choice == '5':
                handler_exit(restaurant)
                print('Выход из ресторана')
                break
        else:
            print('Ошибка: неправильный ввод')
