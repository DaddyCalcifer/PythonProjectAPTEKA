from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

root = Tk()
root.title("Аптека")
root.geometry("500x500")

class Drug:
    def __init__(self, name, count, price):
        self.name = name
        self.count = int(count)
        self.price = int(price)

inventory = [
    (Drug("Анальгин", int(10), int(100))),
    (Drug("Аспирин", int(5), int(70))),
    (Drug("Валидол", int(7), int(180))),
    (Drug("Но-шпа", int(3), int(290)))
]
def show_inventory():
    global tree
    tree.delete(*tree.get_children())
    for item in inventory:
        #print(item, inventory[item])
        tree.insert("",END, values=[item.name,item.count,item.price])

def add_item():
    global inventory
    found = False
    try:
        item_name = item_entry.get()
        item_quantity = int(quantity_entry.get())
        item_price = int(price_entry.get())
        for item in inventory:
            if item.name == item_name:
                item.count += item_quantity
                item.price = item_price
                found = True
                break
        if not found:
            inventory.append(Drug(item_name, item_quantity, item_price))
    except ValueError as e:
        showerror(title="Ошибка", message="Сообщение об ошибке: " + str(e))
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)
    show_inventory()

def sell_item():
    for x in tree.selection():
        x_ = tree.item(x)
        for item in inventory:
            if item.name == x_["values"][0]:
                inventory.remove(item)

    show_inventory()

def clear_inventory():
    inventory.clear()
    show_inventory()

item_label = ttk.Label(root, text="Товар:")
item_label.pack()

item_entry = ttk.Entry(root)
item_entry.pack()

quantity_label = ttk.Label(root, text="Количество:")
quantity_label.pack()

quantity_entry = ttk.Entry(root)
quantity_entry.pack()

price_label = ttk.Label(root, text="Цена:")
price_label.pack()

price_entry = ttk.Entry(root)
price_entry.pack()

add_button = ttk.Button(root, text="Добавить", command=add_item)
add_button.pack()

sell_button = ttk.Button(root, text="Продать", command=sell_item)
sell_button.pack()

#show_button = ttk.Button(root, text="Показать остатки товаров", command=show_inventory)
#show_button.pack()

clear_button = ttk.Button(root, text="Очистить все товары", command=clear_inventory)
clear_button.pack()

columns = ("name", "count", "price")

tree = ttk.Treeview(columns=columns, show="headings")

# определяем заголовки
tree.heading("name", text="Название")
tree.heading("count", text="Количество")
tree.heading("price", text="Цена (руб.)")
tree.column("#1", stretch=YES, width=200)
tree.column("#2", stretch=YES, width=100)
tree.column("#3", stretch=YES, width=100)
tree.pack()

show_inventory()
root.mainloop()
