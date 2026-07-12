variable "azure_location" {
  description = "Azure region where resources will be provisioned"
  type        = string
  default     = "centralindia"
}

variable "vm_size" {
  description = "Free tier eligible size for the Azure Virtual Machine"
  type        = string
  default     = "Standard_B2ats"
}
