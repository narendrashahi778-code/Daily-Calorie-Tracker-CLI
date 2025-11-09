#name: Rahul Kumar
#roll no: 2501730394
#date: 18/10/2025
#project_title: Daily Calorie Tracker CLI

print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you record your meals and calories\nit checks if you stayed within your daily limit\nand it can save your session for future tracking.")

print("")

#these empty lists are used to store meal names and amount of calories 
meal_names = []
calorie_amounts = []

num_meals = int(input("enter the number of meals you've had today: "))

for i in range (num_meals):
    name = (input(f"enter the name of meal {i+1}: ")) #we added an f string {i+1} because the range starts from 0 and not 1 as we did not add a start point 0 is default and meal no.0 does not sound natural
    calorie = float(input(f"enter the anount of calories in {name}: ")) #we used float because calories can often be in decimals 
    meal_names.append(name)
    calorie_amounts.append(calorie)

#calculating total and average calories

total_calories = sum(calorie_amounts)
avg_calories = total_calories / num_meals if num_meals > 0 else 0 #if num_meals > 0 else 0 protects us from errors, if the user enters zero meals then we can avoid ZeroDivisionError

print("")

daily_limit = float(input("What is your daily calorie limit: "))

if total_calories > daily_limit:
    print(f" You have exceeded your daily limit by {total_calories - daily_limit} calories.")
else:
    print("Great job! You're within your daily calorie limit.")


#this is to format the final output in a good manner

print("\nMeal Name\tCalories") #\n = new line \t = tab 
print("_____________________________")
for i in range(num_meals):
    print(f"{meal_names[i]}:\t\t{calorie_amounts[i]}")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{avg_calories}")

save= input("Do you want to save this session to a file? (yes/no): ").lower() #we used .lower() to avoid any errors (for eg. if the user writes YES or YeS instead of yes)

if save == "yes":
    date_today = input("enter today's date (like 27/10/2025): ")
    filename = "record.txt"
    with open (filename, "a") as f: #the "a" stands for append so everything get appended to the file 
        f.write(f"session date: {date_today}\n")
        f.write("Meal Name\tCalories\n")
        f.write("-------------------------\n") 
        for i in range(num_meals):
            f.write(f"{meal_names[i]}\t{calorie_amounts[i]}\n")
        f.write(f"Total:\t{total_calories}\n")
        f.write(f"Average:\t{avg_calories:.2f}\n")
        if total_calories > daily_limit:
            f.write(f"Warning: Exceeded daily limit by {total_calories - daily_limit} calories.\n")
        else:
            f.write("Within daily calorie limit.\n")
        f.write("-------------------------\n\n")
    print(f"Session has been saved to {filename}!")
else:
    print("session not saved")

print("")
print("Thank you for using the Daily Calorie Tracker!\nStay healthy ❤️ stay safe and have a good day! 😃 ")