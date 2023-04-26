def password_to_asterix(password) -> str:
    output = len(password) * "*"
    return output


passk = input("Enter your password: ")
print(password_to_asterix(passk))

