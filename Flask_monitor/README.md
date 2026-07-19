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
| **Async Logic** | JavaScript (Fetch API) | Polls the backend API # 📊 Linux Real-Time System Monitor

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
```

---

## 🔧 Installation & Local Setup

Follow these steps to set up and run the project inside an isolated virtual environment on your Linux machine or cloud VM.

### 1. Clone or Create the Project Directory
```bash
mkdir flask_monitor && cd flask_monitor
```

### 2. Set Up a Virtual Environment
Initialize a clean Python environment to keep system dependencies isolated:
```bash
python3 -m venv .venv
```
*(Note: If you run into errors on Ubuntu/Debian, install the core package using `sudo apt install python3-venv`)*

### 3. Activate the Environment
```bash
source .venv/bin/activate
```
*(Your terminal prompt should now show `(.venv)` at the beginning)*

### 4. Install Dependencies
```bash
pip install Flask psutil
```

---

## ⚡ How to Run

### Development Mode (Default Local Port 5000)
To run locally or test via an SSH tunnel:
```bash
python app.py
```
Access the application at: `http://localhost:5000`

### Production/Cloud Mode (Public HTTP Port 80)
If deploying on a cloud platform (like Azure) with HTTP routing enabled, update the execution port to `80` in `app.py`. Because Linux restricts ports under 1024, execute the application using your virtual environment's explicit Python binary with `sudo`:
```bash
sudo .venv/bin/python app.py
```
Access the application globally via your server's Public IP: `http://your_server_public_ip`

---

## 🧠 How it Works: Architecture Breakdown

```text
[ Browser Client ]  ---( Every 2s /api/metrics )--->  [ Flask Backend ]
       ^                                                     |
       |                                              Reads /proc file system
       +------------( Returns Live JSON Data )---------------+       |
                                                             v
                                                      [ Linux Kernel ]
```

1. **The Backend API:** The Flask server exposes an asynchronous API endpoint at `/api/metrics`. When pinged, it triggers `psutil.cpu_percent(interval=None)` which instantaneously calculates CPU load delta since the last check without pausing execution.
2. **The Frontend Loop:** The browser loads the initial HTML structure. A JavaScript background loop governed by `setInterval()` fires a browser `fetch()` block to the backend every 2000 milliseconds. 
3. **Dynamic Rendering:** Once JSON data returns, JavaScript dynamically recalculates the document structure, shifting CSS width properties to animate the structural tracking bars dynamically.

---

## 🔒 Security Notes for Production
* **Do not use debug mode in public deployments:** Ensure `debug=True` is turned off if exposed broadly to the internet.
* **Production WSGI:** For scaled deployments, run the Flask app inside a production WSGI server like **Gunicorn** reverse-proxied behind **Nginx**.
*  in the background. |

---

## 📂 Project Structure

```text
flask_monitor/
│
├── .venv/                 # Python Isolated Virtual Environment
├── app.py                 # Core Flask application and API routes
└── templates/
    └── index.html         # Dashboard UI and asynchronous frontend logic
