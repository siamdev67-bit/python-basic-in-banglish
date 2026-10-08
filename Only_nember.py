while True :
  try:
    num = int(input("namber :"))
    if num >= 1 and num <=50:
      print(f"Valid number: {num}")
      break
    else:
      print("Number must be between 1 and 50")
  except ValueError:
    print("Only numbers are allowed")
      