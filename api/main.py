#Frontend ----> API -----> logic ------> db ------> Response

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
    allow_origins=["*"],  
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
    customer_id: int
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
    courier_id: int
    name: str
    phone: str
    vehicle_no: str

# ------------------ Parcel Models ------------------
class ParcelCreate(BaseModel):
    sender_id: int
    receiver_id: int
    weight: float
    price: float
    status: str = "Pending"

class ParcelUpdate(BaseModel):
    sender_id: Optional[int] = None
    receiver_id: Optional[int] = None
    weight: Optional[float] = None
    price: Optional[float] = None
    status: Optional[str] = None

class ParcelResponse(BaseModel):
    parcel_id: int
    sender_id: int
    receiver_id: int
    weight: float
    price: float
    status: str
    created_at: str

# ------------------ Tracking Models ------------------
class TrackingCreate(BaseModel):
    parcel_id: int
    courier_id: int
    location: str
    remarks: str = ""

class TrackingUpdate(BaseModel):
    parcel_id: Optional[int] = None
    courier_id: Optional[int] = None
    location: Optional[str] = None
    remarks: Optional[str] = None

class TrackingResponse(BaseModel):
    tracking_id: int
    parcel_id: int
    courier_id: int
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
def update_customer(customer_id: int, customer: CustomerUpdate):
    result = customer_manager.update(customer_id, **customer.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
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
def update_courier(courier_id: int, courier: CourierUpdate):
    result = courier_manager.update(courier_id, **courier.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/couriers/{courier_id}")
def delete_courier(courier_id: int):
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
def update_parcel(parcel_id: int, parcel: ParcelUpdate):
    result = parcel_manager.update(parcel_id, **parcel.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/parcels/{parcel_id}")
def delete_parcel(parcel_id: int):
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
def get_tracking(parcel_id: int):
    result = tracking_manager.get_by_parcel(parcel_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.put("/tracking/{tracking_id}")
def update_tracking(tracking_id: int, tracking: TrackingUpdate):
    result = tracking_manager.update(tracking_id, **tracking.model_dump(exclude_unset=True))
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.delete("/tracking/{tracking_id}")
def delete_tracking(tracking_id: int):
    result = tracking_manager.delete(tracking_id)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@app.get("/")
def root():
    return {"message": "Parcel Tracking API is running "}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)