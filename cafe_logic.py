# cafe_logic.py

def calculate_total_cost(drinks_cost, cakes_cost, service_charge, tax_percent=5):
    """
    Returns subtotal, tax, and total.
    """
    subtotal = drinks_cost + cakes_cost + service_charge
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    return round(subtotal, 2), round(tax, 2), round(total, 2)
