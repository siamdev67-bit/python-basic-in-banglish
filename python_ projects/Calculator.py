#operator select opsoin
operator = input("select an operator +,-,*,/, :")

#operator shothik ase kina dekhe 
if operator == "+" or operator == "-" or operator == "*" or operator == "/":
  
 #jodi operator shothik hoy ta holey porer numbere select opsoin asbe
  farst_num = int(input("..."))
  second_num = int(input("..."))
  
  #addison
  if operator == "+":
    print(f"anser is {farst_num + second_num}")
    
  #divison
  elif operator == "-":
    print(f"anser is {farst_num - second_num}")
    
  #maltificishon
  elif operator == "*":
    print(f"anser is {farst_num * second_num}")

    #jodi bhag korar somoy second_num e 0 dey taho ly you cant do that 0 ei messeg ash be ar jodi 0na thake ta ho ly anser dibe
  if second_num == 0 :
    print("you cant do that 0")
  else:
    print(f"anser is {farst_num / second_num}")

#ar jo di operator bhol dey taholy ei messeg ash be 
else:
  print("operator is rong")
    
  
