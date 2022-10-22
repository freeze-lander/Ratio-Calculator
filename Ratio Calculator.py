print("-----------------------------------------------------")
print("         Hi, Wellcome to Ratio Calculator")
print("                Created By Yovid")
print("-----------------------------------------------------")
one = input('Input 1st name:')
two = input('Input 2nd name:')
print("-----------------------------------------------------")
print("Input only numbers")
print('What is',one,"'s ratio")
ratio1= int (input('Ratio:'))
print('What is',two,"'s ratio")
ratio2= int (input('Ratio:'))
print("-----------------------------------------------------")
print("Tell the total items")
tt= int (input('total:'))
print("-----------------------------------------------------")
print("Answers")
print('Total parts:',ratio1+ratio2)
print('One part =',tt/(ratio1+ratio2))
print(one,"'s parts = ",tt/(ratio1+ratio2)*ratio1 )
print(two,"'s parts = ",tt/(ratio1+ratio2)*ratio2)
print("-----------------------------------------------------")
input('Enter to Stop')








