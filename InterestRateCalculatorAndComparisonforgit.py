#Interest Rate Calculator and Comparison



def Total_Over_Time(User_Amount, User_Interest_Rate, Months_Held):                  #Function to calculate interest rate over a period of time.
    Interest_Rate = (User_Interest_Rate /100)
    Monthly_Rate = (Interest_Rate /12)
    Interest_Earned = (User_Amount * Monthly_Rate * Months_Held)
    New_Total = (User_Amount + Interest_Earned)
    return New_Total


counter = 0                                                                         #Empty counter to iterate the loop.
highest_interest_rate = []                                                          #Empty list to store each total.
while counter < 3:                                                                  #Iterate 3 times.
    User_Amount = input("Enter Savings Deposit Amount(type 'E' to quit): ")         #Gets user input.
    if User_Amount == "E":                                                          #User can quit out by entering E.
        break
    User_Interest_Rate = input("Enter Interest Rate as Percentage(type 'E' to quit): ") #Gets user input.
    if User_Interest_Rate == "E":
        break
    Months_Held = input("For how many months?(type 'E' to quit): ")                 #Gets user input.
    if Months_Held == "E":
        break
    a = Total_Over_Time(int(User_Amount), int(User_Interest_Rate), int(Months_Held))
    highest_interest_rate.append(a)                         #Adds next interest rate to list.
    print("Total: ", a)                                     #Prints total then returns to beginning of while loop if true.
    counter += 1                                            #Adds 1 to the counter when it repeats.

print("Comparisons Complete: ", counter)                    #When while loop breaks this will print.
if highest_interest_rate:                                   #If the list is not empty this will print.
    print("Highest Total: ", end='')
    print(max(highest_interest_rate))
