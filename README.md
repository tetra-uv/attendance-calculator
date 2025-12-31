# Attendance Calculator – Prototype (Round 1)

## Problem Statement

In most colleges and universities, students are required to maintain a minimum attendance percentage (commonly 75%) to be eligible for examinations.

In reality, students often face the following problems:
- Attendance portals only show percentages, not clear guidance.
- Students do not know how many classes they must attend going forward.
- There is confusion about how many classes can be missed without risk.
- This uncertainty causes stress, panic, and poor planning.

There is a clear gap between raw attendance data and meaningful, actionable insight.

---

## Our Solution

The Attendance Calculator is a simple web-based prototype that converts attendance data into clear decisions.

Instead of showing only percentages, the system answers practical questions such as:
- How many classes must be attended from now?
- How many classes can be missed without falling below the required attendance?
- Is the student currently safe or at risk?

The goal is clarity, not complexity.

---

## What the Prototype Does

This prototype allows a student to:
- Enter semester start and end dates
- Provide a weekly class schedule
- Input current attendance percentage
- Set the minimum required attendance percentage

Based on these inputs, the system calculates:
- Total classes in the semester
- Classes completed so far
- Classes attended
- Remaining classes
- Classes that must be attended
- Classes that can be missed
- A clear SAFE or WARNING status

---

## Responsible Use of the Term “Bunk”

In this project, the word “bunk” is used in a practical and responsible sense.

It does not promote irresponsible skipping of classes. Instead, it represents flexibility that students may need for:
- Health-related breaks
- Mental fatigue or burnout
- Personal or family situations
- Managing the demanding and chaotic nature of college life

The purpose of this tool is to help students plan responsibly within institutional attendance rules, not to encourage absence.

---

## System Working and Flow

The system follows a clear and logical flow:

1. The user enters semester dates, weekly schedule, and attendance details.
2. The system validates all inputs for logical correctness.
3. If inputs are invalid, an error is shown immediately.
4. If inputs are valid:
   - Total semester classes are calculated.
   - Completed and remaining classes are derived.
   - Required future attendance is computed.
   - A SAFE or WARNING result is generated.
5. The calculated results are displayed back to the user.

---

## System Flow Diagram

The complete working of the system is visually explained in the flow diagram below:

diagrams/system_flow.svg

This diagram represents:
- Input handling
- Validation decision
- Core calculation logic
- Error handling path
- Final result output

---

## Why This Project Matters

Students think in terms of classes, not percentages.

By translating attendance rules into clear numbers, this tool:
- Reduces confusion
- Prevents last-minute panic
- Helps students plan attendance calmly and responsibly

The prototype focuses on real student needs rather than complex features.

---

## Technology Stack

- Python
- Streamlit (for user interface)
- Modular backend logic

---

## Planned Improvements for Round 2

This prototype assumes an ideal scenario where students already know their exact attendance percentage. In real situations, this is often inaccurate.

Planned improvements include:
- Manual marking of present and absent classes
- Extra and compensatory class handling
- Attendance percentage calculation based on user-entered data
- Holiday and cancelled class support
- OCR-based timetable extraction from PDFs or images
- Subject-wise attendance tracking

These improvements aim to bring the system closer to real-world accuracy.

---

## Project Structure

attendance_calculator/
│
├── app.py
├── backend.py
├── README.md
├── requirements.txt
├── CONTRIBUTING.md
├── .gitignore
│
└── diagrams/
    └── system_flow.svg

---

## Running the Project Locally

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

---

## Live Demo

The prototype is deployed and accessible here:https://attendance-calculator-djqnxaygyglkzeuefat32l.streamlit.app/

This deployment is intended for demonstration purposes.

---


## Note

This repository represents a Round 1 prototype intended for demonstration and evaluation purposes.
<br/>

Authors : Shreeyash Raajendran Kurupath , Mohd Uvais Ahmed , Mohammad Rayyan Farooqui , Mujtaba hassan 