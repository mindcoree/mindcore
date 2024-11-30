from admin_panel import admin
from storage import load_json
from client_panel import client

def main():
    restaurant = load_json()
    print("Добро пожаловать в  Система управления рестораном")
    while True:
        print("1. Зайти от имени Администратора")
        print("2. Зайти от имени Клиента")
        print("3. Выход из системы управления рестораном")
        input_choice = input('Ваш выбор:')
        if input_choice in ('1', '2', '3'):
            if input_choice == '1':
                admin(restaurant)
            elif input_choice == '2':
                client(restaurant)
            else:
                print('exit')
                break
        else:
            print('Ошибка: Введите ( 1 / 2 / 3 )')


if __name__ == "__main__":
    main()


