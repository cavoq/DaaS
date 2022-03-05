def get_gmail_account_from_file(path: str):
     file = open(path, "r")
     account = file.readline()
     password = file.readline()
     return account, password
    
         