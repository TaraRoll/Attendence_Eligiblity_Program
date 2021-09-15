'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not'''

n = int(input("Enter classes held:"))
m = int(input("Enter classes attended:"))
per = (m/n)*100
print("Percent of class attended:",per,"%")
if(per>75):
  print("They can sit in the exam")
else:
  print("Student is denied from sitting in the exam")



