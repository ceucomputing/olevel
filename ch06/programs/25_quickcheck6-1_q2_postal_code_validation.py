# Input and input validation
while True:
    postal_code = input("Enter postal code: ")
    if postal_code.isdigit() and len(postal_code) == 6:
        break
    print("Data validation failed!")
    print("Postal code should be exactly 6 digits")
