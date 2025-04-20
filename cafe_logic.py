"""
Core business logic for Cafe Management System
This module separates the business logic from the Streamlit UI
"""
import datetime
import random

class CafeManager:
    def __init__(self):
        # Menu prices
        self.prices = {
            # Drinks
            'latte': 50,
            'irish_coffee': 100,
            'cold_coffee': 150,
            'orange_squash': 200,
            'mango_squash': 250,
            'fruit_juice': 300,
            'cold_drink': 350,
            'virgin_mojito': 400,
            
            # Cakes
            'dry_cake': 50,
            'chocolate_cake': 100,
            'butterscotch_cake': 150,
            'blackforest_cake': 200,
            'redvelvet_cake': 250,
            'trio_cake': 300,
            'dryfruit_cake': 350,
            'freshfruit_cake': 400
        }
        
        # Fixed charges
        self.service_charge = 100
        self.tax_rate = 0.15  # 15%
        
        # Initialize order
        self.reset_order()
    
    def reset_order(self):
        """Reset the current order to empty state"""
        self.order = {item: 0 for item in self.prices}
        self.costs = {
            'drinks_cost': 0,
            'cakes_cost': 0,
            'service_charge': self.service_charge,
            'tax': 0,
            'subtotal': 0,
            'total': 0
        }
        self.receipt_text = ""
    
    def update_item_quantity(self, item_name, quantity):
        """Update the quantity of a specific item in the order"""
        if item_name in self.order:
            self.order[item_name] = quantity
            return True
        return False
    
    def get_item_price(self, item_name):
        """Get the price of a specific item"""
        return self.prices.get(item_name, 0)
    
    def calculate_costs(self):
        """Calculate all costs based on current order"""
        # Separate drinks and cakes
        drinks = ['latte', 'irish_coffee', 'cold_coffee', 'orange_squash', 
                  'mango_squash', 'fruit_juice', 'cold_drink', 'virgin_mojito']
        
        # Calculate drinks cost
        drinks_cost = sum(self.order[item] * self.prices[item] for item in drinks)
        
        # Calculate cakes cost (all items that are not drinks)
        cakes = [item for item in self.order if item not in drinks]
        cakes_cost = sum(self.order[item] * self.prices[item] for item in cakes)
        
        # Calculate subtotal
        subtotal = drinks_cost + cakes_cost + self.service_charge
        
        # Calculate tax
        tax = subtotal * self.tax_rate
        
        # Calculate total
        total = subtotal + tax
        
        # Update costs dictionary
        self.costs['drinks_cost'] = drinks_cost
        self.costs['cakes_cost'] = cakes_cost
        self.costs['service_charge'] = self.service_charge
        self.costs['subtotal'] = subtotal
        self.costs['tax'] = tax
        self.costs['total'] = total
        
        return self.costs
    
    def generate_receipt(self):
        """Generate a formatted receipt for the current order"""
        # Make sure costs are up-to-date
        self.calculate_costs()
        
        # Current date and reference number
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        ref_number = random.randint(10908, 500876)
        
        # Start building receipt
        receipt = f"""
Cafe Management System - Receipt
Date: {date}
Reference: {ref_number}

Items                        Quantity        Price
--------------------------------------------------
"""
        
        # Add ordered items to receipt
        for item, quantity in self.order.items():
            if quantity > 0:
                price = self.prices[item]
                total_price = quantity * price
                # Format item name with proper spacing
                formatted_item = f"{item.replace('_', ' ').title():<28}"
                receipt += f"{formatted_item}{quantity:<16}Rs. {total_price}\n"
        
        # Add summary to receipt
        receipt += f"""
--------------------------------------------------
Cost of Drinks:                     Rs. {self.costs['drinks_cost']:.2f}
Cost of Cakes:                      Rs. {self.costs['cakes_cost']:.2f}
Service Charge:                     Rs. {self.costs['service_charge']:.2f}
--------------------------------------------------
Subtotal:                           Rs. {self.costs['subtotal']:.2f}
Tax (15%):                          Rs. {self.costs['tax']:.2f}
--------------------------------------------------
Total:                              Rs. {self.costs['total']:.2f}
--------------------------------------------------

Thank you for visiting our cafe!
"""
        
        self.receipt_text = receipt
        return receipt
