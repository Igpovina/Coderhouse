from dataclasses import dataclass
from typing_extensions import Self

class User_data():
    def __init__(self, f_name, l_name, dob, passwd, ID):
        self.first_name = f_name
        self.last_name = l_name
        self.DOB = dob
        self.__password = passwd
        self.user_ID = ID
        
    # def _popualte(self):
    #     #complete fields


class User(User_data):
    def __init__(self, f_name, l_name, dob, passwd, ID):
        if  self.user_id ==  -1:
            self.new_user = True
        else:
            self.new_user = False
            super().__init__(f_name, l_name, dob, passwd, ID)

            
            
    def __populate():
        #Query self.user_id from database and
        #set all instance variables, e.g.
       pass

    def commit(self):
        if self.new_user:
            #Insert
            pass
        else:
            #update
            pass
        
    def delete(self):
        if not self.new_user:
            return False
        
    def getFullname(self):
        return self.first_name, " ", self.last_name
    
class admin(User_data):
    def __init__(self, f_name, l_name, dob, passwd, ID):
        super().__init__(f_name, l_name, dob, passwd, ID)
        

class Post():
    def __init__(self, txt):
        self.body = txt
    
    def submmit():
        pass
    
    def delete_post():
        pass