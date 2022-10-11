#comments

import math

def Intensity(age):
 intensity = 1
 if age >= 80:
  age_above = age-80
  intensity = 1-0.4-0.04*age_above
  if intensity<0.2:
   intensity = 0.2
 elif age>=75:
  age_above = age-75
  intensity = 1-0.25-0.03*age_above
 elif age>65:
  age_above = age-65
  intensity = 1-0.05-0.02*age_above
 elif age>60:
  age_above = age-60
  intensity = 1-0.01*age_above
 return intensity

valid_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
valid_integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Valid_String(string):
  valid_string = True
  if len(string)<1:
    valid_string = False
  if string.isspace():
    valid_string = False
  i=0
  while i<len(string):
    if (string[i] in valid_characters)==False:
      valid_string = False
    i += 1
  return valid_string

def Valid_Integer(integer):
  i=0
  valid_integer = True
  while i<len(integer):
    if (integer[i] in valid_integers)==False:
      valid_integer = False
    i += 1
  return valid_integer


#These are ten categories of workouts:
#1------------------------------------------------------
def Fat_Loss(intensity):
 name_workout = "Gym workout for fat loss\n"


 workout = f"\nPlate thrusters ({math.ceil(15*intensity)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*intensity)} reps x 3 sets)\n\
Box jumps ({math.ceil(10*intensity)} reps x 3 sets)\n\
Lounges ({math.ceil(10*intensity)} reps x 3 sets)\n\
Renegade rows ({math.ceil(10*intensity)} reps x 3 sets)\n\
Press ups ({math.ceil(15*intensity)} reps x 3 sets)\n\
Treadmill ({math.ceil(15*intensity)} mins x 2 sets)\n\
Supermans ({math.ceil(15*intensity)} reps x 3 sets)\n\
Crunches ({math.ceil(20*intensity)} reps x 3 sets)"
 msg = name_workout+workout
 return msg

#2------------------------------------------------------
def Stretch_Relax(intensity):
 name_workout = "Gym workout for stretch and relax\n"

 workout = f"\nQuad stretchs ({math.ceil(2*intensity)} mins x 3 sets)\n\
Hamstring stretchs ({math.ceil(2*intensity)} mins x 3 sets)\n\
Chest and shoulder stretchs ({math.ceil(2*intensity)} mins x 2 sets)\n\
Upper back stretchs ({math.ceil(3*intensity)} mins x 2 sets)\n\
Biceps stretchs ({math.ceil(2*intensity)} mins x 2 sets)\n\
Triceps stretchs ({math.ceil(2*intensity)} mins x 3 sets)\n\
Hip flexors ({math.ceil(2*intensity)} mins x 3 sets)\n\
Calf stretchs ({math.ceil(2*intensity)} mins x 3 sets)\n\
Lower back stretchs ({math.ceil(2*intensity)} mins x 3 sets)"
 msg = name_workout+workout
 return msg

#3------------------------------------------------------
def High_Intensity(intensity):
 name_workout = "Gym workout for high-intensity exercises\n"

 workout = f"\nJumping jacks ({math.ceil(20*intensity)} reps x 4 sets)\n\
Sprints ({math.ceil(20*intensity)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(20*intensity)} reps x 4 sets)\n\
Squat jumps ({math.ceil(20*intensity)} reps x 4 sets)\n\
Lunges ({math.ceil(20*intensity)} reps x 3 sets)\n\
Crunches ({math.ceil(20*intensity)} reps x 3 sets)\n\
Treadmill ({math.ceil(15*intensity)} mins x 2 sets)\n\
Side planks ({math.ceil(15*intensity)} reps x 3 sets)\n\
Burpees ({math.ceil(15*intensity)} reps x 3 sets)"
 msg = name_workout+workout
 return msg

#4------------------------------------------------------
def Strong_Legs(intensity):
 name_workout = "Gym workout for strong legs\n"

 workout = f"\nBack squats ({math.ceil(10*intensity)} reps x 5 sets)\n\
Hip thrusts ({math.ceil(12*intensity)} reps x 3 sets)\n\
Overhead presses ({math.ceil(10*intensity)} reps x 5 sets)\n\
Rack pulls ({math.ceil(10*intensity)} reps x 5 sets)\n\
Squats ({math.ceil(10*intensity)} reps x 4 sets)\n\
Dumbbell lunges ({math.ceil(10*intensity)} reps x 3 sets)\n\
Leg curls ({math.ceil(15*intensity)} reps x 3 sets)\n\
Standing calf raises ({math.ceil(20*intensity)} reps x 2 sets)"
 msg = name_workout+workout
 return msg

#5------------------------------------------------------
def Strong_ABS(intensity):
 name_workout = "Gym workout for strong ABS\n"

 workout = f"\nCross crunchs ({math.ceil(12*intensity)} reps x 3 sets)\n\
Knee ups ({math.ceil(15*intensity)} reps x 5 sets)\n\
Hip thrusts ({math.ceil(15*intensity)} reps x 3 sets)\n\
Mountain climbers ({math.ceil(15*intensity)} reps x 3 sets)\n\
Vertical hip thrusts ({math.ceil(12*intensity)} reps x 3 sets)\n\
Bicycles ({math.ceil(15*intensity)} mins x 2 sets)\n\
Front planks ({math.ceil(15*intensity)} mins x 3 sets)\n\
Dragon flags ({math.ceil(12*intensity)} reps x 4 sets)\n\
Reverse crunches ({math.ceil(10*intensity)} reps x 3 sets)"
 msg = name_workout+workout
 return msg

#6------------------------------------------------------
def Shoulder_Arm(intensity): 
 name_workout = "Gym workout for strong shoulder and arms\n"

 workout = f"\nBench presses ({math.ceil(10*intensity)} reps x 5 sets)\n\
Triceps dips ({math.ceil(10*intensity)} reps x 5 sets)\n\
Incline dumbbell presses ({math.ceil(12*intensity)} reps x 3 sets)\n\
dumbbell flyes ({math.ceil(15*intensity)} reps x 3 sets)\n\
Triceps extensions ({math.ceil(15*intensity)} reps x 3 sets)\n\
Pull ups ({math.ceil(10*intensity)} reps x 5 sets)\n\
Treadmill ({math.ceil(15*intensity)} mins x 2 sets)\n\
Bent over rows ({math.ceil(10*intensity)} reps x 5 sets)\n\
Chin ups ({math.ceil(10*intensity)} reps x 3 sets)"
 msg = name_workout+workout
 return msg

#7------------------------------------------------------
def Male_Younger_18():
 name_workout = "Gym workout for a male younger than 18 years old\n"
 
 workout = "\nHigh knees (20 reps x 3 sets)\n\
Squats (10 reps x 3 sets)\n\
Calf raises (10 reps x 3 sets)\n\
Scissor jumps (12 reps x 3 sets)\n\
Burpees (10 reps x 3 sets)\n\
Treadmill (10 mins x 2 sets)"
 msg = name_workout+workout
 return msg

#8------------------------------------------------------
def Female_Younger_18(): 
 name_workout = "Gym workout for a female younger than 18 years old\n"

 workout = "\nSquats (10 reps x 3 sets)\n\
Crunches (10 reps x 2 sets)\n\
Jumping jacks (10 reps x 3 sets)\n\
Push ups (10 reps x 2 sets)\n\
Burpees (10 reps x 3 sets)\n\
Treadmill (10 mins x 2 sets)"
 msg=name_workout+workout
 return msg

#9------------------------------------------------------
def Male_18(intensity):
 name_workout = "Gym workout for a male at least 18 years old\n"

 workout = f"\nStanding biceps curls ({math.ceil(20*intensity)} reps x 3 sets)\n\
Seated incline curls ({math.ceil(18*intensity)} reps x 3 sets)\n\
Seated dumbbell presses ({math.ceil(12*intensity)} reps x 3 sets)\n\
Leg presses ({math.ceil(15*intensity)} reps x 3 sets)\n\
Bench presses ({math.ceil(10*intensity)} reps x 4 sets)\n\
Tricep kickbacks ({math.ceil(15*intensity)} reps x 3 sets)\n\
Hip thrusts ({math.ceil(12*intensity)} reps x 3 sets)\n\
Seated rows ({math.ceil(10*intensity)} reps x 4 sets)"
 msg = name_workout+workout
 return msg

#10------------------------------------------------------
def Female_18(intensity):
 name_workout = "Gym workout for a female at least 18 years old\n"

 workout = f"\nLateral raises ({math.ceil(15*intensity)} reps x 3 sets)\n\
 Reverse flyes ({math.ceil(12*intensity)} reps x 3 sets)\n\
 Hip thrusts ({math.ceil(12*intensity)} reps x 3 sets)\n\
 Incline dumbbell presses ({math.ceil(15*intensity)} reps x 3 sets)\n\
 Squats ({math.ceil(10*intensity)} reps x 4 sets)\n\
 Dumbbell lunges ({math.ceil(10*intensity)} reps x 3 sets)\n\
 Leg presses ({math.ceil(12*intensity)} reps x 3 sets)\n\
 Dumbbell presses ({math.ceil(10*intensity)} reps x 4 sets)"
 msg = name_workout+workout
 return msg


###############################################################
##################### EXECUTING CODE ##########################
###############################################################


def __main__():
 #Gathering name of user
 
 valid_input = False
 while valid_input == False:
  name = input("Please enter your name: ")
  name = name.strip(" ")
  if Valid_String(name):
    valid_input = True
  else:
    print("Error: Only accept alphabetical characters and spaces for name")
 
 #Gathering age of user
 valid_input = False
 while valid_input == False:
  age = input("\nPlease enter your age: ")
  if Valid_Integer(age):
   if 0<=int(age)<=110:
    valid_input = True
   else:
    print("Error: The age is a number between 0 to 110")
  else:
   print("Error: The age is a number between 0 to 110")
 age = int(age)

 #Gathering sex of user
 valid_input = False
 while valid_input == False:
  sex = input("\nPlease enter your biological sex (female/male): ")
  if sex == "male" or sex == "female":
   valid_input = True
  else:
   print("Error: Please enter valid input")

 #Gathering focus of user
 valid_input = False
 while valid_input == False:
  number_workout = input("\nHow many days per week you can train: ")
  if Valid_Integer(number_workout):
   if 1<=int(number_workout)<=7:
    valid_input = True
   else:
    print("Error: It can only be a number between 1 to 7")
  else:
   print("Error: It can only be a number between 1 to 7")
 number_workout = int(number_workout)
 

 #Gathering number of workouts the user wants to do in a week
 valid_input = False
 while valid_input == False:
  focus = input("\nWhat do you want to get out of your training?\
    \n\t1. Your goal is losing weight \
    \n\t2. Your goal is to staying calm and relax \
    \n\t3. Your goal is increasing your heart rate \
    \n\t4. Your goal is having stronger legs \
    \n\t5. Your goal is having stronger ABS \
    \n\t6. Your goal is having stronger shoulders and arms \
    \nChoose a number between 1 to 6: ")
  if Valid_Integer(focus):
   if 1<=int(focus)<=7:
    valid_input = True
   else:
    print("Error - It can only be a number between 1 to 6")
  else:
   print("Error - It can only be a number between 1 to 6")
 focus= int(focus)
 

 #Executing the code
 print(f"\nHello {name}! Here is your training:\n\
  -------------------------------------------------------------------------------------")
 
 #Determining intensity of workout based on age
 intensity = Intensity(age)

 #Creating primary workout for user
 primary_workout = 0
 if focus == 1:
  primary_workout = Fat_Loss(intensity)
 elif focus == 2:
  primary_workout = Stretch_Relax(intensity)
 elif focus == 3:
  primary_workout = High_Intensity(intensity)
 elif focus == 4:
  primary_workout = Strong_Legs(intensity)
 elif focus == 5:
  primary_workout = Strong_ABS(intensity)
 elif focus == 6:
  primary_workout = Shoulder_Arm(intensity)

 #Figuering out wether to create secondary workout and if so assigning the correct workout to the person depending on age and sex 
 if number_workout > 1:
  secondary_workout = 0
  if sex == "male":
   if age >= 18:
    secondary_workout = Male_18(intensity)
   elif age < 18:
    secondary_workout = Male_Younger_18()
  elif age >= 18:
   secondary_workout = Female_18(intensity)
  elif age < 18:
   secondary_workout = Female_Younger_18()

 i=1
 while (i <= number_workout):
  print(f"Day {i}")
  if i%2 == 0:
   print(secondary_workout)
  elif i%2 != 0:
   print(primary_workout)
  print("-------------------------------------------------------------------------------------")
  i = i+1

 print(f"\nBye {name}.")

if __name__ == "__main__":
    __main__()