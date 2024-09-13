# Fox, chicken, grain program

#Main
print("A fox, chicken and a bag of grain wait by the side of a river.")
fox = 0
chicken = 0
grain = 0
farmer = 0
choice = input("Which item will you take in your rowboat to the other side? fox, chicken, grain or farmer? Choose:")
print("------------------------")
if choice == "farmer" and farmer == 0:
    farmer = farmer + 1
elif choice == "fox" and farmer == 0 and fox == 0:
    farmer = farmer + 1
    fox = fox + 1
elif choice == "chicken" and farmer == 0 and chicken == 0:
  farmer = farmer + 1
  chicken = chicken + 1
elif choice == "grain" and farmer == 0 and grain == 0:
  grain = grain + 1
  farmer = farmer + 1
else: 
  print("Try again")
