
import re
product_list = []


def code_checker(code):
    if re.match(r"^[a-zA-Z0-9\s]{3,50}$", code):
        return True
    else:
        print("Error : code is not valid")
        return False


def name_checker(name):
    if re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return True
    else:
        print("Error : Name is not valid")
        return False


def brand_checker(brand):
    if re.match(r"^[a-zA-Z0-9]{3,50}$", brand):
        return True
    else:
        print("Error : brand is not valid")
        return False


def price_checker(price):
    if 1000 <= price <= 2000:
        return True
    else:
        print("Error : price is not ok !!!")
        return False


def show_menu():
    print("1)Add phone")
    print("2)find by code")
    print("3)find by price")
    print("4)show list")
    print("0)Exit")
    option = int(input("Enter Option : "))
    print("-" * 50)
    return option


def get_data():
    name = input("enter Name : ")
    code = input("enter code : ")
    brand = input("enter brand")
    price = int(input("enter price : "))

    if (name_checker(name) and price_checker(price) and code_checker(code) and brand_checker(brand)):
        product = {"name": name, "code": code, "price": price, "brand": brand}
        product_list.append(product)
        print("Info : product Saved")


def show_list():
    for product in product_list:
        print(product["name"], product["code"], product["price"], product["brand"])

