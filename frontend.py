import streamlit as st
import requests

# Define backend URL
backend_url = "http://localhost:5000"

# Fetch products from backend
def fetch_products():
    response = requests.get(f"{backend_url}/api/products")
    return response.json()

# Fetch analysis from backend
def fetch_analysis():
    response = requests.get(f"{backend_url}/api/analysis")
    return response.json()

# Place an order
def place_order(cart):
    total = sum(item['price'] for item in cart)
    order = {'items': cart, 'total': total}
    response = requests.post(f"{backend_url}/api/orders", json=order)
    return response.status_code == 201

# UI Setup
st.title("Supermarket")

# Page Navigation
page = st.sidebar.selectbox("Select a page", ["Home", "Cart", "Analysis"])

if page == "Home":
    st.header("Products")
    products = fetch_products()
    cart = st.session_state.get('cart', [])

    for product in products:
        st.subheader(product['name'])
        st.text(f"Category: {product['category']}")
        st.text(f"Price: ${product['price']}")
        if st.button(f"Add to Cart", key=product['id']):
            cart.append(product)
            st.session_state['cart'] = cart
            st.success(f"Added {product['name']} to cart!")

elif page == "Cart":
    st.header("Cart")
    cart = st.session_state.get('cart', [])
    if cart:
        for idx, item in enumerate(cart):
            st.text(f"{item['name']} - ${item['price']}")
            if st.button(f"Remove", key=f"remove_{idx}"):
                cart.pop(idx)
                st.session_state['cart'] = cart
                st.success(f"Removed {item['name']} from cart!")
        if st.button("Place Order"):
            if place_order(cart):
                st.success("Order placed successfully!")
                st.session_state['cart'] = []
            else:
                st.error("Failed to place order")
    else:
        st.info("Your cart is empty")

elif page == "Analysis":
    st.header("Business Analysis")
    analysis = fetch_analysis()
    st.text(f"Total Revenue: ${analysis['totalRevenue']}")
    st.text(f"Total Orders: {analysis['totalOrders']}")
    st.text(f"Average Order Value: ${analysis['averageOrderValue']}")
    st.text(f"Highest Selling Product: {analysis['highestSellingProduct']}")
    st.text(f"Highest Profit Making Product: {analysis['highestProfitMakingProduct']}")
    st.text(f"Most Liked Product: {analysis['mostLikedProduct']}")
