#The welcoming line of the Smart Calculator.
response=['Welcome to Smart Calculator!','Devan is my name.', 
          'Thanks for using me! ','Sorry ,this is  beyond my ability.'] 
  
# fetching tokens from the text command 
def extract_from_text(text): 
    l=[] 
    for t in text.split(' '): 
        try: 
            l.append(float(t)) 
        except ValueError: 
            pass
    return l 
  
# calculating LCM (Least Common Multiple)
def lcm(a,b): 
    L=a if a>b else b 
    while L<=a*b: 
        if L%a==0 and L%b==0: 
            return L 
        L+=1
  
# calculating HCF (Highest Common Factor)
def hcf(a,b): 
    H=a if a<b else b 
    while H>=1: 
        if a%H==0 and b%H==0: 
            return H 
        H-=1
  
# Addition function
def add(a,b): 
    return a+b 
  
# Subtraction function
def sub(a,b): 
    return a-b 
  
# Multiplication function
def mul(a,b): 
    return a*b 
  
# Division function
def div(a,b): 
    return a/b 
  
# Remainder function
def mod(a,b): 
    return a%b 
  
# Response to command 
# printing - "Thanks for using me" on exit 
def end(): 
    print(response[2]) 
    input('press enter key to exit') 
    exit() 
   
def myname(): 
    print(response[1]) 
def sorry(): 
    print(response[3]) 
   
# Operations that are defined by the users input that tell the calculator what funtion to run. 
operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add, 
            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub, 
            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf, 
            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul, 
            'DIVISION':div,'MOD':mod,'REMANDER'
            :mod,'MODULAS':mod} 
  
# commands that can show the calculators nane, and three ways to exit the calculator.
commands={'NAME':myname,'EXIT':end,'END':end,'CLOSE':end} 
           
print('--------------'+response[0]+'------------') 
print('--------------'+response[1]+'--------------------') 
   
#The Calculator asks the user to type out what function they want performed and displays an error if the criteria is not met.   
while True: 
    print() 
    text=input('Enter your queries:  ') 
    for word in text.split(' '): 
        if word.upper() in operations.keys(): 
            try: 
                l = extract_from_text(text) 
                r = operations[word.upper()] (l[0],l[1]) 
                print(r) 
            except: 
                print('something went wrong going plz enter again !!') 
            finally: 
                      break
        elif word.upper() in commands.keys(): 
                      commands[word.upper()]() 
                      break
    else:          
        sorry() 
 
