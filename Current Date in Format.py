from datetime import datetime

def program_4():
    now = datetime.now()
    print("Formatted date:", now.strftime("%a %b %d %H:%M:%S IST %Y"))

program_4()
