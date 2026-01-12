# Attendance Calculator – Smart Attendance Planning System

## Introduction
In most colleges and universities, students are required to maintain a minimum attendance percentage, commonly around 75 percent, to be eligible for examinations. However, attendance portals typically present only a percentage value, which does not help students make informed decisions.

This project addresses that gap by transforming raw attendance data into clear, actionable insights that help students plan their attendance responsibly and without panic.

---

## Problem Statement
Students frequently face the following issues:
- Attendance systems show only percentages, not actionable guidance
- Students do not know how many classes they must attend going forward
- There is uncertainty about how many classes can be missed safely
- Lack of clarity leads to stress, poor planning, and last-minute panic

There is a clear disconnect between attendance data and meaningful decision-making support.

---

## Project Objective
The objective of this project is to convert attendance data into practical, decision-oriented answers:
- How many classes must be attended from now on to meet eligibility criteria?
- How many classes can still be missed without falling below the requirement?
- Is the student currently safe, at risk, or beyond recovery?

The system focuses on clarity, correctness, and responsible academic planning.

---

## Project Evolution

### Round 1 – Proof of Concept
Round 1 was developed as a rapid proof-of-concept to validate the idea and the feasibility of attendance prediction.

**Technology Used**
- Python
- Streamlit

**Key Capabilities**
- Semester start and end date input
- Weekly timetable input
- Current attendance percentage input
- Required attendance percentage input
- SAFE / WARNING status indication

**Limitations of Round 1**
- Relied on weekly approximations instead of real calendar dates
- Did not account for holidays
- Monolithic architecture unsuitable for scaling
- Limited UI control

---

### Round 2 – System Design and Architectural Enhancement
Round 2 focuses on correctness, scalability, and clean system design. The architecture was redesigned to separate concerns and improve long-term maintainability.

**Major Improvements**
- Transition from Streamlit to a custom frontend
- Introduction of a stateless backend API
- Accurate date-based class counting
- Holiday-aware attendance calculation
- Academic-grade rounding rules

---

## Technology Stack (Round 2)

### Frontend
- HTML
- CSS
- JavaScript

The frontend is lightweight, framework-independent, and designed for clarity and ease of use. Subject-wise input is optional and does not disrupt the core workflow.

### Backend
- Python
- FastAPI

The backend exposes a stateless REST API with a `POST /calculate` endpoint. CORS is enabled to allow seamless frontend integration.

---

## Core System Features
- Day-by-day calendar iteration for accurate class counting
- Automatic exclusion of predefined holidays
- Optional subject-wise attendance input
- Strict academic rounding:
  - Attended classes are floored
  - Required classes are ceiled
- Clear status classification:
  - SAFE
  - WARNING
  - CRITICAL

---

## System Architecture and Data Flow
The system architecture follows a clean separation of responsibilities:
- User interacts with the frontend
- Frontend sends structured input to the backend API
- Backend processes data using calendar-based logic and holiday rules
- Backend returns computed attendance guidance
- Frontend presents clear results to the user

Detailed system flow and Data Flow Diagrams (DFD) are included in the repository for reference.

---

## Repository Structure
attendance_calculator/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── System_flow_diagram/
│   ├── system_flow.svg
│   └── system_architecture_round2_dfd.svg
├── backend.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Scalability and Reliability
The Round 2 architecture is designed for future growth:
- Stateless backend allows horizontal scaling
- Frontend and backend can be deployed independently
- Clear separation of concerns improves maintainability
- Architecture supports future feature expansion

---

## Team Contributions
- Shreeyash Raajendran Kurupath – System design, logic planning, documentation
- Mohd Uvais Ahmed – Frontend development, UX flow, integration
- Mohammad Rayyan Farooqui – Backend logic and API implementation
- Mujtaba Hassan – Testing, validation, and documentation support

---

## Disclaimer
All calculations provided by this system are indicative and intended solely for planning assistance. Final attendance eligibility is subject to institutional rules and regulations.
