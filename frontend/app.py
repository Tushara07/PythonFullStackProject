import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import CustomerManager, CourierManager, ParcelManager, TrackingManager

# Initialize managers
customer_mgr = CustomerManager()
courier_mgr = CourierManager()
parcel_mgr = ParcelManager()
tracking_mgr = TrackingManager()

# ---- Page Config ----
st.set_page_config(page_title="Parcel Tracking System", layout="wide")

# ---- Session State for Navigation ----
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---- Header Navigation ----
header_cols = st.columns([1, 6, 1, 1, 1, 1])
with header_cols[0]:
    if st.button(" Home "):
        st.session_state.page = "Home"
with header_cols[2]:
    if st.button("Customers"):
        st.session_state.page = "Customers"
with header_cols[3]:
    if st.button("Couriers"):
        st.session_state.page = "Couriers"
with header_cols[4]:
    if st.button("Parcels"):
        st.session_state.page = "Parcels"
with header_cols[5]:
    if st.button("Tracking"):
        st.session_state.page = "Tracking"

st.markdown("---")

# ---- Page Background & Button Styling ----
st.markdown(
    """
    <style>
    /* Entire page background */
    .stApp {
        background-color: #D1D1EB;
    }


    /* Streamlit buttons styling */
    div.stButton > button {
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);    
        padding: 0.35em 0.75em;                        
        font-weight: 500;                              
        transition: all 0.2s ease;                     
    }

    div.stButton > button:hover {
        box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.4);
        background-color: #38506E;                     /* hover color */
        color: white;
        transform: translateY(-1px);                   /* lift on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------- Home Page ----------------
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align: center;text-shadow: 1px 1.5px 2px rgba(0,0,0,0.4);'>📦 Parcel Tracking System</h1>", unsafe_allow_html=True)
    
    st.write(" ")

    left_col, right_col = st.columns([2, 1])  # Left for operations, right for stats

    # ---------------- Left Column: Operations ----------------
    with left_col:
        st.markdown("<h3 style='text-align: left;'>Select an Operation</h3>", unsafe_allow_html=True)
        st.write(" ")  # spacing

        # Vertical buttons with spacing
        st.write(" ")  # spacing
        if st.button("👤 Customers", key="home_customers"):
            st.session_state.page = "Customers"
        st.write("Manage all customer records: Add, Update, View, Delete.")

        st.write(" ")  # spacing
        if st.button("📦 Couriers", key="home_couriers"):
            st.session_state.page = "Couriers"
        st.write("Manage courier details and assignments.")

        st.write(" ")  # spacing
        if st.button("📬 Parcels", key="home_parcels"):
            st.session_state.page = "Parcels"
        st.write("Track parcel details, weight, price, and status.")

        st.write(" ")  # spacing
        if st.button("🔎 Tracking", key="home_tracking"):
            st.session_state.page = "Tracking"
        st.write("Add and view tracking updates for parcels.")

    # ---------------- Right Column: Quick Stats ----------------
    with right_col:
        st.markdown("### Quick Stats")
        
        # Fetch data from your DatabaseManager directly
        customers_res = customer_mgr.db.get_customers()
        couriers_res = courier_mgr.db.get_couriers()
        parcels_res = parcel_mgr.db.get_parcels()

        total_customers = len(customers_res) if customers_res else 0
        total_couriers = len(couriers_res) if couriers_res else 0
        total_parcels = len(parcels_res) if parcels_res else 0
        in_transit = sum(1 for p in parcels_res if p.get("status") == "In Transit") if parcels_res else 0
        delivered = sum(1 for p in parcels_res if p.get("status") == "Delivered") if parcels_res else 0

        st.metric("Total Customers", total_customers)
        st.metric("Total Couriers", total_couriers)
        st.metric("Total Parcels", total_parcels)
        st.metric("Parcels In Transit", in_transit)
        st.metric("Parcels Delivered", delivered)
    
    


# ---------------- Customers Page ----------------
elif st.session_state.page == "Customers":
    st.subheader("👤 Customer Operations")
    action = st.selectbox("Select Action", ["Add", "View All", "Update", "Delete"])

    if action == "Add":
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        address = st.text_input("Address")
        if st.button("Save Customer"):
            result = customer_mgr.add(name, email, phone, address)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "View All":
        data = customer_mgr.get_all()
        if data["success"]:
            st.table(data["data"])
        else:
            st.error(data["message"])

    elif action == "Update":
        cust_id = st.text_input("Customer ID")
        if cust_id:
            cust_id = int(cust_id)  # <-- convert to int
        name = st.text_input("New Name")
        email = st.text_input("New Email")
        phone = st.text_input("New Phone")
        address = st.text_input("New Address")
        if st.button("Update Customer"):
            result = customer_mgr.update(cust_id, name, email, phone, address)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "Delete":
        cust_id = st.text_input("Customer ID")
        if cust_id:
            cust_id = int(cust_id)  # <-- convert to int
        if st.button("Delete Customer"):
            result = customer_mgr.delete(cust_id)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

# ---------------- Couriers Page ----------------
elif st.session_state.page == "Couriers":
    st.subheader("📦 Courier Operations")
    action = st.selectbox("Select Action", ["Add", "View All", "Update", "Delete"])

    if action == "Add":
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        vehicle = st.text_input("Vehicle No.")
        if st.button("Save Courier"):
            result = courier_mgr.add(name, phone, vehicle)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "View All":
        data = courier_mgr.get_all()
        if data["success"]:
            st.table(data["data"])
        else:
            st.error(data["message"])

    elif action == "Update":
        courier_id = st.text_input("Courier ID")
        if courier_id:
            courier_id = int(courier_id)  # <-- convert to int
        name = st.text_input("New Name")
        phone = st.text_input("New Phone")
        vehicle = st.text_input("New Vehicle No.")
        if st.button("Update Courier"):
            result = courier_mgr.update(courier_id, name, phone, vehicle)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "Delete":
        courier_id = st.text_input("Courier ID")
        if courier_id:
            courier_id = int(courier_id)  # <-- convert to int
        if st.button("Delete Courier"):
            result = courier_mgr.delete(courier_id)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

# ---------------- Parcels Page ----------------
elif st.session_state.page == "Parcels":
    st.subheader("📬 Parcel Operations")
    action = st.selectbox("Select Action", ["Add", "View All", "Update", "Delete"])

    if action == "Add":
        sender_id = st.text_input("Sender ID")
        receiver_id = st.text_input("Receiver ID")
        if sender_id and receiver_id:
            sender_id = int(sender_id)  # <-- convert to int
            receiver_id = int(receiver_id)
        weight = st.number_input("Weight (kg)", min_value=0.1)
        price = st.number_input("Price", min_value=1)
        if st.button("Save Parcel"):
            result = parcel_mgr.add(sender_id, receiver_id, weight, price)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "View All":
        data = parcel_mgr.get_all()
        if data["success"]:
            st.table(data["data"])
        else:
            st.error(data["message"])

    elif action == "Update":
        parcel_id = st.text_input("Parcel ID")
        if parcel_id:
            parcel_id = int(parcel_id)  # <-- convert to int
        status = st.selectbox("Status", ["Pending", "In Transit", "Delivered"])
        if st.button("Update Parcel"):
            result = parcel_mgr.update(parcel_id, status=status)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "Delete":
        parcel_id = st.text_input("Parcel ID")
        if parcel_id:
            parcel_id = int(parcel_id)  # <-- convert to int
        if st.button("Delete Parcel"):
            result = parcel_mgr.delete(parcel_id)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

# ---------------- Tracking Page ----------------
elif st.session_state.page == "Tracking":
    st.subheader("🔎 Track Parcel")
    action = st.selectbox("Select Action", ["Add Tracking Update", "View by Parcel", "Update Tracking", "Delete Tracking"])

    if action == "Add Tracking Update":
        parcel_id = st.text_input("Parcel ID")
        courier_id = st.text_input("Courier ID")
        if parcel_id and courier_id:
            parcel_id = int(parcel_id)  # <-- convert to int
            courier_id = int(courier_id)
        location = st.text_input("Location")
        remarks = st.text_area("Remarks")
        if st.button("Save Tracking"):
            result = tracking_mgr.add(parcel_id, courier_id, location, remarks)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "View by Parcel":
        parcel_id = st.text_input("Parcel ID")
        if parcel_id:
            parcel_id = int(parcel_id)  # <-- convert to int
        if st.button("View Tracking"):
            result = tracking_mgr.get_by_parcel(parcel_id)
            if result["success"]:
                st.table(result["data"])
            else:
                st.error(result["message"])

    elif action == "Update Tracking":
        track_id = st.text_input("Tracking ID")
        if track_id:
            track_id = int(track_id)  # <-- convert to int
        location = st.text_input("New Location")
        remarks = st.text_area("New Remarks")
        if st.button("Update Tracking"):
            result = tracking_mgr.update(track_id, location=location, remarks=remarks)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

    elif action == "Delete Tracking":
        track_id = st.text_input("Tracking ID")
        if track_id:
            track_id = int(track_id)  # <-- convert to int
        if st.button("Delete Tracking"):
            result = tracking_mgr.delete(track_id)
            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])

st.markdown(
    "<div style='text-align: center; padding: 10px; color: #555;'>© 2025 Parcel Tracking System</div>",
    unsafe_allow_html=True
)

