from foodcalculators import *;

print("Hello! Which of the following meal plans are you currently using?");
print("1. Unlimited Plan\n2. 14-Plus Plan\n3. 9-Plus Plan\n4. 330 Plan\n" +\
	"5. 250 Plan");

userPlan = "";
date = "PLACEHOLDER";
dayofweek = "PLACEHOLDER";

userPlan = input("Type a number 1-5: ");
print(userPlan);
# TODO: Implement other plans. For now I will start with 9-Plus

print("The 9-Plus Plan has 9 meals per week and 415 dining dollars per semester.");
print("The current date is " + date + ", which is a " + dayofweek);
# if date is between Sept 6 - Dec 12, it's fall semester
# if date is between Jan 19 - May 12, it's spring semester

print(getMealStatus(12, 12));
