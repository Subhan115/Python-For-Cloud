import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

def run_backup_wizard():
    # 1. Verify Authentication
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    if not connect_str:
        print("[ERROR] AZURE_STORAGE_CONNECTION_STRING environment variable is missing!")
        return
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    print("=== 🛠️ AZURE INTERACTIVE BACKUP WIZARD ===")
    
    # 2. Get the target file location
    while True:
        file_path = input("\nEnter the full path of the file to backup: ").strip()
        if os.path.isfile(file_path):
            break
        print("[ERROR] File not found. Please enter a valid file path.")
    
    file_name = os.path.basename(file_path)

    # 3. Handle Container Selection or Creation
    print("\nFetching your current Azure Containers...")
    try:
        containers = list(blob_service_client.list_containers())
    except Exception as e:
        print(f"[ERROR] Could not fetch containers: {e}")
        return

    print("\nAvailable Containers:")
    if containers:
        for idx, container in enumerate(containers, 1):
            print(f" [{idx}] {container.name}")
    else:
        print(" (No containers found in this storage account)")

    print(" [N] Create a brand NEW container")
    
    choice = input("\nSelect a number or type 'N' for a new container: ").strip().lower()

    # 4. Process the user's choice
    if choice == 'n' or not containers:
        while True:
            new_name = input("Enter a name for your new container (lowercase, numbers, hyphens only): ").strip().lower()
            try:
                print(f"Creating container '{new_name}'...")
                container_client = blob_service_client.create_container(new_name)
                selected_container_name = new_name
                print("[SUCCESS] New container created!")
                break
            except ResourceExistsError:
                print("[INFO] That container already exists. Let's use it.")
                selected_container_name = new_name
                break
            except Exception as e:
                print(f"[ERROR] Invalid name or choice: {e}. Try again.")
    else:
        try:
            selection_idx = int(choice) - 1
            if 0 <= selection_idx < len(containers):
                selected_container_name = containers[selection_idx].name
            else:
                print("[ERROR] Invalid selection. Defaulting to first container.")
                selected_container_name = containers[0].name
        except ValueError:
            print("[ERROR] Invalid input. Defaulting to first container.")
            selected_container_name = containers[0].name

    # 5. Direct Stream Upload (No local copy made!)
    print(f"\nStreaming '{file_name}' directly to Azure container '{selected_container_name}'...")
    
    try:
        blob_client = blob_service_client.get_blob_client(container=selected_container_name, blob=file_name)
        
        # Opening the file locally and pushing its stream directly to the cloud
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
        print(f"\n🎉 [SUCCESS] Backup complete! '{file_name}' is safely stored in the cloud.")
    except Exception as e:
        print(f"\n[ERROR] Upload failed: {e}")

if __name__ == "__main__":
    run_backup_wizard()
