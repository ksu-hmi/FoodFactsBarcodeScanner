# Welcome to Thought for Food! 

Thought for Food is a Python-based tool that uses the Open Food Facts API to fetch and display food product information. The user provides a product barcode, and the application returns the product's name, ingredients, and nutritional information.

This a prototype for a tool that would identify if sodium intake exceeds the daily recommended amount for a user profile identified as having hypertension.

## Table of Contents
Our application will have the following tabs:
 - User profile set up
 - Food Scanner
 - A tool that alerts if sodium intake exceeds the daily recommended amount of 1500 mg per day.

## Features

- Nutrition recommendation tool for those diagnosed with comorbidities.
- Create user profile with the ability to select multiple comorbidities.
- Food barcode scanner.
- Generate health recommendations based on the scanned products nutrition label and the selected user profile comorbidities.

## New features added by Nathan
- Saturated Fat content per serving will now display with user input
- Daily max recommended by American Heart Association will display with user input
- Food item will be recommended or not recommended based on both sodium content and saturated fat per serving for user with hypertension

## ThoughtForFood Webflask
- Added an about page for web app
- Added a barcode scan page (functionality live!)
- Layout template
- Profile submission form
- Welcome page

### Prerequisites

Ensure you have Python 3.7 or later installed on your machine. You can check your Python version by running the following command in your command line:

```
python --version
```

Also, this project uses the `requests` library to handle HTTP requests. If you haven't installed it yet, you can do so with the following command:

```
pip install requests
```

### Installation

1. Clone the repository:
```
git clone https://github.com/sonnymay/FoodFactsBarcodeScanner.git
```

2. Navigate into the cloned repository:
```
cd FoodFactsBarcodeScanner
```

3. Run the Python script:
```
python main.py
```

## Usage

When you run the script, it will prompt you to input a barcode. Enter the barcode of the product you want to know more about and press Enter. The script will then display the product's name, ingredients, and nutritional information. 

Please note that the Open Food Facts database may not include all barcodes. If the script cannot find the barcode you entered, it will notify you accordingly.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/YourUsername/FoodFactsBarcodeScanner/issues). 

Nathan updated code to tell end-user if a product is recommended based on sodium content. Source used is DASH diet recommended daily limit of 2300mg/day.
Nathan updated code to allow user to state whether or not they suffer from hypertension when creating a user profile.
