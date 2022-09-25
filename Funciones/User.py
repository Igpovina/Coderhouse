from dataclasses import dataclass
from typing_extensions import Self

class User_data():
    def __init__(self, f_name, l_name, dob, passwd, ID):
        self.first_name = f_name
        self.last_name = l_name
        self.DOB = dob
        self.password = passwd
        self.user_ID = ID
        
    # def _popualte(self):
    #     #complete fields


class User(User_data):
    def __init__(self, User_data):
        if  User_data.user_id ==  -1:
            self.new_user = True
        else:
            self.new_user = False

            self._populate()
            
    def _populate(self):
        #Query self.user_id from database and
        #set all instance variables, e.g.
        self.first_name = User_data.first_name
        self.last_name = User_data.last_name
        self.DOB = User_data.DOB
        self.password = User_data.password

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
    
class admin():
    pass

class Post():
    def __init__(self, txt):
        body = txt
    
    def submmit():
        pass
    
    def delete_post():
        pass