# CCLab-2

# Lab 2: Monolithic Architecture - College Fest Application

## Student Information
- **Name:** [Your Name]
- **SRN:** PES1UG23CS725
- **Course:** Cloud Computing

## Project Overview
This project demonstrates a **Monolithic Architecture** using a FastAPI-based "College Fest" application. [cite_start]It illustrates the characteristics of a monolith, including tight integration of modules, single deployment units, and the "Single Point of Failure" risk[cite: 9, 54, 56]. [cite_start]The lab involves identifying performance bottlenecks and observing how a bug in one module affects the entire system[cite: 57, 182].

## Screenshots
The `screenshots/` folder contains the following:
- [cite_start]**SS1:** Events page successfully loaded[cite: 149].
- [cite_start]**SS2:** Monolith Failure (Division by Zero)[cite: 153].
- [cite_start]**SS3:** Checkout page working after bug fix[cite: 189].
- [cite_start]**SS4 & SS5:** Before/After optimization for /checkout[cite: 246, 442].
- [cite_start]**SS6 & SS7:** Before/After optimization for /events[cite: 450, 451].
- [cite_start]**SS8 & SS9:** Before/After optimization for /my-events[cite: 455, 456].

## Optimization Explanations

### 1. Route: `/checkout`
* [cite_start]**Bottleneck:** A "division by zero" error acted as a single point of failure, crashing the entire server[cite: 161]. [cite_start]Additionally, an inefficient `while` loop was used to calculate the total payable[cite: 336, 337].
* [cite_start]**Change Made:** Commented out the crash-inducing code and replaced the linear `while` loop with a direct summation loop[cite: 186, 340].
* [cite_start]**Performance Impact:** Restored availability and reduced CPU cycles, leading to a drop in average response time[cite: 441].

### 2. Route: `/events`
* **Bottleneck:** An intentional "waste" loop executing 3,000,000 iterations for every request.
* **Change Made:** Removed the computational loop logic entirely from the endpoint.
* **Performance Impact:** Significant reduction in latency as the CPU no longer performs millions of useless calculations before rendering the HTML.

### 3. Route: `/my-events`
* **Bottleneck:** A "dummy" loop running 1,500,000 iterations created artificial processing delay.
* **Change Made:** Deleted the loop to streamline the request-handling process.
* **Performance Impact:** Improved the request-response cycle, allowing the server to handle database joins and template rendering instantly.

## Setup Instructions
1. [cite_start]Create a virtual environment: `python -m venv .venv`[cite: 71].
2. [cite_start]Activate environment: `.\.venv\Scripts\activate`[cite: 72].
3. [cite_start]Install requirements: `pip install -r requirements.txt`[cite: 76].
4. [cite_start]Populate database: `python insert_events.py`[cite: 79].
5. [cite_start]Run server: `uvicorn main:app --reload`[cite: 85].
