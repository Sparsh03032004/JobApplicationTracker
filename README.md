# Job Application Tracker Dashboard 💼
> A clean, lightweight, dark-themed desktop productivity utility engineered to manage recruitment pipelines using a native relational SQL database.

Job Application Tracker is a structured desktop dashboard designed to optimize the workflow of job seekers. Built entirely in Python without heavy external database engine footprints, the application decouples data entry interfaces from storage operations, writing data directly to a persistent, localized transactional storage engine.

---

## ✨ Key Features

* **Relational SQL Storage Engine:** Implements a localized SQLite schema to store corporate recruitment entries, discarding unstable flat JSON or CSV layouts for relational tables.
* **Complete CRUD Matrix:** Features transactional integrity routines enabling users to seamlessly write, read, filter, or purge data rows safely with zero index collision.
* **Modern Dark-Mode Aesthetic:** Features a custom styled `ttk` widget frame environment optimized for high legibility and distraction-free data tracking.
* **Dynamic Time Sorting:** Automatically organizes active application records dynamically based on upcoming interview parameters using system clock verification arrays.
* **Zero Dependency Footprint:** Operates completely using core standard libraries, making it instantly portable and testable inside any basic python shell.

---

## 🛠️ Architecture & Tech Stack

* **Programming Core:** Python 3
* **Interface System:** Tkinter GUI Engine + Modernized TTK Component Mapping
* **Database Infrastructure:** SQLite3 Relational Engine (Serverless Local Storage)
* **Time Mechanics Layer:** Native `datetime` System Interface
* **Version Management:** Git Architecture

---

## 🚀 Getting Started

### Installation
This application runs entirely on native core standard frameworks. No external library downloads or database platform deployments are required.

### Initializing the Dashboard
1. Open your terminal engine inside your project directory folder:
```bash
python AppCore.py
```

## 🎮 Interface Architecture Reference

The application divides processing responsibilities across a dual-panel layout configuration:

| Interface Panel Component | Execution Target | Technical Operation |
| :--- | :--- | :--- |
| **Data Entry Panel (Left)** | User Submission System | Performs parameter safety validation checks before marshaling text arrays into SQL insert statements. |
| **Live Database Table (Right)** | Dynamic Treeview Grid | Pulls records from the local SQLite layer, re-indexing and rendering columns chronologically. |
