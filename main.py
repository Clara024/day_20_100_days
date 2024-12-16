print ("List Generator")

#Get user input
start = int(input("What number do you wish to start from?:"))
end = int(input("What number do you wish to end before?:"))
increase = int(input("What is the increament value?:"))

for digit in range(start, end, increase):
  print (digit)
  print()