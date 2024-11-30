from controllers import (handler_add_menu,
                         handler_update_manu,
                         handler_report,
                         handler_exit,
                         handler_show_orders)


def admin(restaurant):
    while True:
        login = input('введите пароль:')
        if login == '123':
            print('Вы вошли в систему администрации')
            while True:
                print('1. Добавление нового блюд в меню.')
                print('2. Обновление информации о блюдах.')
                print('3. Отобразить отчет.')
                print('4. Отображение всех заказов.')
                print('5. Выход из Системы управления рестораном.')
                admin_choice = input('Ваш выбор:')
                if admin_choice in ('1','2','3','4','5'):
                    if admin_choice == '1':
                        handler_add_menu(restaurant)
                    elif admin_choice == '2':
                        handler_update_manu(restaurant)
                    elif admin_choice == '3':
                        handler_report(restaurant)
                    elif admin_choice == '4':
                        handler_show_orders(restaurant)
                    elif admin_choice == '5':
                        handler_exit(restaurant)
                        print('Выход из админ панели.')
                        return
                else:
                    print('Ошибка: неправильный ввод')
        else:
            print('Неправильный пароль!')
            print('Попробуйте еще раз.')