#Display the purpose of the program
print("CURRENT AFFAIRS QUESTIONS")
print("Lets see how current you are")

#Display the insturctions
print("INSTRUCTIONS!!!")
print("Choose the correct answer from the option letter A-D")
print("Each questions carries 20 marks")
print("Understand the Questons so that you have a good grade score")

#Print the user's name
name = str(input("Please enter your name: "))

#Initialize the score variable
score = 0

#Ask the user a questions and
#Wait for the answer

que1 = input("When did Nigeria gain her Independent? \n(A)Oct 1st 1990 \n(B)Nov 1st 1840 \n(C)Oct 1st 1960 \n(D)Sept 1st 1960\n")

if(que1.upper()=="C"):
    print("correct!")
    score = score + 20
else:
    print("wrong!")

que2 = input("Who was the president of Nigeria in the year 1999? \n(A)General Olusegun Obasanjo \n(B)Hon. Olusegun Agagu \n(C)General Muhammadu Buhari \n(D)Goodluck Ebele Jonathan\n")
if(que2.upper()=="A"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")

que3 = input("The federal capital territory was formerly at? \n(A)Badia \n(B)Abuja \n(C)Zamfara \n(D)Lagos\n")
if(que3.upper()=="D"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
que4 = input("When will the next election be in Nigeria? \n(A)2019 \n(B)2020 \n(C)2022 \n(D)2023\n")
if(que4.upper()=="A"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
que5 = input("What is the full meaning of 'PMB'? \n(A)Primary Mobile Barrack \n(B)President Muhammadu Buhari \n(C)President of Magician Begium \n(D)Post Mend Black\n")
if(que5.upper()=="B"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")

que6 = input("_____ can also stand as the country identity aside Flag. \n(A)Color \n(B)Physique \n(C)The COat Of Arm \n(D)All of the above\n")
if(que6.upper()=="C"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")

que7 = input("How many colour has Nigeria Flag? \n(A)6 \n(B)2 \n(C)4 \n(D)3\n")
if(que7.upper()=="B"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")

que8 = input("The talk of the state parties as far as Nigeria is concerned are _____. \n(A)ADC and ANPP \n(B)APGA and HOPE \n(C)APD and PDP \n(D)APC and PDP\n")
if(que8.upper()=="D"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    
que9 = input("How many stanzas has The Nigeria National Anthem? \n(A)Eight \n(B)Two \n(C)Three \n(D)Twelve\n")
if(que9.upper()=="B"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    
que10 = input("In which of the listed category did you fall as a Nigeria? \n(A)Civilian \n(B)Military \n(C)I dont know \n(D)Why the silly question!\n")
if(que10.upper()=="A"):
    print("Correct!")
    score = score + 20
elif(que10.upper()=="B"):
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")

#Print the user's score
print("Welldone",name,"Your total score is",score)

#Total Score
Totalscore = 200

#Percentage score
perscore = score * 100/Totalscore
print("Dear",name,"Your percentage score is",perscore,"%")

#Grade
grade1 = 'A1'
grade2 = 'B2'
grade3 = 'B3'
grade4 = 'C4'
grade5 = 'C5'
grade6 = 'C6'
grade7 = 'D7'
grade8 = 'E8'
grade9 = 'F9'
if((score<=200) and (score>=180)):
    print(grade1)
elif((score<180) and (score>=160)):
    print(grade2)
elif((score<160) and (score>=140)):
    print(grade3)
elif((score<140) and (score>=120)):
    print(grade4)
elif((score<120) and (score>=100)):
    print(grade5)
elif((score<100) and (score>=80)):
    print(grade6)
elif((score<80) and (score>=60)):
    print(grade7)
elif((score<60) and (score>=40)):
    print(grade8)
elif((score<40) and (score>=1)):
    print(grade9)
