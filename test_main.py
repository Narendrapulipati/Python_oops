import sys
#parent class
class shop:
    product = "laptop"  # Class variable

    def __init__(self, brand, price,warranty, color,ram):
        self.brand = brand
        self.price = price
        self.warranty=warranty
        self.color=color
        self.ram=ram

    def show_details(self):
        print(f"\nProduct Details:")
        print(f"Product: {shop.product}")  # calling class variable
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")
        print(f"warranty: ₹{self.warranty}")
        print(f"color: ₹{self.color}")
        print(f"ram: ₹{self.ram}")

#inheritence using
class Customer(shop):
    def __init__(self):
        brand = input("Enter brand: ")
        brands = ['HP', 'Lenovo', 'Dell']

        if brand not in brands:
            print("Enter Laptop is Not Available")
            sys.exit()  # Stop program if brand not found

        print("Laptop is available")

        price = input("Enter price range you want (₹): ")
        warranty = input("Enter warranty detail in years : ")
        color = input("Enter color : ")
        ram = input("Enter ram size required: ")
        try:
            price = int(price)
        except ValueError:
            print("Invalid price, setting price to 0.")
            price = 0


        shop.__init__(self, brand, price, warranty,color,ram)  # Call parent constructor

my_product = Customer()
my_product.show_details()
