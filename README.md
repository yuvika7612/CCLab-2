# CCLab-2

# Lab 2: Monolithic Architecture - College Fest Application

## Student Information
- **Name:** Yuvika T
- **SRN:** PES1UG23CS725
- **Course:** Cloud Computing

## Project Overview
This project demonstrates a **Monolithic Architecture** using a FastAPI-based "College Fest" application.It illustrates the characteristics of a monolith, including tight integration of modules, single deployment units, and the "Single Point of Failure" risk. The lab involves identifying performance bottlenecks and observing how a bug in one module affects the entire system.

## Screenshots
- **SS1:** Events page successfully loaded.
- **SS2:** Monolith Failure (Division by Zero).
- **SS3:** Checkout page working after bug fix.
- **SS4 & SS5:** Before/After optimization for /checkout.
- **SS6 & SS7:** Before/After optimization for /events.
- **SS8 & SS9:** Before/After optimization for /my-events.

## Optimization Explanations

### 1. Route: `/checkout`
* **Bottleneck:** A "division by zero" error acted as a single point of failure, crashing the entire server.Additionally, an inefficient `while` loop was used to calculate the total payable.
* **Change Made:** Commented out the crash-inducing code and replaced the linear `while` loop with a direct summation loop.
* **Performance Impact:** Restored availability and reduced CPU cycles, leading to a drop in average response time.

### 2. Route: `/events`
* **Bottleneck:** An intentional "waste" loop executing 3,000,000 iterations for every request.
* **Change Made:** Removed the computational loop logic entirely from the endpoint.
* **Performance Impact:** Significant reduction in latency as the CPU no longer performs millions of useless calculations before rendering the HTML.

### 3. Route: `/my-events`
* **Bottleneck:** A "dummy" loop running 1,500,000 iterations created artificial processing delay.
* **Change Made:** Deleted the loop to streamline the request-handling process.
* **Performance Impact:** Improved the request-response cycle, allowing the server to handle database joins and template rendering instantly.

## Setup Instructions
1. Create a virtual environment: `python -m venv .venv`.
2. Activate environment: `.\.venv\Scripts\activate`.
3. Install requirements: `pip install -r requirements.txt`.
4. Populate database: `python insert_events.py`.
5. Run server: `uvicorn main:app --reload`.
