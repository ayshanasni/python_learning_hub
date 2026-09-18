#Ask the user to enter their name and print a welcome message with their name.
NAME=input("Enter your name")
print("Welcome",NAME)
AGE=input("Enter your age")#age of the user
print("You are",AGE,"years old")
CITY=input("Enter your Place:")#city of the user
print(f"My name is {NAME},I am {AGE} years old and I am from{CITY} ")
num_1=int(input("Enter the first number"))#operations between numbers
num_2=int(input("Enter the second number"))
print(f"sum of {num_1} & {num_2} is {num_1+num_2}")
print(f"difference of {num_1} & {num_2} is {num_1-num_2}")
print(f"product of {num_1} & {num_2} is {num_1*num_2}")
print(f"quetient of {num_1} & {num_2} is {num_1/num_2}")
#to find the area and perimeter of the rectangle
LENGTH=float(input("Length of the rectangle is "))
WIDTH=float(input("Width of the rectangle is"))
print(f"area of rectangle is{LENGTH*WIDTH}")
print(f"PerImeter of the rectangle is{2*(LENGTH+WIDTH)}")
#to find area and perimeter of square 
SIDEOFSQUARE=float(input("Side of the square is"))
print(f"area of the sqaure is {SIDEOFSQUARE*SIDEOFSQUARE}")
print(f"Perimeter of the square is {4*SIDEOFSQUARE}")
#area of the circle
RADIUS=float(input("Radius of the circle is"))
print(f"Area of the circle is{3.14*RADIUS*RADIUS}")
#fahranheit to celcius conversion
CELCIUS=float(input("Enter temperature in celcius"))
FAHRENHEIT=(CELCIUS*9/5)+32
print("Temperature in Fahrenheit:",FAHRENHEIT)
FAHRENHEIT=float(input("Enter temperature in Fahrenheit"))
CELCIUS=(FAHRENHEIT-32)*5/9
print("Temperature in Celcius",CELCIUS)
#to find the year of birth
BIRTHYEAR=int(input("Enter year of birth"))
CURRENTYEAR=2026
AGE_1=CURRENTYEAR-BIRTHYEAR
print("Your approximate age is ",AGE_1)
#Days 
DAYS=int(input("Enter number of days"))
WEEKS=DAYS//7
REMAININGDAYS=DAYS%7
print("Weeks",WEEKS,"Remaining days,REMAININGDAYS")
#remaining seconds
SECONDS=int(input("Enter the number of seconds"))
MINUTES=SECONDS // 60
REMAININGSECONDS=SECONDS % 60
print("Minutes:",MINUTES,"Remaining seconds:",REMAININGSECONDS)
#discount amount
AMOUNT=float(input("Enter amount in rupees:"))
DISCOUNTPERCENT=float(input("Enter the discount in percentage"))
DISCOUNTAMOUNT=(AMOUNT * DISCOUNTPERCENT)/100
FINALPRICE=AMOUNT-DISCOUNTAMOUNT
print("Discount amount",DISCOUNTAMOUNT)
print("Final price",FINALPRICE)
#bill
PRICE=int(input("Enter the price of product:"))
QUANTITY=int(input("Enter the qauntity of product:"))
TOTALBILL=PRICE*QUANTITY
print("Total bill:",TOTALBILL)
TOTALBILL=int(input("Enter the total bill amount"))
NUMBEROFPEOPLE=int(input("Enter thenumber of people"))
SHARE=TOTALBILL/NUMBEROFPEOPLE
print("Each person should pay:",SHARE)
#salary
SALARY=int(input("Enter the basic salary"))
HRA=0.20*SALARY
DA=0.10*SALARY
GROSS_SALARY=SALARY+HRA+DA
print("HRA:",HRA)
print("DA:",DA)
print("Gross salary:",GROSS_SALARY)
#simpleinterest
PRINCIPAL=float(input("Enter the pricipal"))
RATE_OF_INTEREST=float(input("Enter the rate of interest"))
TIME=float(input("Enter the time(in years)"))
SIMPLE_INTEREST=(PRINCIPAL*RATE_OF_INTEREST*TIME)/100
print("Simple interest:",SIMPLE_INTEREST)
#marks
Mark1=float(input("Enter the mark of the subject1: "))
Mark2=float(input("Enter the mark of the subject2: "))
Mark3=float(input("Enter the mark of the subject3: "))
Mark4=float(input("Enter the mark of the subject4: "))
Mark5=float(input("Enter the mark of the subject5: "))
Total_Marks= Mark1 + Mark2 + Mark3 + Mark4+ Mark5
print("Total marks:", Total_Marks)
Average= (Mark1 + Mark2 + Mark3 + Mark4 + Mark5)/5
print("Average:", Average)
#square and cube
Num=float(input("Enter a number:"))
Square=Num**2
Cube=Num**3
print("Square:", Square)
print("Cube:", Cube)





