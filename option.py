def choose_option():
    while True:
        try:
            option = int(input("\nChoose Option: "))
            return option
          # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")
