# Open the file and read the lines
with open("currencydata.txt") as f:
    lines = f.readlines()

# Create a dictionary to store currency data
currency_dict = {}
for line in lines:
    parsed = line.strip().split("\t")
    currency_dict[parsed[0]] = float(parsed[1])  # Convert exchange rate to float

# Get user input
amount = int(input("Enter an amount in INR: "))
currency = input("Enter the name of the currency you want to convert this amount to: ")

# Perform the conversion
if currency in currency_dict:
    converted_amount = amount * currency_dict[currency]
    print(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
else:
    print(f"Sorry, the currency '{currency}' is not available in the data.")
