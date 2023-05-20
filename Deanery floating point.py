#Converting a deanery value from 8 bit floating point 143

__author__ = 'Aneez Amja'

#Converting a deanery value from 8 bit floating point
Loop = 'Yes'

while Loop == 'Yes':
    BNum = input("Enter a 8 bit binary number  ") #8 bit bijnary number#
    Bsign = BNum[0]  # Splits BNum first number of 8 bit binary number is declared as the sign dictating whether its postive or negative#
    Man = BNum[1:5] # Splits BNum 2 till 4 number of the 8 bit binary number is the mantissa#
    SignExp = BNum[5]# Splits BNum 6th number of 8 bit binary number is declared as the sign dictating whether the exponent is postive or negative#
    Exp = BNum[6:8] # Last 2 values of the 8 bit binary number is the exponent#

    print(Bsign,Man,SignExp,Exp)

    if Bsign=='1':#determines if the number is overall positive or negative
        sign='-' #Indicates whether the number is negative or positive
    else:
        sign = "+"#Indicates whether the number is negative or positive

                                                #Exp = - 3
                                                # -4 2 1
    Exponent = 0                                 #  1 0 1
    if SignExp[0] == "1":
        Exponent = Exponent  - 4    #Most Significant bit(-4) therefore making the sign of the exponent negative
    if Exp[0] == '1':               #If the first character of "Exp" is a 1 then
        Exponent = Exponent +2      # Then the "Exp" is gets added by 2
    if Exp[1]== '1':                #If the second character of "Exp" is a 1 then
        Exponent = Exponent +1      #The second integer of "Exp" is gets added by 1

    Mantiss = 0                     #Mantissa is currently 0
    if Man[0] == "1":               # If the first character of the "Man" is 1 then
        Mantiss = Mantiss + 0.5     # The "Mantiss" variable is added by 0.5 as that is the most significant bit
    if Man[1] == "1":               # If the second character of the "Man" is 1 then
        Mantiss = Mantiss + 0.25    # The "Mantiss" variable is added by 0.25 as that is the 2nd most significant bit
    if Man[2] == "1":               # If the third character of the "Man" is 1 then
        Mantiss = Mantiss + 0.125   # The "Mantiss" variable is added by 0.125 as that is the 3rd significant bit
    if Man[3] == "1":               # If the fourth character of the "Man" is 1 then
        Mantiss = Mantiss + 0.0625  # The "Mantiss" variable is added by 0.0625 as that is the 4th significant bit

    AllMantiss = Mantiss            # All the "Mantiss" values added up into one varianle called "AllMantiss"
    Deanery =AllMantiss * 2**Exponent # The deanery value is the Mantiss total times by 2^Exponent

    print("The Deanery value as a floating point binary is :",sign,Deanery) #Prints out the Deanery value as a floating point binary

    Loop = input("Do you want to retry? Yes/No") #Loops back to the start







 


























