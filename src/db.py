# dp_manager.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from uuid import uuid4
from datetime import datetime

# Load env variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Supabase client
supabase: Client = create_client(url, key)

# ----- Customers -----
def add_customer(name, email, phone, address):
    """Add customer"""
    data = {
        "customer_id": str(uuid4()),
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
    return supabase.table("customers").insert(data).execute()

def get_customers():
    """Get customers"""
    return supabase.table("customers").select("*").execute().data

def update_customer(customer_id, name=None, email=None, phone=None, address=None):
    """Update customer"""
    data = {}
    if name: data["name"] = name
    if email: data["email"] = email
    if phone: data["phone"] = phone
    if address: data["address"] = address
    return supabase.table("customers").update(data).eq("customer_id", customer_id).execute()

def delete_customer(customer_id):
    """Delete customer"""
    return supabase.table("customers").delete().eq("customer_id", customer_id).execute()


# ----- Couriers -----
def add_courier(name, phone, vehicle_no):
    """Add courier"""
    data = {
        "courier_id": str(uuid4()),
        "name": name,
        "phone": phone,
        "vehicle_no": vehicle_no
    }
    return supabase.table("couriers").insert(data).execute()

def get_couriers():
    """Get couriers"""
    return supabase.table("couriers").select("*").execute().data

def update_courier(courier_id, name=None, phone=None, vehicle_no=None):
    """Update courier"""
    data = {}
    if name: data["name"] = name
    if phone: data["phone"] = phone
    if vehicle_no: data["vehicle_no"] = vehicle_no
    return supabase.table("couriers").update(data).eq("courier_id", courier_id).execute()

def delete_courier(courier_id):
    """Delete courier"""
    return supabase.table("couriers").delete().eq("courier_id", courier_id).execute()


# ----- Parcels -----
def add_parcel(sender_id, receiver_id, weight, price, status="Pending"):
    """Add parcel"""
    data = {
        "parcel_id": str(uuid4()),
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "weight": weight,
        "price": price,
        "status": status,
        "created_at": datetime.now().isoformat()
    }
    return supabase.table("parcels").insert(data).execute()

def get_parcels():
    """Get parcels"""
    return supabase.table("parcels").select("*").execute().data

def update_parcel(parcel_id, status=None, weight=None, price=None):
    """Update parcel"""
    data = {}
    if status: data["status"] = status
    if weight: data["weight"] = weight
    if price: data["price"] = price
    return supabase.table("parcels").update(data).eq("parcel_id", parcel_id).execute()

def delete_parcel(parcel_id):
    """Delete parcel"""
    return supabase.table("parcels").delete().eq("parcel_id", parcel_id).execute()


# ----- Tracking -----
def add_tracking(parcel_id, courier_id, location, remarks=""):
    """Add tracking"""
    data = {
        "tracking_id": str(uuid4()),
        "parcel_id": parcel_id,
        "courier_id": courier_id,
        "location": location,
        "timestamp": datetime.now().isoformat(),
        "remarks": remarks
    }
    return supabase.table("tracking").insert(data).execute()

def get_tracking(parcel_id):
    """Get parcel tracking"""
    return supabase.table("tracking").select("*").eq("parcel_id", parcel_id).execute().data

def update_tracking(tracking_id, location=None, remarks=None):
    """Update tracking"""
    data = {}
    if location: data["location"] = location
    if remarks: data["remarks"] = remarks
    return supabase.table("tracking").update(data).eq("tracking_id", tracking_id).execute()

def delete_tracking(tracking_id):
    """Delete tracking"""
    return supabase.table("tracking").delete().eq("tracking_id", tracking_id).execute()

