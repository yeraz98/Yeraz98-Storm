import os
import sys

def banner():
    os.system("clear")
    print("\033[1;91m YERAZ98 TOOL-KIT FRAMEWORK\033[0m")

def main():
    banner()
    print("\033[1;33m[1]\033[0m Kuzgun-Max (kuzgun.py)")
    print("\033[1;33m[2]\033[0m Serxan Project (serxan.py)")
    print("\033[1;33m[3]\033[0m Yeraz98 Ultra (yeraz98_ultra.py)")
    print("\033[1;33m[4]\033[0m Azrael Flood (azrael_flood.py)")
    print("\033[1;33m[5]\033[0m Yeraz98 Tool (yeraz98.py)")
    print("\033[1;31m[0]\033[0m Çıxış")
    
    choice = input("\nSeçim: ")
    
    if choice == "1": os.system("python kuzgun.py")
    elif choice == "2": os.system("python serxan.py")
    elif choice == "3": os.system("python yeraz98_ultra.py")
    elif choice == "4": os.system("python azrael_flood.py")
    elif choice == "5": os.system("python yeraz98.py")
    elif choice == "0": sys.exit()

if __name__ == "__main__":
    main()
