import subprocess

def install_dependencies():
    try:
        # Update the system packages
        subprocess.check_call(["sudo", "apt", "update"])
        
        # Install required system dependencies
        subprocess.check_call([
            "sudo", "apt", "install", "-y",
            "cmake", "g++", "make", "libopenblas-dev", "libx11-dev", "libgtk-3-dev"
        ])

        print("System dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")

