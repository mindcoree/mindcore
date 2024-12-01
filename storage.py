import json
from models import Restaurant,MenuItem,Order


def save_to_json(restaurant):

    with open('menu.json', 'w', encoding='utf-8') as menu_file:
        json.dump([item.to_dict_menu() for item in restaurant.menu], menu_file, ensure_ascii=False,indent=3)

    with open('orders.json','w',encoding='utf-8') as orders_file:
        json.dump([order.to_dict_order() for order in restaurant.orders],orders_file,ensure_ascii=False,indent=3)
    #пример \u041f\u0440\u0438\u0432\u0435\u0442

def load_json(menu_file='menu.json',orders_file='orders.json'):


    with open(menu_file,'r',encoding='utf-8') as menu_file:
        menu = json.load(menu_file)
    list_menu = [MenuItem.from_dict_menu(item) for item in menu]


    with open(orders_file,'r',encoding='utf-8') as orders_file:
        orders  =json.load(orders_file)
    list_orders = [Order.from_dict_order(order) for order in orders]


    restaurant = Restaurant('Ресторан',list_menu,list_orders)

    return restaurant




