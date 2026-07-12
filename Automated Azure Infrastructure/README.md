# Automated Azure Infrastructure Deployer

An automated, portable cloud infrastructure deployment tool that utilizes a Python wrapper script to orchestrate, validate, and provision a secure Linux environment on Azure via Terraform[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span).

---

## 🚀 Features

* **Automated Sequential Execution**: Automatically executes `terraform init`, `terraform plan`, and `terraform apply` within a unified script workflow[span_2](start_span)[span_2](end_span).
* **Interactive Guardrails**: Implements a manual confirmation prompt following the planning phase to prevent accidental cloud deployments[span_3](start_span)[span_3](end_span).
* **Real-Time Output Streaming**: Leverages Python's `subprocess` system to pipe stdout directly to your console while handling execution errors gracefully[span_4](start_span)[span_4](end_span).
* **Decoupled Architecture**: Utilizes localized variables for region and instance definitions to maximize code portability across distinct Azure tenants[span_5](start_span)[span_5](end_span).

---

## 🏗️ Architecture Components

The underlying Terraform script builds a fully integrated, functional network and compute layer following a precise configuration sequence:

* **1. Resource Group**: Allocates the logical management container `automate-backup-rg` to bound all resources within a target region[span_6](start_span)[span_6](end_span).
* **2. Virtual Network**: Establishes `automate-vnet` using a private `10.0.0.0/16` address space block[span_7](start_span)[span_7](end_span).
* **3. Subnet**: carves out a dedicated internal network slice (`10.0.1.0/24`) inside the parent Virtual Network framework[span_8](start_span)[span_8](end_span).
* **4. Public IP**: Allocates a static public IP endpoint named `automate-vm-ip` to ensure persistent external entry points[span_9](start_span)[span_9](end_span).
* **5. Network Security Group (NSG)**: Deploys the firewall baseline `allow_user_to_connect`, explicitly opening inbound access paths for Port 22 (SSH), Port 80 (HTTP), and Port 443 (HTTPS)[span_10](start_span)[span_10](end_span).
* **6. Network Interface Card (NIC)**: Provisions `automate-vm-nic` to couple dynamic internal subnets directly with the static public IP route[span_11](start_span)[span_11](end_span).
* **7. NSG Association**: Formally binds the firewall rule structures of the NSG directly onto the virtual network interface card[span_12](start_span)[span_12](end_span).
* **8. Linux Virtual Machine**: Deploys an Ubuntu 22.04 LTS compute instance running on standard block storage with configured password credentials[span_13](start_span)[span_13](end_span).

---

## ⚙️ Configuration & Variables

Modify the input variables within `variables.tf` to repurpose this codebase for alternative application environments[span_14](start_span)[span_14](end_span):

| Variable Name | Description | Default Value |
|---|---|---|
| `azure_location` | Target Azure region deployment context for all system resources[span_15](start_span)[span_15](end_span) | `"centralindia"`[span_16](start_span)[span_16](end_span) |
| `vm_size` | The cloud computation hardware footprint tier assigned to the instance[span_17](start_span)[span_17](end_span) | `"Standard_B2ats"`[span_18](start_span)[span_18](end_span) |

---

## 🛠️ Prerequisites

* **Python 3.x Engine** installed locally on the host machine[span_19](start_span)[span_19](end_span).
* **Terraform CLI Binary** installed (Azure Provider version constraints configured to `~> 4.0`)[span_20](start_span)[span_20](end_span).
* **Azure CLI Tool** installed and authenticated via shell context (`az login`).

---

## 💻 How To Run

1. Clone this repository structure directly to your local development workspace.
2. Open your system terminal environment and log into your Azure CLI account module.
3. Launch the automated deployment manager script:
   ```bash
   python main.py
4. Evaluate the structural planning dry-run printout displayed right inside your shell window.
5. Type yes when prompted by the wrapper application to securely compile your live cloud topology.
