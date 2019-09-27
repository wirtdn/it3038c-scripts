import time

start_time = time.time()

#print('What is your name?')
#myName = input()

while True:
  print("Please type your name.")
  myName = input()
  if myName =='Devan':
    break
print("Thank you")

#while myName != 'Devan':
#  if myName == 'yourname':
#    print('Ha ha, very funny. Seriously, who are you?')
#  else: 
#    print('This is not your name!')
#    myName = input()
print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())
programAge = int(time.time() - start_time)

if myAge < 13:
  print('Are you legeally allowed to use this app?')
elif myAge ==13:
  print("You're a teenager now... that's cool, i guess")
elif myAge > 13 and myAge <30:
  print("These are prime days. Enjoy them")
elif myAge >= 30 and myAge < 65:
  print("It's all downhill from here")
else:
  print("... and you're not dead yet?")

time.sleep(1)
print("%s? That's funny, I'm %s seconds old." % (myAge, programAge))
print("I wish I was " + str(int(myAge) * 2) + " years old. Then I would be twice your age HaHa!")

time.sleep(3)
print("I'm tired. I go sleep sleep now.") 
