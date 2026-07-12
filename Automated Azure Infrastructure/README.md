# Automated Azure Infrastructure Deployer

A streamlined Infrastructure as Code (IaC) automation tool that combines **Python** and **Terraform** to provision a complete, secure cloud network and Linux virtual machine on Microsoft Azure. 

Instead of manually running separate infrastructure commands, the Python wrapper safely orchestrates the entire Terraform lifecycle (`init`, `plan`, `apply`) with real-time feedback and an explicit deployment safety confirmation.

---

## 🏗️ Architecture & Resources Provisioned

The Terraform configuration automatically builds out a standard, production-ready cloud architecture:

*   **Resource Group:** Acts as the logical container for all components (`automate-backup-rg`).
*   **Virtual Network (VNet):** Configured with a dedicated `10.0.0.0/16` address space.
*   **Subnet:** An internal subnet mapped to `10.0.1.0/24`.
*   **Public IP Address:** A static IP address allocated to allow external connectivity.
*   **Network Security Group (NSG):** Pre-configured with firewall rules for essential ports:
    *   `Port 22` (SSH)
    *   `Port 80` (HTTP)
    *   `Port 443` (HTTPS)
*   **Network Interface (NIC):** Links the VM to the subnet and attaches the Static Public IP and NSG.
*   **Linux Virtual Machine:** An Ubuntu Server 22.04 LTS instance (`Standard_B2ats`) provisioned with a 30 GB standard OS disk.

---

## 🛠️ Repository Structure

*   `main.py` - The Python script utilizing `subprocess` to manage the lifecycle workflow.
*   `main.tf` - Defines the Azure provider and the concrete infrastructure resource declarations.
*   `variables.tf` - Declares variables for easy configuration (e.g., setting the default region to Central India and the VM sizing).

---

## 🚀 How It Works (Code Analysis)

### 1. The Automation Wrapper (`main.py`)
The Python script handles execution flow and error management securely:
*   **Real-time Output:** Uses `subprocess.run()` to transparently stream Terraform console outputs straight to your screen.
*   **Error Interception:** If a phase (like initialization or planning) fails, the script catches the `CalledProcessError`, prints a clean error log, and exits gracefully before trying to deploy faulty code.
*   **Safety Checkpoint:** Halts execution right after the planning phase, prompting you for a mandatory `yes/no` confirmation before executing the final `-auto-approve` block.

### 2. Infrastructure as Code (`main.tf` & `variables.tf`)
*   **Providers:** Bound to the HashiCorp `azurerm` provider (`~> 4.0`).
*   **Security Context:** Explicitly associates the NSG directly to the network interface card via an association resource, keeping inbound traffic bounded tightly to explicit administrative ports.

---

## 📋 Prerequisites

Before running the script, ensure you have the following installed and configured on your machine:

1. [Python 3.x](https://www.python.org/)
2. [Terraform CLI](https://developer.hashicorp.com/terraform/downloads)
3. [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

Make sure you are authenticated to your Azure account in your terminal:
```bash
az login
