# Attendance Calculator – System Design & Prototype (Round 1 & Round 2)

## Problem Statement

In most colleges and universities, students are required to maintain a minimum attendance percentage (commonly 75%) to be eligible for examinations.

In practice, students face multiple issues:
- Attendance portals show only percentages, not actionable guidance
- Students do not know how many classes they must attend going forward
- There is uncertainty about how many classes can be missed safely
- This lack of clarity leads to stress, panic, and poor attendance planning

There exists a clear gap between raw attendance data and meaningful, decision-oriented insight.

---

## Project Objective

The objective of this project is to bridge that gap by translating attendance data into clear, practical answers:
- How many classes must be attended from now on?
- How many classes can still be missed?
- Is the student currently safe, at risk, or beyond recovery?

The focus is on clarity, correctness, and responsible planning.

---

## Round 1: Prototype Overview (Proof of Concept)

### Purpose of Round 1

Round 1 was designed as a rapid proof-of-concept to validate:
- The core idea
- Attendance prediction feasibility
- User understanding of results

### Technology Used (Round 1)

- Python
- Streamlit (rapid UI prototyping)

Streamlit was intentionally used to quickly demonstrate logic without full system architecture.

### Capabilities (Round 1)

- Semester start and end date input
- Weekly schedule input
- Current attendance percentage input
- Required attendance percentage input
- SAFE / WARNING status output

### System Flow Diagram (Round 1)

System_flow_diagram/system_flow.svg

---

## Why Round 2 Was Needed

Round 1 relied on ideal assumptions and had limitations:
- Weekly approximations instead of real calendar dates
- No holiday handling
- Limited UI control
- Monolithic design unsuitable for scaling

Round 2 focuses on correctness, extensibility, and system-level design.

---

## Round 2: Architecture & Enhancements

### Architectural Transition

Round 1 used a Streamlit-based prototype.  
Round 2 uses a custom frontend with a stateless backend API.

This transition enables:
- Clear separation of frontend and backend
- Better UI/UX control
- Improved accuracy
- Scalability and future extensibility

---

## Technology Stack (Round 2)

### Frontend

Located in:
frontend/
├── index.html
├── style.css
└── script.js

- Built using HTML, CSS, and JavaScript
- No framework dependency
- Lightweight and user-friendly
- Optional subject-wise input without breaking core workflow

### Backend

Located at:
backend.py

- Python with FastAPI
- Stateless REST API
- Endpoint: POST /calculate
- CORS-enabled for frontend integration

---

## Core Backend Improvements (Round 2)

### Date-Accurate Class Counting
- Day-by-day calendar iteration
- Handles mid-week semester starts and cutoffs
- Removes weekly approximation errors

### Holiday Awareness
- Predefined holiday configuration
- Automatically excluded from class counting
- No additional user input required

### Strict Academic Rounding
- Attended classes are floored
- Required classes are ceiled
- Prevents over-crediting attendance

### Optional Subject-Wise Input
- Subject-wise entry is optional
- Core calculations work without subject data
- Improves accuracy without increasing user burden

---

## System Architecture & Data Flow Diagram (Round 2)

The complete DFD Level-1 for Round 2 is available at:

System_flow_diagram/system_architecture_round2_dfd.svg

This diagram illustrates:
- User, frontend, and backend interaction
- Sequential backend processing
- Static holiday data usage
- Clear data flow paths
- Future extensibility points

---

## Scalability and Reliability

The Round 2 design supports growth through:
- Stateless backend architecture
- Independent frontend and backend components
- Clear responsibility separation
- Horizontal backend scaling capability
- Isolated failure domains

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

## Team Contributions

- Shreeyash Raajendran Kurupath – System design, logic planning, documentation
- Mohd Uvais Ahmed – Frontend development, UX flow, integration
- Mohammad Rayyan Farooqui – Backend logic, API implementation
- Mujtaba Hassan – Testing, validation, documentation support

---

## Note

This repository demonstrates the evolution from a proof-of-concept (Round 1) to a structured and scalable system design (Round 2).  
All calculations are indicative and intended for planning assistance. Final attendance decisions remain subject to institutional rules.
