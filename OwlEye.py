
print("""
                                                  
                                                  
                                      
                 
                              
                              ......              
            ,;;;'.     ...';;::loooc,..           
           ;:clcc;,,;:clddxxxollodxxol:.          
           ':looolllodkOOOOko:;,;:lxxol;.         
            .codxdxkOO00kxl,.   .':oxdl:.         
             .codxO0KK0x:,.    .;codxdl,.         
              'lox0KKKx;....';coxkOkdoc'.         
              .cokKXX0x:'.,oxkOkO0Oxl:,.          
             ..cdOKKKKOo:;oO0KKK0Odl:'.           
             .'ldOKXXK0xodkO0K00Oxol;.            
             .,loxKXXK0O000000Okddo:.             
              'cook0KOO0KKK00Okxdl,.              
              ' :cxOOxxOOO00Okdoc..               
                ':oxxdxkOOOkxo:'.                 
                 ';lodkkxxoc,.                    
                    ,;;'...                       
                                                  
                                                       
                                                      OwlEye""")
print("                                            Made by VioletCarson   v1.0.0")                                    
print("")
print("")
activeid = []
starttest = input("Enable Test Password? [y/n]: ")
if starttest == "y":
    testcode = input("insert test password: ")

comb = len(activeid)
firstname = input(" >Target's first name: ")
if firstname != "":
    comb += 1
lastname = input(" >Target's last name: ")
if lastname != "":
    comb += 1
nickname = input(" >Target's nickname: ")
if nickname != "":
    comb += 1
phone = input(" >Target's phone number: ")
if phone != "":
    comb += 1
birthday = input(" >Target's birthday: ")
if birthday != "":
    comb += 1
pet = input(" >Target's pet: ")
if pet != "":
    comb += 1
animal = input(" >Target's favourite animal: ")
if animal != "":
    comb += 1
color = input(" >Target's favourite color: ")
if color != "":
    comb += 1
sports = input(" >Target's favourite team: ")
if sports != "":
    comb += 1
Mbirth = input(" >Target's mother's birthday: ")
if Mbirth != "":
    comb += 1
Dbirth = input(" >Target's father's birthday: ")
if Dbirth != "":
    comb += 1
Numbers = input(" >add common numbers? [y/n]: ")
if Numbers == "y":
    comb += 4
print(" add keywords for the target:")
keyword1 = input(" >")
if keyword1 != "":
    comb += 1
keyword2 = input(" >")
if keyword2 != "":
    comb += 1
keyword3 = input(" >")
if keyword3 != "":
    comb += 1
if firstname != "" and lastname != "" :
    advanced1 = firstname[0] 
    advanced2 = lastname[0]
    advanced3 = firstname[0]+lastname[0]
    comb += 3


launch = input("press enter")
if Numbers == 'y':
   satan = "666"
   dirty = "69"
   dumb1 = "1234"
   dumb2 = "123"
   dumb3 = "234"
   ID = [advanced1,advanced2,advanced3,firstname,lastname,nickname,pet,birthday,animal,color,sports,Mbirth,Dbirth,keyword1,keyword2,keyword3,satan,dirty,dumb1,dumb2,dumb3]
else:
   ID = [advanced1,advanced2,advanced3,firstname,lastname,nickname,pet,birthday,animal,color,sports,Mbirth,Dbirth,keyword1,keyword2,keyword3]
import time
import random
Power = [0,1]
position = [1,2,3]

wordlist = []
progressl = []

combinations = 2*((comb)*(comb - 1)) + 5*((comb)*(comb - 1)*(comb - 2))
if combinations < 1000:
     combinations = 5000


import sys


                        #two variables password generator with dash
for x in range (-combinations, combinations):
      progress = round((len(wordlist)/combinations)*100)
      progressl.append(progress)
      
      if progress not in progressl:
        print("Progress =", round((len(wordlist)/combinations)*100),"%")
     

      wordlist = list(dict.fromkeys(wordlist))  
      x = len(wordlist)
      underscore = (random.choice(Power))
      var1 = (random.choice(ID))
      var2 = (random.choice(ID))
       
      if var1 == var2:
          x = x
      
      else:
       
          if underscore < 1:
                 Password = (var1 + var2)
                 if Password == "":
                       x = x
                 else:
                                   
                       x = x + 1
                       wordlist.append(Password)
                            
          else:
                     Password = (var1 + "_" + var2)
                     if Password == "_" :
                        x = x
                     elif Password in wordlist:
                        
                        x = x
                     else: 
                        wordlist.append(Password)
                        x += 1

                        #two variables password generator with dot
for x in range (-combinations, combinations):
      progress = round((len(wordlist)/combinations)*100)
      progressl.append(progress)
      
      if progress not in progressl:
        print("Progress =", round((len(wordlist)/combinations)*100),"%")
     

      wordlist = list(dict.fromkeys(wordlist))  
      x = len(wordlist)
      underscore = (random.choice(Power))
      var1 = (random.choice(ID))
      var2 = (random.choice(ID))
       
      if var1 == var2:
          x = x
      
      else:
       
          if underscore < 1:
                 Password = (var1 + var2)
                 if Password == "":
                       x = x
                 else:
                                   
                       x = x + 1
                       wordlist.append(Password)
                            
          else:
                     Password = (var1 + "." + var2)
                     if Password == "." :
                        x = x
                     elif Password in wordlist:
                        
                        x = x
                     else: 
                        wordlist.append(Password)
                        x += 1  

                        #three variables password generator with dash
for x in range (-combinations,2*combinations):
        
        progressl.append(progress)
        progress = round((len(wordlist)/combinations)*100)
        if progress not in progressl:
            print("Progress =", round((len(wordlist)/combinations)*100),"%")
        
        wordlist = list(dict.fromkeys(wordlist))  
        x = len(wordlist)
        underscore = (random.choice(Power))
        var1 = (random.choice(ID))
        var2 = (random.choice(ID))
        var3 = (random.choice(ID))
        if (var1 == var2) or (var1 == var3) or (var2 == var3) or (var1 == var2 == var3) :
              x = x
        else:

            underscore = (random.choice(Power))
            var1 = (random.choice(ID))
            var2 = (random.choice(ID))
            var3 = (random.choice(ID))
            if underscore < 1:
                Password = (var1 + var2 + var3)
                if Password == "":
                   x = x
                elif Password in wordlist:
                     
                        x = x
                else:
                        wordlist.append(Password)
                        
                        x = x + 1

                  
            else:
                var4 = (random.choice(position))
                if var4 == 1:
                            Password = (var1 + "_" + var2 + var3)
                            if Password in wordlist:
                                x = x
                            else:
                                wordlist.append(Password)
                                x = x + 1
                                
                elif var4 == 2:
                        Password = (var1 + var2 + "_" + var3)
                        if Password in wordlist:
                            x = x
                        else:
                            wordlist.append(Password)
                            
                            x = x + 1                                                 
                else:
                        Password = (var1 + "_" + var2 + "_" + var3)
                        if Password in wordlist:
                            x = x
                        else:
                            wordlist.append(Password)
                            x = x + 1
                        #three variables password generator with dot                       
for x in range (-combinations,2*combinations):
        
        progressl.append(progress)
        progress = round((len(wordlist)/combinations)*100)
        if progress not in progressl:
            print("Progress =", round((len(wordlist)/combinations)*100),"%")
        
        wordlist = list(dict.fromkeys(wordlist))  
        x = len(wordlist)
        underscore = (random.choice(Power))
        var1 = (random.choice(ID))
        var2 = (random.choice(ID))
        var3 = (random.choice(ID))
        if (var1 == var2) or (var1 == var3) or (var2 == var3) or (var1 == var2 == var3) :
              x = x
        else:

            underscore = (random.choice(Power))
            var1 = (random.choice(ID))
            var2 = (random.choice(ID))
            var3 = (random.choice(ID))
            if underscore < 1:
                Password = (var1 + var2 + var3)
                if Password == "":
                   x = x
                elif Password in wordlist:
                     
                        x = x
                else:
                        wordlist.append(Password)
                        
                        x = x + 1

                  
            else:
                var4 = (random.choice(position))
                if var4 == 1:
                            Password = (var1 + "." + var2 + var3)
                            if Password in wordlist:
                                x = x
                            else:
                                wordlist.append(Password)
                                x = x + 1
                                
                elif var4 == 2:
                        Password = (var1 + var2 + "." + var3)
                        if Password in wordlist:
                            x = x
                        else:
                            wordlist.append(Password)
                            
                            x = x + 1                                                 
                else:
                        Password = (var1 + "." + var2 + "." + var3)
                        if Password in wordlist:
                            x = x
                        else:
                            wordlist.append(Password)
                            x = x + 1

                        #output

complete = (round((len(wordlist)/combinations)*100))
for k in range (100 - complete):
    time.sleep(0.03)
    print("Progress =", complete + 1,"%")
    complete += 1



time.sleep(1)
print ("""


""")
print(wordlist)
print("")
print("")
print ("Total unique passwords:",(len(wordlist)))

print("")
if combinations > 5000:
    print ("Total combinations:",(combinations))


if starttest == "y":
    if testcode in wordlist:
        print("access gratned")
    else:
       
       print("access denied")



  
print("")
print("the wordlist has been saved as target.txt")
print("""

...Finch also notices a rose placed on the train seat. It is a kind called a “Violet Carson”
""")

with open('target.txt', 'w') as f:
    for item in wordlist:
        f.write("%s\n" % item)
