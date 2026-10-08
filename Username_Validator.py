user_name = input("User Name :").strip()

if len(user_name) >= 3 and user_name.lower().startswith("s"):
  print(f"username : {user_name}")
  print("valid username")
else:
  print(f"username : {user_name}")
  print("invaled user_name")