maths=int(input("Enter maths mark"))

phy=int(input("enter physics mark"))

chem=int(input("enter chemistry mark"))

if(maths>=35 and phy>=35 and chem>=35):

    avg=(maths+phy+chem)/3
    if(avg<=59):

        print("You have got C grade")

    elif(avg>59 and avg<=69):

        print("You have got B grade")

    elif(avg>69):

        print("You have got A grade")

else:

   print("You have failed the exams so your grade will not be calculated")