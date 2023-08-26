import os
import sys
import pwd
import subprocess


while True:
    print("Menu:")
    print("1. Make yourself Root")
    print("2. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        # Disable security settings
        os.system("sudo sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config")
        os.system("sudo service ssh restart")
        
        # Log in as root without password
        os.system("sudo su")
        
        # Check if login was successful
        if os.getuid() == 0:
            print("SUCCESS!")
        else:
            print("Failed")
    elif choice == "2":
        sys.exit
    else:
        print("Invalid choice. Please try again.")
