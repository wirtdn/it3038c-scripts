import time

start_time = time.time()

print('What is your name?')
myName = input()
print('Hello, ' + myName + '. That is a good name. How old are you?')
myAge = int(input())
programAge = int(time.time() - start_time)
print("%s? That's funny, I'm %s seconds old." % (myAge, programAge))
print("I wish I was " + str(int(myAge) * 2) + " years old. Then I would be twice your age HaHa!")

time.sleep(3)
print("I'm tired. I go sleep sleep now.") 
