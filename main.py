from pip._vendor import requests 
from web_app import Flask, render_template, request

#### Setting up the basic logic of the app #####
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

    @staticmethod
    def create_or_edit_profile():
        print("Enter User Profile: ")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        hypertension_input = input("Do you have hypertension? (yes/no): ").strip().lower()
        has_hypertension = hypertension_input in ['yes', 'y']

        profile = {
            'name': name,
            'age' : age,
            'gender': gender,
            'hypertension': has_hypertension
        }

        print("\nProfile created for " + name + ". \nAge: " + str(age) + " \nGender: " + gender + " \nHypertension status: " + ("Yes" if has_hypertension else "No"))
        return profile

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

class RecommendationModel:
    def evaluate_food_item(self, user_profile, food_nutriments, display_sodium=True):
        has_hypertension = user_profile.get("hypertension", False)
        explanation = []
        recommended = True

        sodium_mg = food_nutriments.get('sodium_serving', 0) * 1000  # convert g to mg

        # Check for hypertension
        if display_sodium:
            print("\nSodium per serving: " + str(round(sodium_mg, 2)) + " mg")
        
        if has_hypertension and sodium_mg > 500:
            recommended = False
            explanation.append("⚠️  Warning: High sodium content. Not recommended for those with hypertension.")
        elif sodium_mg == 0:
            print("\nSodium per serving data not available for this product.")
         
        if recommended:
            return {
                "recommended": True,
                "message": "Great choice! You can eat this product. It's aligned with your health needs."
            }
        else:
            return {
                "recommended": False,
                "message": " and".join(explanation) + "." + "It would be best to find an alternative option becaue of the high sodium content of this product."
            }

##### Main FoodFactsBarcode functionality ####
def main():
    user_profile = {}

    while True:
        choice = UserInterface.main_menu()

        if choice == 1:
            user_profile = UserInterface.create_or_edit_profile()

        elif choice == 2:
            barcode = input("Enter a product barcode: ")
            product_info = get_product_info(barcode)

            if isinstance(product_info, dict):
                print(f"\nProduct: {product_info['product_name']}")
                print(f"Ingredients: {product_info['ingredients_text']}")
                has_hypertension = user_profile.get('hypertension', False)
                recommendation_model= RecommendationModel()
                evaluation = recommendation_model.evaluate_food_item(user_profile,product_info['nutriments'])
                print(evaluation['message'])
            else:
                print(product_info)

        elif choice == 3:
            print("Previously scanned products feature is not yet implemented.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")

if __name__ == '__main__':
    main()
