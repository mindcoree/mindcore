class MenuItem:
    def __init__(self, id_dish:int, name_dish:str, category:str, price:int, availability:bool):
        self.id_dish = id_dish
        self.name_dish = name_dish
        self.category = category
        self.availability = availability
        self.price = price

    def to_dict_menu(self):
        return {
            'id_dish': self.id_dish,
            'name_dish':self.name_dish,
            'category':self.category,
            'price':self.price,
            'availability':self.availability
        }

    def update_availability(self,update_availability):
        self.availability = update_availability

    @classmethod
    def from_dict_menu(cls,data:dict):
        return cls(
            id_dish = data["id_dish"],
            name_dish = data["name_dish"],
            category = data["category"],
            price = data["price"],
            availability = data["availability"]
        )


class Order:
    def __init__(self,order_id:int,user_name:str,list_menu:list[MenuItem],payment_method:str,status):
        self.order_id = order_id
        self.user_name = user_name
        self.total_price = (sum(item.price for item in list_menu)+sum(item.price for item in list_menu)/10)
        self.payment_method = payment_method
        self.list_menu = list_menu
        self.status = status

    def update_status(self,update_status:str):
        self.status = update_status

    def to_dict_order(self):
        return {
            'order_id':self.order_id,
            'user_name':self.user_name,
            'items':[item.to_dict_menu() for item in self.list_menu],
            'total_price':self.total_price,
            'payment_method':self.payment_method,
            'status': self.status
        }

    @classmethod
    def from_dict_order(cls,data:dict):

        items_menu = [MenuItem.from_dict_menu(item) for item in data['items']]

        return cls(
            order_id = data['order_id'],
            user_name = data['user_name'],
            list_menu = items_menu,
            payment_method=data['payment_method'],
            status = data["status"]
        )


class Restaurant:
    def __init__(self,name_restaurant:str,menu:list[MenuItem],orders:list[Order]):
        self.orders = orders
        self.name_restaurant = name_restaurant
        self.menu = menu

    def append_menu(self,item:MenuItem):
        self.menu.append(item)

    def append_orders(self,ord:Order):
        self.orders.append(ord)

    def update_menu_dish(self,id_dish,new_name_dish,new_category,new_price,new_availability):

        item = next(filter(lambda item_id:item_id.id_dish == id_dish,self.menu),None)
        if item:

            self.menu = [dish for dish in self.menu if dish.id_dish != id_dish]

            if new_name_dish:
                item.name_dish = new_name_dish
            if new_category:
                item.category = new_category
            if new_price:
                item.price = new_price
            if new_availability:
                item.availability = new_availability

            self.append_menu(item)

            print(f'Блюдо: {new_name_dish} с ID {id_dish} успешно обновлено.')
            return True
        else:
            print(f"Блюдо: {new_name_dish} с ID {id_dish} не найдено.")
            return False





