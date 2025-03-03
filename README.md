# Supermarket-Billing-System
A simple **Supermarket Billing System** built using Python with Object-Oriented Programming (OOP). The system allows users to purchase multiple items, generate a bill, and save it as a JSON file.

## Features 🚀
- View available items and their prices.
- Add multiple items to the cart in a single session.
- Generate a formatted bill with GST calculations.
- Save the bill as a JSON file for record-keeping.
- Handles invalid inputs gracefully.

## Technologies Used 🛠️
- **Python** (for implementation)
- **JSON** (for saving bill data)
- **Datetime module** (for timestamps)

## Installation & Usage 💻
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/supermarket-billing.git
   cd supermarket-billing
   ```
2. **Run the script:**
   ```bash
   python supermarket_billing.py
   ```

## How It Works 🛒
1. Enter your name.
2. View available items.
3. Add multiple items to the cart by entering item names and quantities.
4. Generate the bill, view the breakdown, and save it.
5. Choose to exit the program when done.

## Example Output 📄
```
==================== Madhu Supermarket ====================
Name: John Doe            Date: 2025-03-03 14:30:15
------------------------------------------------------------
S.No  Item           Quantity   Price   
------------------------------------------------------------
1     Rice           2          Rs 40  
2     Sugar          1          Rs 30  
------------------------------------------------------------
Total Amount:                 Rs 70  
GST (5%):                     Rs 3.5  
Final Amount:                 Rs 73.5  
============================================================
Thanks for shopping with us!
============================================================
```

## Future Enhancements 🚀
- Add discount features.
- Implement a GUI version.
- Store past bills in a database.

## License 📜
This project is open-source and available under the **MIT License**.

---
Made with ❤️ by Madhu Komire

