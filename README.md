# 🛒 E-Commerce Price Comparison 

## 📌 Overview
This Python-based web scraping tool allows users to compare product prices from Amazon and Flipkart. It fetches product names and prices from both platforms and displays them in a formatted table for easy comparison.

## 🚀 Features
- Scrapes product names and prices from **Amazon** and **Flipkart**
- Displays results in a well-structured **table format**
- Uses **random user-agents** to avoid detection
- Handles multiple product searches dynamically

## 🔧 Installation

### Prerequisites
Make sure you have **Python 3.6+** installed on your system.

### 📥 Install Required Packages
Run the following command to install the dependencies:
```sh
pip install requests beautifulsoup4 prettytable
```

## ▶️ Usage

1. Clone or download the repository.
2. Navigate to the project folder.
3. Run the script:
   ```sh
   python main.py
   ```
4. Enter the product name when prompted.
5. View the price comparison table in the terminal.

## 📝 Example
**Input:**
```
Enter Product name to search for: iPhone 15
```

**Output:**
```
amazon scraping status: 200
flipkart scraping status: 200

+------+-----------------------+------------+
| S.NO | amazon Product Name   | Price (INR)|
+------+-----------------------+------------+
| 1    | Apple iPhone 15 ...   | ₹79,999    |
| 2    | Apple iPhone 15 Pro.. | ₹1,29,999  |
+------+-----------------------+------------+

+------+-----------------------+------------+
| S.NO | flipkart Product Name | Price (INR)|
+------+-----------------------+------------+
| 1    | Apple iPhone 15 (Blue)| ₹78,499    |
| 2    | Apple iPhone 15 Pro.. | ₹1,28,999  |
+------+-----------------------+------------+
```

## 📌 Notes
- This script scrapes publicly available data and is intended for **educational purposes**.
- **Amazon** and **Flipkart** frequently update their website structure, which might require modifying the scraping logic.
