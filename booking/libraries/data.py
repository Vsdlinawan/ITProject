class User:
    def __init__(self):
        self.is_logged_in = False
        self.current_user = None
    
    def login(self):
        self.is_logged_in = True
    
    def logout(self):
        self.is_logged_in = False
    
    def getLogin(self):
        return self.is_logged_in