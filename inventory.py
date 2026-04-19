import tkinter as tk
from tkinter import messagebox

MAX_ITEMS = 5

money = 400

SHOP = {
    "Phone": 100,
    "Food": 10,
    "PC": 200,
    "Suit": 30,
    "Charger": 30,
    "Toy": 15
}

inventory = []
equipped_item = None


def refresh_inventory():
    listbox.delete(0, tk.END)

    for i, item in enumerate(inventory):
        text = item
        if i == equipped_item:
            text += " (Equipped)"
        listbox.insert(tk.END, text)

    money_label.config(text=f"Money: {money}$")


def buy_item():
    global money

    item = shop_listbox.get(tk.ACTIVE)

    if not item:
        return

    price = SHOP[item]

    if money < price:
        messagebox.showwarning("Error", "Not enough money")
        return

    if len(inventory) >= MAX_ITEMS:
        messagebox.showwarning("Error", "Inventory full")
        return

    money -= price
    inventory.append(item)

    refresh_inventory()


def equip_item():
    global equipped_item

    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Error", "Select item")
        return

    equipped_item = selected[0]

    refresh_inventory()


def remove_item():
    global equipped_item

    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Error", "Select item")
        return

    index = selected[0]
    item = inventory.pop(index)

    if index == equipped_item:
        equipped_item = None

    refresh_inventory()


def open_inventory():
    inventory_frame.pack(side="left", padx=10, pady=10)
    shop_frame.pack(side="right", padx=10, pady=10)
    money_label.pack(side="top", pady=10)


def close_inventory():
    global inventory, equipped_item

    inventory.clear()
    equipped_item = None

    listbox.delete(0, tk.END)

    inventory_frame.pack_forget()
    shop_frame.pack_forget()
    money_label.pack_forget()


root = tk.Tk()
root.title("Inventory")
root.geometry("650x400")


menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

tk.Button(menu_frame, text="Open Inventory", command=open_inventory).pack(side="left", padx=5)
tk.Button(menu_frame, text="Close Inventory", command=close_inventory).pack(side="left", padx=5)


inventory_frame = tk.Frame(root)

tk.Label(inventory_frame, text="Inventory").pack()

listbox = tk.Listbox(inventory_frame, width=25, height=15)
listbox.pack()

tk.Button(inventory_frame, text="Equip", command=equip_item).pack(fill="x")
tk.Button(inventory_frame, text="Remove", command=remove_item).pack(fill="x")


shop_frame = tk.Frame(root)

tk.Label(shop_frame, text="Shop").pack()

shop_listbox = tk.Listbox(shop_frame, width=25, height=15)
shop_listbox.pack()

for item in SHOP:
    shop_listbox.insert(tk.END, item)

tk.Button(shop_frame, text="Buy", command=buy_item).pack(fill="x")


money_label = tk.Label(root, text=f"Money: {money}$", font=("Arial", 14))


close_inventory()

root.mainloop()

