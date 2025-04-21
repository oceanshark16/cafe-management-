import streamlit as st
import random
import datetime

# Page configuration
st.set_page_config(page_title="Cafe VIT_SOHAM", layout="wide")

# Title
st.title("Cafe Management Systemssss")

# Initialize menu and prices
MENU_PRICES = {
    # Drinks
    "Latte": 50,
    "Irish Coffee": 100,
    "Cold Coffee": 150,
    "Orange Squash": 200,
    "Mango Squash": 250,
    "Fruit Juice": 300,
    "Cold Drink": 350,
    "Virgin Mojito": 400,
    # Cakes
    "Dry Cake": 50,
    "Chocolate Cake": 100,
    "Butterscotch Cake": 150,
    "Black Forest Cake": 200,
    "Red Velvet Cake": 250,
    "Trio Cake": 300,
    "Dry Fruit Cake": 350,
    "Fresh Fruit Cake": 400,
}

# Initialize session state
if "order_quantities" not in st.session_state:
    st.session_state.order_quantities = {item: 0 for item in MENU_PRICES}
if "receipt" not in st.session_state:
    st.session_state.receipt = ""
if "totals" not in st.session_state:
    st.session_state.totals = {
        "drinks": 0,
        "cakes": 0,
        "service_charge": 100,
        "subtotal": 0,
        "tax": 0,
        "total": 0
    }

# Split columns
col1, col2 = st.columns(2)

# Drinks input
with col1:
    st.subheader("Drinks")
    for item in list(MENU_PRICES.keys())[:8]:
        st.session_state.order_quantities[item] = st.number_input(
            f"{item} (Rs. {MENU_PRICES[item]})",
            min_value=0,
            step=1,
            value=st.session_state.order_quantities[item]
        )

# Cakes input
with col2:
    st.subheader("Cakes")
    for item in list(MENU_PRICES.keys())[8:]:
        st.session_state.order_quantities[item] = st.number_input(
            f"{item} (Rs. {MENU_PRICES[item]})",
            min_value=0,
            step=1,
            value=st.session_state.order_quantities[item]
        )

# Calculate total
def calculate_total():
    drinks_total = sum(
        qty * MENU_PRICES[item] for item, qty in st.session_state.order_quantities.items()
        if item in list(MENU_PRICES.keys())[:8]
    )
    cakes_total = sum(
        qty * MENU_PRICES[item] for item, qty in st.session_state.order_quantities.items()
        if item in list(MENU_PRICES.keys())[8:]
    )
    service_charge = 100
    subtotal = drinks_total + cakes_total + service_charge
    tax = subtotal * 0.15
    total = subtotal + tax
    st.session_state.totals = {
        "drinks": drinks_total,
        "cakes": cakes_total,
        "service_charge": service_charge,
        "subtotal": subtotal,
        "tax": tax,
        "total": total
    }

# Generate receipt
def generate_receipt():
    calculate_total()
    ref_no = random.randint(10000, 99999)
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    receipt_lines = [
        "Cafe Management System - Receipt",
        f"Date: {date}",
        f"Reference No: {ref_no}",
        "-" * 40,
        "Item\t\tQty\tPrice",
        "-" * 40,
    ]
    for item, qty in st.session_state.order_quantities.items():
        if qty > 0:
            line = f"{item:20s} {qty:<3d} Rs. {qty * MENU_PRICES[item]:.2f}"
            receipt_lines.append(line)

    totals = st.session_state.totals
    receipt_lines += [
        "-" * 40,
        f"Drinks Cost:\t\tRs. {totals['drinks']:.2f}",
        f"Cakes Cost:\t\tRs. {totals['cakes']:.2f}",
        f"Service Charge:\t\tRs. {totals['service_charge']:.2f}",
        f"Subtotal:\t\tRs. {totals['subtotal']:.2f}",
        f"Tax (15%):\t\tRs. {totals['tax']:.2f}",
        f"Total:\t\tRs. {totals['total']:.2f}",
        "-" * 40,
        "Thank you for visiting our Cafe!"
    ]

    st.session_state.receipt = "\n".join(receipt_lines)

# Reset app
def reset_app():
    st.session_state.order_quantities = {item: 0 for item in MENU_PRICES}
    st.session_state.receipt = ""
    st.session_state.totals = {
        "drinks": 0, "cakes": 0, "service_charge": 100,
        "subtotal": 0, "tax": 0, "total": 0
    }

# Buttons
col1, col2, col3 = st.columns(3)
if col1.button("Calculate Total"):
    calculate_total()
if col2.button("Generate Receipt"):
    generate_receipt()
if col3.button("Reset"):
    reset_app()

# Show totals
st.subheader("Billing Summary")
totals = st.session_state.totals
st.text(f"Drinks Total: Rs. {totals['drinks']:.2f}")
st.text(f"Cakes Total: Rs. {totals['cakes']:.2f}")
st.text(f"Service Charge: Rs. {totals['service_charge']:.2f}")
st.text(f"Tax (15%): Rs. {totals['tax']:.2f}")
st.text(f"Total Payable: Rs. {totals['total']:.2f}")

# Show receipt
if st.session_state.receipt:
    st.subheader("Receipt")
    st.text_area("Receipt", value=st.session_state.receipt, height=400)
