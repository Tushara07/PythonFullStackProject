# Parcel/Courier Tracking System

The Parcel/Courier Tracking System simplifies parcel management and tracking for courier services. Customers can register parcels with sender and receiver details and track them using a unique ID. Couriers update parcel status and location at each checkpoint. Built with Python (backend) and Supabase (database), the system ensures efficient data handling and scalability. A simple web frontend (React/HTML-CSS) allows easy interaction, showcasing skills in Python, SQL, database design, and API integration.

# Features

1.Parcel Registration – Register parcels with sender and receiver details.

2.Tracking ID Generation – Automatically generate a unique tracking ID for each parcel.

3.Status Tracking – Track parcel status: Pending, In Transit, Delivered, Cancelled.

4.Courier Updates – Couriers can update parcel location and status in real time.

5.Centralized Database – Maintain a centralized database of Customers, Couriers, and Parcels.

6.Tracking History – View parcel tracking history with timestamps and remarks.

7.Interactive Frontend – User-friendly interface using Streamlit for customers and couriers.

8.Data Management – Efficient CRUD operations for managing all records.

# Project Structure

ParcelCourier Tracking System/
|
|----src/               # core application logic
|   |---logic.py        # Business logic and task operations
|   |---db.py           # Database operation
|
|----api/               # Backend API
|   |---main.py         # FastAPI endpoints
|
|----frontend/          # Frontend applications
|   |---app.py          # Streamlit web interface
|
|----requirements.txt   # Python dependencies
|
|----README.md          # Project Documentation
|
|----.env               # Python Environment Variables 


# Quick Start

## Prerequisites

- Python 3.8 or higher
- A Supabase account
- Git(Push, Cloning)

### 1. Clone or Download the project

# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2. Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set up Supabase Project:

1.Create a Supabase Project

2.Create the Customers Table:

- Go to the SQL Editior in Supabase dashboard
- Run this SQL command:

    -- 1. Customers Table
    CREATE TABLE customers (
        customer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(15) NOT NULL,
        address TEXT NOT NULL
    );

    -- 2. Couriers Table
    CREATE TABLE couriers (
        courier_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        vehicle_no VARCHAR(20) NOT NULL
    );

    -- 3. Parcels Table
    CREATE TABLE parcels (
        parcel_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        sender_id UUID REFERENCES customers(customer_id) ON DELETE CASCADE,
        receiver_id UUID REFERENCES customers(customer_id) ON DELETE CASCADE,
        weight DECIMAL(10,2) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'In Transit', 'Delivered', 'Cancelled')),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- 4. Tracking Table
    CREATE TABLE tracking (
        tracking_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        parcel_id UUID REFERENCES parcels(parcel_id) ON DELETE CASCADE,
        courier_id UUID REFERENCES couriers(courier_id) ON DELETE SET NULL,
        location VARCHAR(100) NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        remarks TEXT
    );

3.Get your supabase credentials

### 4. Configure Environment Variables

1. Create '.env' file in the project root

2. Add your Supabase credentials to '.env' :
SUPABASE_URL= "your_project_url"
SUPABASE_KEY= "your_anonymous_key"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

- The app will open in your browser at `http://localhost:8000`

## FastAPI Backend
cd api
python main.py

- The API will be available as `http://localhost:8080`

## How to use

1. Register Parcel – Customer enters sender and receiver details, weight, and price. A tracking ID is generated.

2. Assign Courier – System assigns a courier to deliver the parcel.

3. Track Parcel – Customer checks the parcel status using the tracking ID.

4. Update Status – Courier updates parcel location and status (Pending, In Transit, Delivered, Cancelled).

5. View History – All updates with timestamps and remarks are stored and can be viewed.


## Technical Details 

Python Libraries:

    - Streamlit – Frontend web interface

    - Supabase-py – Database operations with Supabase

    - UUID – Generate unique IDs for parcels, customers, and couriers

    - Datetime – Manage timestamps for tracking updates

### Technologies Used

    - Database (DB): Supabase (PostgreSQL)

	- Backend: FastAPI (Python REST API Framework)

	- Frontend: Streamlit (Python web framework)

	- Tools: VS Code, Supabase Console, Postman/Thunder Client

    - Language: Python 3.8+

### Key components

1. src/db.py : Database operations 
- Handles all CRUD operations with Supabase

2. src/logic.py : Business logic 
- Task validation and processing 
- Implements parcel registration, status updates, courier assignment, and validation

3. api/main.py : Backend API
- Contains FastAPI endpoints for interacting with parcels, customers, couriers, and tracking data.
- Serves as the REST API layer between frontend and database.

4. frontend/app.py : Streamlit frontend
- Provides an interactive web interface for customers and couriers.
- Allows parcel registration, tracking, and status updates.

5. requirements.txt : Python dependencies
- Lists all Python packages required to run the project (FastAPI, Streamlit, Supabase client, etc.).

6. README.md : Project documentation
- Explains project overview, setup instructions, features, and usage.

7. .env : Environment variables
- Stores sensitive keys and configurations, such as Supabase URL and API key, securely.


## Troubleshooting

## Common Issues

1. "Module not found errors"
    - Make sure you've installed all dependencies :
        `pip install -r requirements.txt`
    - Check that you're running commands from correct directory

## Future Enhancements

Ideas for extending this project:

1. Real-time Notifications – Send SMS or email alerts to customers and couriers for parcel status updates.

2. Route Optimization – Integrate maps and GPS tracking to plan the fastest and most efficient delivery routes.

3. User Authentication & Role Management – Implement secure login for customers and couriers with role-based access control.

4. Analytics & Reports – Generate detailed reports on deliveries, delays, courier performance, and parcel history.

5. Mobile App Interface – Develop a mobile-friendly version for customers and couriers to track and update parcels on the go.

## Support

If you encounter any issues or have questions :
Mobile : 6303072571
Email : tusharakatamreddy@gmail.com




