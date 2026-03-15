print("Simple Calculator")
num1=float(input("Enter 1st number"))
num2=float(input("Enter 2nd number"))
print("different hunk?")
print("Choose operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("enter choice")
if choice == "1":
	print("Result:",num1+num2)
elif choice == "2":
	print("Result:",num1-num2)
elif choice == "3":
	print("Result:" ,num1*num2)
elif choice == "4":
	if num2!=0:
		print("Result:",num1/num2)
	else:
		print("Error : Division by zero")
else:
	print("Invalid choice")
print("adding local branch : local-feature")
print("this is first test")
print("adding this new line for Github branch and local branch commit changes not visible")
print("this is the next test")
