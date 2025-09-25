#src_logic.py

from src.db import DatabaseManager

'''Acts as a bridge between frontend (streamlit/FastAPI) and the database'''

# ----- Customer Operations -----
class CustomerManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, name, email, phone, address):
        if not name or not email or not phone or not address:
            return {"success": False, "message": "All fields required"}
        result = self.db.add_customer(name, email, phone, address)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Customer added successfully"}

    def update(self, customer_id, name=None, email=None, phone=None, address=None):
        if not customer_id:
            return {"success": False, "message": "Customer ID required"}
        result = self.db.update_customer(customer_id, name=name, email=email, phone=phone, address=address)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Customer updated successfully"}

    def get_all(self):
        result = self.db.get_customers()
        if result.error:
            return {"success": False, "message": f"Error: {result.error}", "data": []}
        return {"success": True, "data": result.data}

    def delete(self, customer_id):
        if not customer_id:
            return {"success": False, "message": "Customer ID required"}
        result = self.db.delete_customer(customer_id)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Customer deleted successfully"}


# ----- Courier Operations -----
class CourierManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, name, phone, vehicle_no):
        if not name or not phone or not vehicle_no:
            return {"success": False, "message": "All fields required"}
        result = self.db.add_courier(name, phone, vehicle_no)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Courier added successfully"}

    def update(self, courier_id, name=None, phone=None, vehicle_no=None):
        if not courier_id:
            return {"success": False, "message": "Courier ID required"}
        result = self.db.update_courier(courier_id, name=name, phone=phone, vehicle_no=vehicle_no)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Courier updated successfully"}

    def get_all(self):
        result = self.db.get_couriers()
        if result.error:
            return {"success": False, "message": f"Error: {result.error}", "data": []}
        return {"success": True, "data": result.data}

    def delete(self, courier_id):
        if not courier_id:
            return {"success": False, "message": "Courier ID required"}
        result = self.db.delete_courier(courier_id)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Courier deleted successfully"}


# ----- Parcel Operations -----
class ParcelManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, sender_id, receiver_id, weight, price, status="Pending"):
        if not sender_id or not receiver_id or weight is None or price is None:
            return {"success": False, "message": "All fields required"}
        result = self.db.add_parcel(sender_id, receiver_id, weight, price, status)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Parcel added successfully"}

    def update(self, parcel_id, sender_id=None, receiver_id=None, weight=None, price=None, status=None):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required"}
        result = self.db.update_parcel(parcel_id, sender_id=sender_id, receiver_id=receiver_id,weight=weight, price=price, status=status)
                                       
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Parcel updated successfully"}

    def get_all(self):
        result = self.db.get_parcels()
        if result.error:
            return {"success": False, "message": f"Error: {result.error}", "data": []}
        return {"success": True, "data": result.data}

    def delete(self, parcel_id):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required"}
        result = self.db.delete_parcel(parcel_id)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Parcel deleted successfully"}


# ----- Tracking Operations -----
class TrackingManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add(self, parcel_id, courier_id, location, remarks=""):
        if not parcel_id or not courier_id or not location:
            return {"success": False, "message": "All fields required"}
        result = self.db.add_tracking(parcel_id, courier_id, location, remarks)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Tracking added successfully"}

    def update(self, tracking_id, parcel_id=None, courier_id=None, location=None, remarks=None):
        if not tracking_id:
            return {"success": False, "message": "Tracking ID required"}
        result = self.db.update_tracking(tracking_id, parcel_id=parcel_id, courier_id=courier_id,location=location, remarks=remarks)
                                         
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Tracking updated successfully"}

    def get_by_parcel(self, parcel_id):
        if not parcel_id:
            return {"success": False, "message": "Parcel ID required", "data": []}
        result = self.db.get_tracking(parcel_id)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}", "data": []}
        return {"success": True, "data": result.data}

    def delete(self, tracking_id):
        if not tracking_id:
            return {"success": False, "message": "Tracking ID required"}
        result = self.db.delete_tracking(tracking_id)
        if result.error:
            return {"success": False, "message": f"Error: {result.error}"}
        return {"success": True, "message": "Tracking deleted successfully"}