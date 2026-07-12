‎# Automated Azure Infrastructure Deployer
‎
‎An automated, portable cloud infrastructure deployment tool that utilizes a Python wrapper script to orchestrate, validate, and provision a secure Linux environment on Azure via Terraform.
‎
‎---
‎
‎## 🚀 Features
‎
‎* **Automated Sequential Execution**: Automatically executes `terraform init`, `terraform plan`, and `terraform apply` within a unified script workflow.
‎* **Interactive Guardrails**: Implements a manual confirmation prompt following the planning phase to prevent accidental cloud deployments.
‎* **Real-Time Output Streaming**: Leverages Python's `subprocess` system to pipe stdout directly to your console while handling execution errors gracefully.
‎* **Decoupled Architecture**: Utilizes localized variables for region and instance definitions to maximize code portability across distinct Azure tenants.
‎---
‎
‎## 🏗️ Architecture Components
‎
‎The underlying Terraform script builds a fully integrated, functional network and compute layer following a precise configuration sequence:
‎
‎* **1. Resource Group**: Allocates the logical management container `automate-backup-rg` to bound all resources within a target region.
‎* **2. Virtual Network**: Establishes `automate-vnet` using a private `10.0.0.0/16` address space block.
‎* **3. Subnet**: carves out a dedicated internal network slice (`10.0.1.0/24`) inside the parent Virtual Network framework.
‎* **4. Public IP**: Allocates a static public IP endpoint named `automate-vm-ip` to ensure persistent external entry points.
‎* **5. Network Security Group (NSG)**: Deploys the firewall baseline `allow_user_to_connect`, explicitly opening inbound access paths for Port 22 (SSH), Port 80 (HTTP), and Port 443 (HTTPS).
‎* **6. Network Interface Card (NIC)**: Provisions `automate-vm-nic` to couple dynamic internal subnets directly with the static public IP route.
‎* **7. NSG Association**: Formally binds the firewall rule structures of the NSG directly onto the virtual network interface card.
‎* **8. Linux Virtual Machine**: Deploys an Ubuntu 22.04 LTS compute instance running on standard block storage with configured password credentials.
‎
‎---
‎
‎## ⚙️ Configuration & Variables
‎
‎Modify the input variables within `variables.tf` to repurpose this codebase for alternative application environments:
‎
‎| Variable Name | Description | Default Value |
‎|---|---|---|
‎| `azure_location` | Target Azure region deployment context for all system resources | `"centralindia"`[span_16](start_span)[span_16](end_span) |
‎| `vm_size` | The cloud computation hardware footprint tier assigned to the instance | `"Standard_B2ats"` |
‎
‎---
‎
‎## 🛠️ Prerequisites
‎
‎* **Python 3.x Engine** installed locally on the host machine.
‎* **Terraform CLI Binary** installed (Azure Provider version constraints configured to `~> 4.0`).
‎* **Azure CLI Tool** installed and authenticated via shell context (`az login`).
‎
‎---
‎
‎## 💻 How To Run
‎
‎1. Clone this repository structure directly to your local development workspace.
‎2. Open your system terminal environment and log into your Azure CLI account module.
‎3. Launch the automated deployment manager script:
‎   ```bash
‎   python main.py
‎4. Evaluate the structural planning dry-run printout displayed right inside your shell window.
‎5. Type yes when prompted by the wrapper application to securely compile your live cloud topology.
