def program_9():
    choice = input("Convert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius? Enter 1 or 2: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Invalid choice")

program_9()
