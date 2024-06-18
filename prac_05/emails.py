name_to_email = {}

email = input("Email: ")
while email != "":
    index_of_at = email.find("@")
    index_of_dot = email.find(".")
    if index_of_dot < index_of_at:
        name = email[:index_of_dot].title() + " " + email[index_of_dot+1:index_of_at].title()
    else:
        name = email[:index_of_at].title()
    correct_name = input(f"Is your name {name}? ").upper()
    if correct_name != "Y" and correct_name != "YES" and correct_name != "":
        name = input("Name: ").title()
    name_to_email[name] = email
    email = input("Email: ")
for name, email in name_to_email.items():
    print(f"{name} ({email})")
