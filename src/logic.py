from src.db import DatabaseManager

'''Acts as a bridge between frontend (streamlit/FastAPI) and the database'''

# ----- Customer Operations -----
class CustomerManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, name, email, phone, address):
        if not name or not email or not phone or not address:
            return {"success": False, "message": "All fields required"}
        try:
            self.db.add_customer(name, email, phone, address)
            return {"success": True, "message": "Customer added successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update(self, customer_id, name=None, email=None, phone=None, address=None):
        if not customer_id:
            return {"success": False, "message": "Customer ID required"}
        try:
            self.db.update_customer(customer_id, name, email, phone, address)
            return {"success": True, "message": "Customer updated successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def get_all(self):
        try:
            data = self.db.get_customers()
            return {"success": True, "data": data}
        except Exception as e:
            return {"success": False, "message": str(e), "data": []}

    def delete(self, customer_id):
        if not customer_id:
            return {"success": False, "message": "Customer ID required"}
        try:
            self.db.delete_customer(customer_id)
            return {"success": True, "message": "Customer deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}


# ----- Courier Operations -----
class CourierManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, name, phone, vehicle_no):
        if not name or not phone or not vehicle_no:
            return {"success": False, "message": "All fields required"}
        try:
            self.db.add_courier(name, phone, vehicle_no)
            return {"success": True, "message": "Courier added successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update(self, courier_id, name=None, phone=None, vehicle_no=None):
        if not courier_id:
            return {"success": False, "message": "Courier ID required"}
        try:
            self.db.update_courier(courier_id, name, phone, vehicle_no)
            return {"success": True, "message": "Courier updated successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def get_all(self):
        try:
            data = self.db.get_couriers()
            return {"success": True, "data": data}
        except Exception as e:
            return {"success": False, "message": str(e), "data": []}

    def delete(self, courier_id):
        if not courier_id:
            return {"success": False, "message": "Courier ID required"}
        try:
            self.db.delete_courier(courier_id)
            return {"success": True, "message": "Courier deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}


# ----- Parcel Operations -----
class ParcelManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, sender_id, receiver_id, weight, price, status="Pending"):
        if not sender_id or not receiver_id or weight is None or price is None:
            return {"success": False, "message": "All fields required"}
        try:
            self.db.add_parcel(sender_id, receiver_id, weight, price, status)
            return {"success": True, "message": "Parcel added successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update(self, parcel_id, sender_id=None, receiver_id=None, weight=None, price=None, status=None):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required"}
        try:
            self.db.update_parcel(parcel_id, status, weight, price)
            return {"success": True, "message": "Parcel updated successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def get_all(self):
        try:
            data = self.db.get_parcels()
            return {"success": True, "data": data}
        except Exception as e:
            return {"success": False, "message": str(e), "data": []}

    def delete(self, parcel_id):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required"}
        try:
            self.db.delete_parcel(parcel_id)
            return {"success": True, "message": "Parcel deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}


# ----- Tracking Operations -----
class TrackingManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, parcel_id, courier_id, location, remarks=""):
        if not parcel_id or not courier_id or not location:
            return {"success": False, "message": "All fields required"}
        try:
            self.db.add_tracking(parcel_id, courier_id, location, remarks)
            return {"success": True, "message": "Tracking added successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def update(self, tracking_id, parcel_id=None, courier_id=None, location=None, remarks=None):
        if not tracking_id:
            return {"success": False, "message": "Tracking ID required"}
        try:
            self.db.update_tracking(tracking_id, location, remarks)
            return {"success": True, "message": "Tracking updated successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    def get_by_parcel(self, parcel_id):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required", "data": []}
        try:
            data = self.db.get_tracking(parcel_id)
            return {"success": True, "data": data}
        except Exception as e:
            return {"success": False, "message": str(e), "data": []}

    def delete(self, tracking_id):
        if not tracking_id:
            return {"success": False, "message": "Tracking ID required"}
        try:
            self.db.delete_tracking(tracking_id)
            return {"success": True, "message": "Tracking deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
