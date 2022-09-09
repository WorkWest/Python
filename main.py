username = ""

def greeting(username): 
  print(f"Welcome {username}")

def username_validation():
  while True:
    username = input("What is your username: ")
    if len(username) > 0:
      greeting(username)
      break
    else:
      print("Try again")