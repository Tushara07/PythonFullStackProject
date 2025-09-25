#Frontend ----> API -----> logic ------> db ------> Response
#api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys,os
from typing import Optional

#import taskmanager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import CustomerManager, CourierManager, ParcelManager, TrackingManager

customer_manager = CustomerManager()
courier_manager = CourierManager()
parcel_manager = ParcelManager()
tracking_manager = TrackingManager()

app = FastAPI(title="Parcel management API", version="1.0")
# Allow CORS (for frontend calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#----Data Models------
# ------------------ Customer Models ------------------
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerResponse(BaseModel):
    customer_id: str
    name: str
    email: str
    phone: str
    address: str

# ------------------ Courier Models ------------------
class CourierCreate(BaseModel):
    name: str
    phone: str
    vehicle_no: str

class CourierUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    vehicle_no: Optional[str] = None

class CourierResponse(BaseModel):
    courier_id: str
    name: str
    phone: str
    vehicle_no: str

# ------------------ Parcel Models ------------------
class ParcelCreate(BaseModel):
    sender_id: str
    receiver_id: str
    weight: float
    price: float
    status: str = "Pending"

class ParcelUpdate(BaseModel):
    sender_id: Optional[str] = None
    receiver_id: Optional[str] = None
    weight: Optional[float] = None
    price: Optional[float] = None
    status: Optional[str] = None

class ParcelResponse(BaseModel):
    parcel_id: str
    sender_id: str
    receiver_id: str
    weight: float
    price: float
    status: str
    created_at: str

# ------------------ Tracking Models ------------------
class TrackingCreate(BaseModel):
    parcel_id: str
    courier_id: str
    location: str
    remarks: str = ""

class TrackingUpdate(BaseModel):
    parcel_id: Optional[str] = None
    courier_id: Optional[str] = None
    location: Optional[str] = None
    remarks: Optional[str] = None

class TrackingResponse(BaseModel):
    tracking_id: str
    parcel_id: str
    courier_id: str
    location: str
    remarks: str
    timestamp: str


# ------------------ Customer Endpoints ------------------
@app.post("/customers")
def create_customer(customer: CustomerCreate):
    result = customer_manager.add(**customer.model_dump())
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/customers")
def get_customers():
    result = customer_manager.get_all()
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.put("/customers/{customer_id}")
def update_customer(customer_id: str, customer: CustomerUpdate):
    result = customer_manager.update(customer_id, **customer.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    result = customer_manager.delete(customer_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

# ------------------ Courier Endpoints ------------------
@app.post("/couriers")
def create_courier(courier: CourierCreate):
    result = courier_manager.add(**courier.model_dump())
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/couriers")
def get_couriers():
    result = courier_manager.get_all()
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.put("/couriers/{courier_id}")
def update_courier(courier_id: str, courier: CourierUpdate):
    result = courier_manager.update(courier_id, **courier.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/couriers/{courier_id}")
def delete_courier(courier_id: str):
    result = courier_manager.delete(courier_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

# ------------------ Parcel Endpoints ------------------
@app.post("/parcels")
def create_parcel(parcel: ParcelCreate):
    result = parcel_manager.add(**parcel.model_dump())
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/parcels")
def get_parcels():
    result = parcel_manager.get_all()
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.put("/parcels/{parcel_id}")
def update_parcel(parcel_id: str, parcel: ParcelUpdate):
    result = parcel_manager.update(parcel_id, **parcel.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/parcels/{parcel_id}")
def delete_parcel(parcel_id: str):
    result = parcel_manager.delete(parcel_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

# ------------------ Tracking Endpoints ------------------
@app.post("/tracking")
def create_tracking(tracking: TrackingCreate):
    result = tracking_manager.add(**tracking.model_dump())
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/tracking/{parcel_id}")
def get_tracking(parcel_id: str):
    result = tracking_manager.get_by_parcel(parcel_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.put("/tracking/{tracking_id}")
def update_tracking(tracking_id: str, tracking: TrackingUpdate):
    result = tracking_manager.update(tracking_id, **tracking.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/tracking/{tracking_id}")
def delete_tracking(tracking_id: str):
    result = tracking_manager.delete(tracking_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)