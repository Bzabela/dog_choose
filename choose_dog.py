# dog breed choice
dog_breed = ["Cockapoo", "Maltipoo", "Cavoodle", "Cavachon", "Bernedoodle"]

result = {}
# max_points = 10
# min_points = 1

# taking every dog from breed list and asking user to score on how cute and fluffly they are
for dog in range (len(dog_breed)):
    rate_cute = int(input (f'How cute is {dog_breed[dog]} from 1 to 10: '))
    rate_fluff = int(input (f'How fluffy is {dog_breed [dog]} from 1 to 10: '))

# store result in dictionary (different values for each dog), print score
    result[dog_breed[dog]] = rate_cute + rate_fluff
    print (f' {dog_breed[dog]} got {result[dog_breed [dog]]} points')

#sorting result (scoreboard)
sorted_result= sorted (result.items(), key=lambda t: t[1], reverse=True)
print(sorted_result)

#TODO Add GUI (Tkinter), make input validation

