first_name = input("what is your first name? ")
last_name = input ("What is your last name? ")

if len(first_name) <= 2:
    print("Add more characters for a complete name. ")
else:
    print(f"hello {first_name}, how is the {last_name} family doing")

