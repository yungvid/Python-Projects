from datetime import datetime

def add_info():
      print("-" * 5 + "Add New Information" + "-" * 5)
      name = input("What is your name?: ")
      location = input("Where are you located?: ")
      age = input("How old are you?: ")

      date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # importing the current date

      with open("vid_survey.txt", "a", encoding="utf-8") as s: # Open a file to save the info input by user
        s.write(f"Date: {date}\n")
        s.write(f"Name: {name}\n")
        s.write(f"Location: {location}\n")
        s.write(f"age: {age}\n")
        s.write(f"-" * 30 + "\n")

print("\nThank you for particitating, Information saved successfully!")
print("-" * 30)

def view_info():
      try:
           with open("vid_survey.txt", "r", encoding="utf-8") as s: # Read and return the saved
            content = s.read()
            if content.strip() == "":
                 print("No Information collected, Try again!")
            else:
                 print(content)

      except FileNotFoundError:
           print("No survey data found. Want to take another Survey")

print("Welcome to VID Little Survey!")
print("-" * 30)

while True:
     print("\n====== MENU ======")
     print("1. Add New Information")
     print("2. View all Information")
     print("3. Exit")

     choice = input("Enter your choice from 1 - 3: ")

     if choice == "1":
          add_info()
     elif choice == "2":
          view_info()
     elif choice == "3":
          print("Thank you for using VID Survey. Goodbye!")
          break
     else:
          print("Invalid choice. Please enter a valid option from 1 to 3.") 






