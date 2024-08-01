#Asking the user about current conditions

is_sunny = bool(input("Is it sunny?"))
has_umbrella = bool(input("Do you have an umbrella?"))

#Establishing the Variables

go_outside = False
stay_inside = False
perfect_day = False

#Evaluating and printing the output

if is_sunny == True or has_umbrella == True:
    go_outside = True
if is_sunny == False and has_umbrella == False:
    stay_inside = True
if is_sunny == True and has_umbrella == False:
    perfect_day = True
print("go outside :-",go_outside)
print("stay inside :-",stay_inside)
print("Perfect day :-",perfect_day)

