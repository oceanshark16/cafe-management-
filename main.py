import streamlit as st
import random
import time
import datetime

def main():
    # Set page configuration
    st.set_page_config(page_title="Cafe Management System", layout="wide")

    # Title
    st.title("Cafe Management System")

    # Initialize session state for storing variables
    if 'items' not in st.session_state:
        st.session_state.items = {
            # Drinks
            'latte': 0,
            'irish_coffee': 0,
            'cold_coffee': 0,
            'orange_squash': 0,
            'mango_squash': 0,
            'fruit_juice': 0,
            'cold_drink': 0,
            'virgin_mojito': 0,
            # Cakes
            'dry_cake': 0,
            'choclate_cake': 0,
            'butterscoth_cake': 0,
            'blackforest_cake': 0,
            'redvelvet_cake': 0,
            'trio_cake': 0,
            'dryfruit_cake': 0,
            'freshfruit_cake': 0
        }
    
    if 'costs' not in st.session_state:
        st.session_state.costs = {
            'drinks_cost': 0,
            'cakes_cost': 0,
            'service_charge': 100,
            'tax': 0,
            'subtotal': 0,
            'total': 0
        }

    if 'date' not in st.session_state:
        st.session_state.date = datetime.datetime.now().strftime("%d/%m/%Y")

    # Create two columns for drinks and cakes
    col1, col2 = st.columns(2)

    # Drinks section
    with col1:
        st.subheader("Drinks")
        
        st.session_state.items['latte'] = st.number_input("Latte (Rs. 50)", min_value=0, step=1, value=st.session_state.items['latte'])
        st.session_state.items['irish_coffee'] = st.number_input("Irish Coffee (Rs. 100)", min_value=0, step=1, value=st.session_state.items['irish_coffee'])
        st.session_state.items['cold_coffee'] = st.number_input("Cold Coffee (Rs. 150)", min_value=0, step=1, value=st.session_state.items['cold_coffee'])
        st.session_state.items['orange_squash'] = st.number_input("Orange Squash (Rs. 200)", min_value=0, step=1, value=st.session_state.items['orange_squash'])
        st.session_state.items['mango_squash'] = st.number_input("Mango Squash (Rs. 250)", min_value=0, step=1, value=st.session_state.items['mango_squash'])
        st.session_state.items['fruit_juice'] = st.number_input("Fruit Juice (Rs. 300)", min_value=0, step=1, value=st.session_state.items['fruit_juice'])
        st.session_state.items['cold_drink'] = st.number_input("Cold Drink (Rs. 350)", min_value=0, step=1, value=st.session_state.items['cold_drink'])
        st.session_state.items['virgin_mojito'] = st.number_input("Virgin Mojito (Rs. 400)", min_value=0, step=1, value=st.session_state.items['virgin_mojito'])

    # Cakes section
    with col2:
        st.subheader("Cakes")
        
        st.session_state.items['dry_cake'] = st.number_input("Dry Cake (Rs. 50)", min_value=0, step=1, value=st.session_state.items['dry_cake'])
        st.session_state.items['choclate_cake'] = st.number_input("Chocolate Cake (Rs. 100)", min_value=0, step=1, value=st.session_state.items['choclate_cake'])
        st.session_state.items['butterscoth_cake'] = st.number_input("Butterscotch Cake (Rs. 150)", min_value=0, step=1, value=st.session_state.items['butterscoth_cake'])
        st.session_state.items['blackforest_cake'] = st.number_input("Black Forest Cake (Rs. 200)", min_value=0, step=1, value=st.session_state.items['blackforest_cake'])
        st.session_state.items['redvelvet_cake'] = st.number_input("Red Velvet Cake (Rs. 250)", min_value=0, step=1, value=st.session_state.items['redvelvet_cake'])
        st.session_state.items['trio_cake'] = st.number_input("Trio Cake (Rs. 300)", min_value=0, step=1, value=st.session_state.items['trio_cake'])
        st.session_state.items['dryfruit_cake'] = st.number_input("Dry Fruit Cake (Rs. 350)", min_value=0, step=1, value=st.session_state.items['dryfruit_cake'])
        st.session_state.items['freshfruit_cake'] = st.number_input("Fresh Fruit Cake (Rs. 400)", min_value=0, step=1, value=st.session_state.items['freshfruit_cake'])

    # Buttons for actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Calculate Total"):
            calculate_cost()
    
    with col2:
        if st.button("Generate Receipt"):
            generate_receipt()
    
    with col3:
        if st.button("Reset"):
            reset_all()

    # Display costs
    st.subheader("Bill Details")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text(f"Cost of Drinks: Rs. {st.session_state.costs['drinks_cost']:.2f}")
        st.text(f"Cost of Cakes: Rs. {st.session_state.costs['cakes_cost']:.2f}")
        st.text(f"Service Charge: Rs. {st.session_state.costs['service_charge']:.2f}")
    
    with col2:
        st.text(f"Tax (15%): Rs. {st.session_state.costs['tax']:.2f}")
        st.text(f"Subtotal: Rs. {st.session_state.costs['subtotal']:.2f}")
        st.text(f"Total Cost: Rs. {st.session_state.costs['total']:.2f}")

    # Receipt area
    st.subheader("Receipt")
    receipt_placeholder = st.empty()
    
    if 'receipt' in st.session_state:
        receipt_placeholder.text_area("", st.session_state.receipt, height=400)

def calculate_cost():
    # Calculate costs of drinks
    drinks_cost = (
        st.session_state.items['latte'] * 50 +
        st.session_state.items['irish_coffee'] * 100 +
        st.session_state.items['cold_coffee'] * 150 +
        st.session_state.items['orange_squash'] * 200 +
        st.session_state.items['mango_squash'] * 250 +
        st.session_state.items['fruit_juice'] * 300 +
        st.session_state.items['cold_drink'] * 350 +
        st.session_state.items['virgin_mojito'] * 400
    )
    
    # Calculate costs of cakes
    cakes_cost = (
        st.session_state.items['dry_cake'] * 50 +
        st.session_state.items['choclate_cake'] * 100 +
        st.session_state.items['butterscoth_cake'] * 150 +
        st.session_state.items['blackforest_cake'] * 200 +
        st.session_state.items['redvelvet_cake'] * 250 +
        st.session_state.items['trio_cake'] * 300 +
        st.session_state.items['dryfruit_cake'] * 350 +
        st.session_state.items['freshfruit_cake'] * 400
    )
    
    # Service charge is fixed at Rs. 100
    service_charge = 100
    
    # Calculate subtotal
    subtotal = drinks_cost + cakes_cost + service_charge
    
    # Calculate tax (15% of subtotal)
    tax = subtotal * 0.15
    
    # Calculate total
    total = subtotal + tax
    
    # Update session state
    st.session_state.costs['drinks_cost'] = drinks_cost
    st.session_state.costs['cakes_cost'] = cakes_cost
    st.session_state.costs['service_charge'] = service_charge
    st.session_state.costs['subtotal'] = subtotal
    st.session_state.costs['tax'] = tax
    st.session_state.costs['total'] = total

def generate_receipt():
    # Calculate costs first
    calculate_cost()
    
    # Generate receipt reference number
    ref_number = random.randint(10908, 500876)
    
    # Create receipt content
    receipt = f"""
    Cafe Management System - Receipt
    Date: {st.session_state.date}
    Reference: {ref_number}
    
    Items                        Quantity        Price
    --------------------------------------------------
    """
    
    # Add drinks to receipt
    if st.session_state.items['latte'] > 0:
        receipt += f"Latte                        {st.session_state.items['latte']}              Rs. {st.session_state.items['latte'] * 50}\n"
    if st.session_state.items['irish_coffee'] > 0:
        receipt += f"Irish Coffee                 {st.session_state.items['irish_coffee']}              Rs. {st.session_state.items['irish_coffee'] * 100}\n"
    if st.session_state.items['cold_coffee'] > 0:
        receipt += f"Cold Coffee                  {st.session_state.items['cold_coffee']}              Rs. {st.session_state.items['cold_coffee'] * 150}\n"
    if st.session_state.items['orange_squash'] > 0:
        receipt += f"Orange Squash                {st.session_state.items['orange_squash']}              Rs. {st.session_state.items['orange_squash'] * 200}\n"
    if st.session_state.items['mango_squash'] > 0:
        receipt += f"Mango Squash                 {st.session_state.items['mango_squash']}              Rs. {st.session_state.items['mango_squash'] * 250}\n"
    if st.session_state.items['fruit_juice'] > 0:
        receipt += f"Fruit Juice                  {st.session_state.items['fruit_juice']}              Rs. {st.session_state.items['fruit_juice'] * 300}\n"
    if st.session_state.items['cold_drink'] > 0:
        receipt += f"Cold Drink                   {st.session_state.items['cold_drink']}              Rs. {st.session_state.items['cold_drink'] * 350}\n"
    if st.session_state.items['virgin_mojito'] > 0:
        receipt += f"Virgin Mojito                {st.session_state.items['virgin_mojito']}              Rs. {st.session_state.items['virgin_mojito'] * 400}\n"
    
    # Add cakes to receipt
    if st.session_state.items['dry_cake'] > 0:
        receipt += f"Dry Cake                     {st.session_state.items['dry_cake']}              Rs. {st.session_state.items['dry_cake'] * 50}\n"
    if st.session_state.items['choclate_cake'] > 0:
        receipt += f"Chocolate Cake               {st.session_state.items['choclate_cake']}              Rs. {st.session_state.items['choclate_cake'] * 100}\n"
    if st.session_state.items['butterscoth_cake'] > 0:
        receipt += f"Butterscotch Cake            {st.session_state.items['butterscoth_cake']}              Rs. {st.session_state.items['butterscoth_cake'] * 150}\n"
    if st.session_state.items['blackforest_cake'] > 0:
        receipt += f"Black Forest Cake            {st.session_state.items['blackforest_cake']}              Rs. {st.session_state.items['blackforest_cake'] * 200}\n"
    if st.session_state.items['redvelvet_cake'] > 0:
        receipt += f"Red Velvet Cake              {st.session_state.items['redvelvet_cake']}              Rs. {st.session_state.items['redvelvet_cake'] * 250}\n"
    if st.session_state.items['trio_cake'] > 0:
        receipt += f"Trio Cake                    {st.session_state.items['trio_cake']}              Rs. {st.session_state.items['trio_cake'] * 300}\n"
    if st.session_state.items['dryfruit_cake'] > 0:
        receipt += f"Dry Fruit Cake               {st.session_state.items['dryfruit_cake']}              Rs. {st.session_state.items['dryfruit_cake'] * 350}\n"
    if st.session_state.items['freshfruit_cake'] > 0:
        receipt += f"Fresh Fruit Cake             {st.session_state.items['freshfruit_cake']}              Rs. {st.session_state.items['freshfruit_cake'] * 400}\n"
    
    # Add subtotal, tax, and total to receipt
    receipt += f"""
    --------------------------------------------------
    Cost of Drinks:                     Rs. {st.session_state.costs['drinks_cost']:.2f}
    Cost of Cakes:                      Rs. {st.session_state.costs['cakes_cost']:.2f}
    Service Charge:                     Rs. {st.session_state.costs['service_charge']:.2f}
    --------------------------------------------------
    Subtotal:                           Rs. {st.session_state.costs['subtotal']:.2f}
    Tax (15%):                          Rs. {st.session_state.costs['tax']:.2f}
    --------------------------------------------------
    Total:                              Rs. {st.session_state.costs['total']:.2f}
    --------------------------------------------------
    
    Thank you for visiting our cafe!
    """
    
    # Store receipt in session state
    st.session_state.receipt = receipt

def reset_all():
    # Reset all items to 0
    for item in st.session_state.items:
        st.session_state.items[item] = 0
    
    # Reset all costs to 0, except service charge which is fixed at 100
    st.session_state.costs = {
        'drinks_cost': 0,
        'cakes_cost': 0,
        'service_charge': 100,
        'tax': 0,
        'subtotal': 0,
        'total': 0
    }
    
    # Clear receipt
    if 'receipt' in st.session_state:
        del st.session_state.receipt

if __name__ == "__main__":
    main()
