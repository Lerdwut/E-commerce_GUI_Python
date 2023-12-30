import os
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

def signup(user_db, username, password):
    if user_db.find_user(username) is not None:
        return "ชื่อผู้ใช้นี้มีอยู่แล้ว"
    
    new_user = User(username, password)
    user_db.add_user(new_user)
    return "ลงทะเบียนสำเร็จ"

def signin(user_db, username, password):
    while True:
        user = user_db.find_user(username)
        if user is None:
            return "ไม่พบชื่อผู้ใช้"

        if user.password == password:
            return "เข้าสู่ระบบสำเร็จ"
        else:
            print("รหัสผ่านไม่ถูกต้อง")
            password = input("กรุณาใส่รหัสผ่านใหม่: ")

user_db = UserDatabase()

print("สมัครสมาชิค")
user = input("ใส่ชื่อผู้ใช้: ")
password = input("ใส่รหัสผ่าน: ")
result = signup(user_db, user, password)
print(result)

print("เข้าสู้ระบบ")
user = input("ใส่ชื่อผู้ใช้: ")
password = input("ใส่รหัสผ่าน: ")
result = signin(user_db, user, password)
print(result)

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

products = [
    Product(1, "Iphone 15", 40000),
    Product(2, "Ryzen 9 7900x", 14550),
    Product(3, "Logitech G PRO X Superlight", 3500),
    Product(4, "Notebook Gaming", 50000),
    Product(5, "Keyboard", 1500),
]

total_price = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("รายการสินค้าในร้านค้า:")
    for product in products:
        print(f"{product.product_id}: {product.name} - ราคา {product.price} บาท")
    
    selected_product_id = int(input("เลือกหมายเลขสินค้าที่ต้องการ: "))
    selected_product = None
    
    for product in products:
        if product.product_id == selected_product_id:
            selected_product = product
            break
    
    if selected_product is not None:
        print(f"คุณเลือก: {selected_product.name} - ราคา {selected_product.price} บาท")
        total_price += selected_product.price
        print(f"ราคารวมทั้งหมด: {total_price} บาท")

    else:
        print("ไม่พบสินค้าที่คุณเลือก")
    
    choice = input("เลือก (1) เพิ่มสินค้าเพิ่ม, (2) เสร็จสิ้น: ")
    if choice == "2":
        break
    elif choice != "1":
        print("กรุณาเลือก (1) เพิ่มสินค้าเพิ่ม หรือ (2) เสร็จสิ้น")

print(f"ราคารวม: {total_price} บาท")