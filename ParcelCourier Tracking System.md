## **Parcel/Courier Tracking System**





#### **Abstract**



The Parcel/Courier Tracking System simplifies parcel management and tracking for courier services. Customers can register parcels with sender and receiver details and track them using a unique ID. Couriers update parcel status and location at each checkpoint. Built with Python (backend) and Supabase (database), the system ensures efficient data handling and scalability. A simple web frontend (React/HTML-CSS) allows easy interaction, showcasing skills in Python, SQL, database design, and API integration.



#### **Technology Stack**



&nbsp;	- Database (DB): Supabase (PostgreSQL)



&nbsp;	- Backend: Python



&nbsp;	- Frontend: Streamlit



&nbsp;	- Tools: VS Code, Supabase Console, Postman/Thunder Client



#### **Database tables:**



**1. Customers**



Column        Type             Description

customer\_id   UUID / Serial    Unique ID for each customer

name          VARCHAR          Full name of the customer

email         VARCHAR          Customer’s email address

phone         VARCHAR          Contact number

address       TEXT             Delivery or home address



**2. Couriers**



Column        Type             Description

courier\_id    UUID / Serial    Unique ID for each courier staff

name          VARCHAR          Courier staff full name

phone         VARCHAR          Contact number

vehicle\_no    VARCHAR          Vehicle registration number



**3. Parcels**



Column        Type                     Description

parcel\_id     UUID / Serial            Unique ID for each parcel

sender\_id     INT / UUID → Customers  Reference to sender

receiver\_id   INT / UUID → Customers  Reference to receiver

weight        DECIMAL                  Parcel weight (kg)

price         DECIMAL                  Shipping cost

status        VARCHAR                  Parcel status: Pending, In Transit, Delivered, Cancelled

created\_at    TIMESTAMP                Date and time of parcel booking



**4. Tracking**



Column        Type                     Description

tracking\_id   UUID / Serial            Unique ID for each tracking record

parcel\_id     INT / UUID → Parcels     Reference to the parcel being tracked

courier\_id    INT / UUID → Couriers    Courier handling this update

location      VARCHAR                  Current parcel location / branch

timestamp     TIMESTAMP                Date and time of the update

remarks       TEXT                     Additional notes (e.g., “Out for Delivery”)



 -- 1. Customers Table

&nbsp;   CREATE TABLE customers (

&nbsp;       customer\_id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),

&nbsp;       name VARCHAR(100) NOT NULL,

&nbsp;       email VARCHAR(100) UNIQUE NOT NULL,

&nbsp;       phone VARCHAR(15) NOT NULL,

&nbsp;       address TEXT NOT NULL

&nbsp;   );



&nbsp;   -- 2. Couriers Table

&nbsp;   CREATE TABLE couriers (

&nbsp;       courier\_id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),

&nbsp;       name VARCHAR(100) NOT NULL,

&nbsp;       phone VARCHAR(15) NOT NULL,

&nbsp;       vehicle\_no VARCHAR(20) NOT NULL

&nbsp;   );



&nbsp;   -- 3. Parcels Table

&nbsp;   CREATE TABLE parcels (

&nbsp;       parcel\_id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),

&nbsp;       sender\_id UUID REFERENCES customers(customer\_id) ON DELETE CASCADE,

&nbsp;       receiver\_id UUID REFERENCES customers(customer\_id) ON DELETE CASCADE,

&nbsp;       weight DECIMAL(10,2) NOT NULL,

&nbsp;       price DECIMAL(10,2) NOT NULL,

&nbsp;       status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'In Transit', 'Delivered', 'Cancelled')),

&nbsp;       created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP

&nbsp;   );



&nbsp;   -- 4. Tracking Table

&nbsp;   CREATE TABLE tracking (

&nbsp;       tracking\_id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),

&nbsp;       parcel\_id UUID REFERENCES parcels(parcel\_id) ON DELETE CASCADE,

&nbsp;       courier\_id UUID REFERENCES couriers(courier\_id) ON DELETE SET NULL,

&nbsp;       location VARCHAR(100) NOT NULL,

&nbsp;       timestamp TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,

&nbsp;       remarks TEXT

&nbsp;   );





#### **Project Structure**



ParcelCourier Tracking System/

│

├── src/                 		# Core application logic

│   ├── logic.py        	# Business logic and task operations

│   └── db.py            	# Database operations (Supabase integration)

│

├── api/                 		# Backend API

│   └── main.py          	# FastAPI endpoints

│

├── frontend/            	# Frontend application

│   └── app.py           	# Streamlit web interface

│

├── requirements.txt     # Python dependencies

├── README.md            # Project documentation

└── .env                 		# Environment variables (API keys, DB URL, etc.)







