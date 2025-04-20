class UserInterface:
    @staticmethod
    def main_menu():
        print("Welcome to Thought for Food!")
        print("\nMain Menu:")
        print("1. Create or Edit User Profile")
        print("2. Scan Product by Barcode")
        print("3. View Previously Scanned Products")
        print("4. Exit")

        choice = int(input("Select an option (1 - 4): "))
        return choice

import requests

def get_product_info(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        product = data.get('product')
        if product:
            return {
                'product_name': product.get('product_name'),
                'ingredients_text': product.get('ingredients_text'),
                'nutriments': product.get('nutriments'),
            }
        else:
            return "No product found for this barcode."
    else:
        return "Error fetching product data."

def main():
    barcode = input("Enter a product barcode: ")
    product_info = get_product_info(barcode)
    print(product_info)

if __name__ == '__main__':
    main()
