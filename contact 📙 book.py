# Initialize empty lists to store contact names and numbers
names = []
contact_numbers = []

# Get the total number of contacts from the user
num = int(input("Enter the total number of contacts you want to save: "))

# Collect contact details from the user
for i in range(num):
    name = input("Name: ")
    contact_number = int(input("Contact Number: "))
    names.append(name)
    contact_numbers.append(contact_number)

# Display the saved contacts
print("\nName\t\tContact Number")
for i in range(num):
    print(f"{names[i]}\t\t{contact_numbers[i]}")

# Search for a contact
search_term = input("\nEnter search term: ")
print("Search result:")
if search_term in names:
    index = names.index(search_term)
    contact_number = contact_numbers[index]
    print(f"Name: {search_term}, Phone Number: {contact_number}")
else:
    print("No records")




