#Tip Calculator in Python
#start
print('Welcome! to the Python Tip Calculator')

#ask user what the total bill is
bill = input('What is the total bill?: $')

#ask for tip
tip = input('how many tip do you want to pay?: ')
new_tip = float(tip)/100

#ask how many people will be pay together
person = int(input('how many people will be paying?: '))

#calculate and print total bill that each person will be paying.
total_bill = float(bill) + new_tip
bill_per_person = total_bill/person

#print and round
print(f'Each person has to pay: ${round(bill_per_person)}.')

#stop
