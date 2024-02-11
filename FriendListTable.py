import sys
import time
import phonenumbers
from rich import box
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.text import Text
from art import text2art

console = Console()
def phone_num_check(num):
    try:
        my_number = phonenumbers.parse(num)
        return phonenumbers.is_valid_number(my_number)
    except phonenumbers.NumberParseException:
        return False
    
def admin():
    console.clear()
    print("Good job, Your Admin, I tried to test a bit with arguments.")


def main():

    console.clear()
    ascii_art = """

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗    ████████╗ ██████╗     ███████╗      ██╗       ████████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗    ██╔════╝      ██║       ╚══██╔══╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║       ██║   ██║   ██║    █████╗        ██║          ██║   
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║       ██║   ██║   ██║    ██╔══╝        ██║          ██║   
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║       ██║   ╚██████╔╝    ██║      ██╗  ██║    ██╗   ██║   
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝       ╚═╝    ╚═════╝     ╚═╝      ╚═╝  ╚═╝    ╚═╝   ╚═╝   

    
    """
    aligned_ascii_art = Align.left(ascii_art)
    console.print(aligned_ascii_art)
    
    table = Table(show_header=True,header_style="Bold White",title="Friend Info Table",title_style="Bold Green", title_justify="left")
    aligned_table = Align.left(table)
    
    table.add_column("Name", style='bold violet')
    table.add_column("Age", style='bold green')
    table.add_column("Address", style='bold green')
    table.add_column("Phone Number", style='bold blue')
    table.add_column("Description", style='yellow')

    Name = input("Enter Name: ")
    if not Name.strip():
        console.print("Name cannot be empty.", style='bold red')
        time.sleep(3)
        main()
    elif any(char.isdigit() for char in Name):
        console.print("Name cannot contain digits.", style='bold red')
        time.sleep(3)
        main()
    Age = input("Enter Age: ")
    if not Age.strip():
        pass
    else:
        try:
            Age = float(Age)
            if Age <= 0:
                console.clear()
                console.print(f"(  {Age}  ) Is not a valid age", style='bold red')
                time.sleep(3)
                main()
        except ValueError:
            console.clear()
            console.print("Age must be a valid number.", style='bold red')
            time.sleep(3)
            main()

    Address = input("Enter Address: ")
        
    inputed_Phone_num = input("Enter Phone Number ( Ensure its in universal format like +972000000000 ): ")
    if not inputed_Phone_num.strip():
        pass
    else:
        if inputed_Phone_num[0] == '+':
            uni_Phone_num = inputed_Phone_num
        else:
            uni_Phone_num = "+972" + inputed_Phone_num[1:]

        if not phone_num_check(uni_Phone_num):
            console.clear()
            console.print("THE PHONE NUMBER YOU ENTERED WAS INVALID", style='bold red')
            time.sleep(3)
            main()

    Description = input("Enter Description: ")
    
    phone_num = "0" + uni_Phone_num[4:]
    table.add_row(Name, Age, Address, phone_num, Description)
    
    
    console.print('\n\n')
    console.print(aligned_table)

if __name__ == "__main__":

    if "--admin" in sys.argv:
        admin()
    else:
        main()
