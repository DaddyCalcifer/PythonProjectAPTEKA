from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Аптека")
root.geometry("500x500")

inventory = [
    ("Анальгин", 10, 100),
    ("Аспирин", 5, 70),
    ("Валидол", 7, 180),
    ("Но-шпа", 3, 290)
]

def show_inventory():
    tree.delete(*tree.get_children())
    for item in inventory:
        #print(item, inventory[item])
        tree.insert("",END, values=item)

def add_item():
    global inventory
    item_name = item_entry.get()
    item_quantity = quantity_entry.get()
    item_price = price_entry.get()
    inventory.append((item_name, item_quantity, item_price))
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)
    show_inventory()

def sell_item():
    item_name = item_entry.get()
    if item_name in inventory:
        inventory[item_name] -= 1
    else:
        print("Данный товар отсутствует в аптеке.")
    item_entry.delete(0, END)
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

show_button = ttk.Button(root, text="Показать остатки товаров", command=show_inventory)
show_button.pack()

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
