import subprocess
import sys

def run_terraform_command(command_list, description):
    """Utility function to run a system command safely with real-time output."""
    print(f"\n🚀 Running: {description}...")
    try:
        # Run the command and pipe output directly to the terminal screen
        subprocess.run(command_list, text=True, check=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ [ERROR] {description} failed.", file=sys.stderr)
        return False

def main():
    print("=== 🛠️ AUTOMATED AZURE INFRASTRUCTURE DEPLOYER ===")

    # 1. Initialize Terraform (downloads the Azure provider plugins)
    if not run_terraform_command(["terraform", "init"], "Terraform Initialization"):
        sys.exit(1)

    # 2. Plan out the changes (shows you a blueprint of what will be created)
    if not run_terraform_command(["terraform", "plan"], "Terraform Planning"):
        sys.exit(1)

    # 3. Request user confirmation before building anything in Azure
    confirm = input("\n⚠️ Ready to build the infrastructure in Azure? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        # -auto-approve tells terraform to execute without asking for its own secondary prompt
        if run_terraform_command(["terraform", "apply", "-auto-approve"], "Terraform Apply"):
            print("\n🎉 Infrastructure successfully deployed to Azure (Central India)!")
        else:
            sys.exit(1)
    else:
        print("\n🛑 Deployment cancelled by user.")

if __name__ == "__main__":
    main()
