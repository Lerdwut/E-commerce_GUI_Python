import tkinter as tk
from tkinter import ttk

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserDatabase:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, username):
        return next((user for user in self.users if user.username == username), None)

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.items)

class Order:
    def __init__(self, order_id, customer, products, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.status = status

    def calculate_total(self):
        return sum(product.price for product in self.products)

class OnlineStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Store")
        
        self.user_db = UserDatabase()
        self.logged_in_user = None  # เพิ่มตัวแปรเพื่อเก็บผู้ใช้ที่เข้าสู่ระบบ
        self.products = [
            Product(1, "iPhone 12", 999),
            Product(2, "Samsung Galaxy S21", 899),
            Product(3, "Google Pixel 5", 799),
        ]
        self.shopping_cart = ShoppingCart()
        self.orders = []

        self.create_signup_frame()
        self.create_product_list()
        self.create_shopping_cart()
        self.create_login_frame()  # เพิ่มการสร้างส่วนของ Login
        
    def create_signup_frame(self):
        signup_frame = ttk.LabelFrame(self.root, text="Sign Up")
        signup_frame.grid(row=0, column=0, padx=10, pady=10)
        
        username_label = ttk.Label(signup_frame, text="Username:")
        username_label.grid(row=0, column=0, sticky="w")
        
        self.username_entry = ttk.Entry(signup_frame)
        self.username_entry.grid(row=0, column=1)
        
        password_label = ttk.Label(signup_frame, text="Password:")
        password_label.grid(row=1, column=0, sticky="w")
        
        self.password_entry = ttk.Entry(signup_frame, show="*")
        self.password_entry.grid(row=1, column=1)
        
        signup_button = ttk.Button(signup_frame, text="Sign Up", command=self.signup)
        signup_button.grid(row=2, columnspan=2)

    def create_login_frame(self):
        login_frame = ttk.LabelFrame(self.root, text="Login/Logout")
        login_frame.grid(row=0, column=3, padx=10, pady=10)
        
        self.login_button = ttk.Button(login_frame, text="Login", command=self.login)
        self.login_button.grid(row=0, column=0)
        
        self.logout_button = ttk.Button(login_frame, text="Logout", command=self.logout, state=tk.DISABLED)
        self.logout_button.grid(row=0, column=1)

    def create_product_list(self):
        product_frame = ttk.LabelFrame(self.root, text="Product List")
        product_frame.grid(row=0, column=1, padx=10, pady=10)
        
        for product in self.products:
            product_label = ttk.Label(product_frame, text=product.name)
            product_label.grid(sticky="w")
            
            add_button = ttk.Button(product_frame, text="Add to Cart", command=lambda p=product: self.add_to_cart(p))
            add_button.grid(sticky="e")

    def create_shopping_cart(self):
        cart_frame = ttk.LabelFrame(self.root, text="Shopping Cart")
        cart_frame.grid(row=0, column=2, padx=10, pady=10)
        
        self.cart_listbox = tk.Listbox(cart_frame, width=40, height=10)
        self.cart_listbox.grid(row=0, column=0, padx=10, pady=10)
        
        total_label = ttk.Label(cart_frame, text="Total:")
        total_label.grid(row=1, column=0, sticky="w")
        
        self.total_value_label = ttk.Label(cart_frame, text="")
        self.total_value_label.grid(row=1, column=0, sticky="e")
        
        remove_button = ttk.Button(cart_frame, text="Remove", command=self.remove_from_cart)
        remove_button.grid(row=2, column=0, padx=10, pady=5)

        buy_button = ttk.Button(cart_frame, text="Buy", command=self.buy_items)
        buy_button.grid(row=3, column=0, padx=10, pady=5)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            if not self.user_db.find_user(username):
                user = User(username, password)
                self.user_db.add_user(user)
                self.show_message("Sign up successful!")
            else:
                self.show_message("Username already exists.")
        else:
            self.show_message("Please enter both username and password.")

    def signin(self):
        username = self.signin_username_entry.get()
        password = self.signin_password_entry.get()

        if username and password:
            user = self.user_db.find_user(username)
            if user and user.password == password:
                self.logged_in_user = user
                self.show_message("Sign in successful!")
                self.login_button.config(state=tk.DISABLED)
                self.logout_button.config(state=tk.NORMAL)
            else:
                self.show_message("Invalid username or password.")
        else:
            self.show_message("Please enter both username and password.")

    def login(self):
        signin_window = tk.Toplevel(self.root)
        signin_window.title("Sign In")

        signin_frame = ttk.Frame(signin_window)
        signin_frame.grid(row=0, column=0, padx=10, pady=10)

        username_label = ttk.Label(signin_frame, text="Username:")
        username_label.grid(row=0, column=0, sticky="w")

        self.signin_username_entry = ttk.Entry(signin_frame)
        self.signin_username_entry.grid(row=0, column=1)

        password_label = ttk.Label(signin_frame, text="Password:")
        password_label.grid(row=1, column=0, sticky="w")

        self.signin_password_entry = ttk.Entry(signin_frame, show="*")
        self.signin_password_entry.grid(row=1, column=1)

        signin_button = ttk.Button(signin_frame, text="Sign In", command=self.signin)
        signin_button.grid(row=2, columnspan=2)

    def logout(self):
        self.logged_in_user = None
        self.show_message("Logout successful!")
        self.login_button.config(state=tk.NORMAL)
        self.logout_button.config(state=tk.DISABLED)

    def add_to_cart(self, product):
        if self.logged_in_user:
            self.shopping_cart.add_item(product)
            self.cart_listbox.insert(tk.END, product.name)
            total = self.shopping_cart.calculate_total()
            self.total_value_label.config(text=f"${total:.2f}")
        else:
            self.show_message("Please log in to add items to the cart.")

    def remove_from_cart(self):
        selected_index = self.cart_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            product_name = self.cart_listbox.get(index)
            product = next((p for p in self.products if p.name == product_name), None)
            if product:
                self.shopping_cart.remove_item(product)
                self.cart_listbox.delete(index)
                total = self.shopping_cart.calculate_total()
                self.total_value_label.config(text=f"${total:.2f}")

    def buy_items(self):
        if self.logged_in_user and self.shopping_cart.items:
            total = self.shopping_cart.calculate_total()
            confirmation_message = f"การสั่งซื้อสำเร็จ!\nราคารวม: ${total:.2f}"
            self.show_message(confirmation_message)

            # สร้างรายการสั่งซื้อใหม่
            order = Order(len(self.orders) + 1, self.logged_in_user, self.shopping_cart.items)
            self.orders.append(order)

            # ล้างตะกร้าสินค้า
            self.shopping_cart.items = []
            self.cart_listbox.delete(0, tk.END)
            self.total_value_label.config(text="$0.00")
        elif not self.logged_in_user:
            self.show_message("Please log in to place an order.")
        else:
            self.show_message("Your shopping cart is empty. Please add items before placing an order.")

    def show_message(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Message")
        
        label = ttk.Label(popup, text=message)
        label.pack(padx=20, pady=20)
        
        ok_button = ttk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(padx=20, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineStoreApp(root)
    root.mainloop()