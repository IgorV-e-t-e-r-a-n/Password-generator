import random 
import string 


options = {
    'uppercase': input("Include uppercase letters? (yes/no): ").lower() == 'yes',
    'lowercase': input("Include lowercase letters? (yes/no): ").lower() == 'yes',
    'digits': input("Include digits? (yes/no): ").lower() == 'yes',
    'symbols': input("Include symbols? (yes/no): ").lower() == 'yes'
}
character_pool = ''.join(
    [string.ascii_uppercase if options['uppercase'] else '',
     string.ascii_lowercase if options['lowercase'] else '',
     string.digits if options['digits'] else '',
     string.punctuation if options['symbols'] else ''])

    


def generate_password(password_length=30):
    #define characters for password
    if not character_pool:
        raise ValueError("Password should include at least one type of characters")
            
    #generate a random password with defined characters
    password = ''.join(random.choice(character_pool) for i in range(password_length))
    #return the result
    return password

if __name__ == "__main__":
    
    password_length = int(input("Enter the desired length of a password: "))
    
    if password_length < 1:
        print("Password length must be longer")
    
    else:
        generated_password = generate_password(password_length)
        print("Generated password", generated_password)
        
        
        
        