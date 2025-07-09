pet = input("What type of pet do you have? (dog | cat |bird |hamster): ")
age = int(input("How old is your pet in human years?"))

pet_age = 0
if pet == "dog" or pet == "cat":
  if age < 3 :
    pet_age *= 12
  else:
    pet_age = 24
    age  = age - 2
    pet_age += age * 4

elif pet == "bird" :
  pet_age = age * 9

elif pet == "hamster":
  pet_age = age * 25


print(
  f'''
===    pet age conversion ===

Pet Type : {pet}
Human Age: {age}
Pet Age: {pet_age}

Fun Fact : Your {pet} is like a {pet_age} -year-old human !
'''
)