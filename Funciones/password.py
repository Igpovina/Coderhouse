def validate_password(password):
    SpecialSym =['$', '@', '#', '%', '*']
    val = True
      
    if len(password) < 8:
        print('length should be at least 8')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
        
# print(validate_password("123321lA#"))