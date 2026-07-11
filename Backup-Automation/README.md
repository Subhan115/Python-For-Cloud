# 🛠️ Azure Interactive Backup Wizard

A lightweight Python CLI tool to stream local files directly to Azure Blob Storage via an interactive command-line wizard.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Azure](https://img.shields.io/badge/azure-blob--storage-007FFF.svg)

---

## 📋 Prerequisites

* **Python 3.7+**
* An **Azure Storage Account** and its **Connection String** *(found under 'Access keys' in the Azure Portal)*.

---

## ⚙️ Setup & Installation

1. **Install required packages:**
   ```bash
   pip install azure-storage-blob azure-core azure-identity
   ```

2. **Set your Azure Connection String:**
   
   * **Linux/macOS:**
     ```bash
     export AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
     ```
   * **Windows (CMD):**
     ```cmd
     set AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
     ```
   * **Windows (PowerShell):**
     ```powershell
     $env:AZURE_STORAGE_CONNECTION_STRING="your_connection_string_here"
     ```

---

## 🎯 Usage

Run the script and follow the step-by-step interactive prompts:

```bash
python backup_wizard.py
```

### 🧠 How it Works
1. **Validates** your local file path.
2. **Fetches** available Azure containers (or lets you create a new one on the fly).
3. **Streams** the file directly to the cloud to prevent duplicating data or exhausting local memory.

---
 
