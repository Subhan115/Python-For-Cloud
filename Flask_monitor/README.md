# 📊 Linux Real-Time System Monitor

A lightweight, high-performance web dashboard built with **Flask** and **Vanilla JavaScript** to monitor Linux server CPU and RAM utilization in real-time. Designed to run efficiently with a minimal footprint, making it ideal for tracking metrics on cloud instances like Azure VMs.

---

## 🚀 Features
* **Real-Time Tracking:** Asynchronous metric updates every 2 seconds without page refreshes.
* **Smooth UI:** Modern dark-mode dashboard featuring fluid CSS transition progress bars.
* **Lightweight Backend:** Leverages `psutil` to sample kernel metrics directly without blocking the application thread.
* **Network Flexible:** Configured to bind to all network interfaces (`0.0.0.0`) for seamless remote cloud access.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3 / Flask | Handles routing and serves the metrics API endpoint. |
| **System Metrics** | `psutil` | Interfaces with Linux `/proc` system files for hardware data. |
| **Frontend** | HTML5 / CSS3 | Renders the clean, responsive dark-themed dashboard. |
| **Async Logic** | JavaScript (Fetch API) | Polls the backend API seamlessly in the background. |

---

## 📂 Project Structure

```text
flask_monitor/
│
├── .venv/                 # Python Isolated Virtual Environment
├── app.py                 # Core Flask application and API routes
└── templates/
    └── index.html         # Dashboard UI and asynchronous frontend logic
