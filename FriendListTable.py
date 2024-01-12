import sys
import phonenumbers
import os
from rich.table import Table
from rich.console import Console

def clear_console():
    os.system("cls")

def admin():
    clear_console()
    print("Good job, Your Admin, I tried to test a bit with arguments.")

def phone_num_check(num):
    try:
        my_number = phonenumbers.parse(num)
        return phonenumbers.is_valid_number(my_number)
    except phonenumbers.NumberParseException:
        return False

    
def main():
    console = Console()

    clear_console()
    table = Table(show_header=True,header_style="Bold White",title="Friend Info Table",title_style="Bold Green")
    table.add_column("Name", )
    table.add_column("Age")
    table.add_column("Address")
    table.add_column("Phone Number")
    table.add_column("Description")

    Name = input("Enter Name: ")
    Age = int(input("Enter Age: "))
    
    if Age <= 0:
        clear_console()
        print(f"(  {Age}  ) Is not a valid age")
        exit()
    
    Address = input("Enter Address: ")
    Phone_num = input("Enter Phone Number ( Ensure its in universal format like +972000000000 ): ")

    if phone_num_check(Phone_num):
        Description = str(input("Enter Description: "))
    
    else:
        clear_console()
        print("The phone number you entered isn't valid")
        exit()

    table.add_row(Name, str(Age), Address, Phone_num, Description)
    
    clear_console()
    console.print(table)


if __name__ == "__main__":
    if "--admin" in sys.argv:
        admin()
    else:
        main()
    