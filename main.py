# if flower1 is even and flower2 is odd (or vice versa) return True


# def lovefunc( flower1, flower2 ):
#     if (flower1%2 == flower2%2):
#       return False
#     else:
#       # return True

## If employed is true and Vacation is false, the return True. Otherwise return false.
# def set_alarm(employed, vacation):
#   return ((employed==True) and (vacation != True))



## Return a phrase based on the number of petals passed in
    


def how_much_i_love_you(nb_petals):
  phrases = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
  while (nb_petals > len(phrases)):
      nb_petals -= 6
  return phrases[nb_petals -1]

#HEY ANTHONY, This is what you meant to do.

def how_much_i_love_you(nb_petals):
  phrases = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
  return phrases[nb_petals%6 - 1]

## Return number of passengers having to wait given CAPACITY, passengers ON the bus, and passensgers WAITing to board

def enough(cap, on, wait):
  room = (cap - on)
  if (room >= wait):
    return 0
  else:
    return (wait-room)

## Given an array of numbers, return the first non-consecutive number. If all numbers are consecutive, return None.
## COME BACK TO THIS ONE LATER!

myList = [1,2,3,4,5,6,7,8]


def first_non_consecutive(arr):
  for num in range(0,len(arr)):
    if (num == len(arr)-1):
        return None
    if (arr[num] != arr[num+1] - 1):
      return arr[num+1]
  
    
## Given an array of your class' test scores as well as your own score, return True if your score is better than the average of all 
## test scores (including yours), else return False

def better_than_average(class_points, your_points):
  return (your_points > (sum(class_points)/len(class_points)))
    

## Return True if given string is all capitalized. Else, return False

def is_uppercase(inp):
  return inp == inp.upper()


## Calculate how many years ago the Father was twice as old as the Son. OR in how many years it will be until that point. 
## Answer is always greater than or equal to 0

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))

## Is the number passed even or odd? Numbers may be positive, negavive, ints or floats.

def is_even(n): 
  return n%2 == 0

## Build a list in reverse order from n to 1

def reverse_seq(n):
  myList = []
  for i in range(1,n+1):
    myList.append(i)
  myList.reverse()
  return myList

#This works but it's long and isn't effecient. You could use the list constructor and just put in the range.

def reverse_seq2(n):
  return list(range(n,0,-1))
#This does the same thing, but uses the range() method to start at the input number, stop at 0, stepping -1

## Given human years, how old are your kitten and puppy?

def human_years_cat_years_dog_years(human_years):
  # my_collection = []
  # my_collection[0] = human_years
  # if (human_years)
  pass

## Return count of all vowels in a given string. 'Y' excluded.  If no vowels, return 0.

def get_count(sentence):
  count  = 0

  for i in sentence.lower():
    if (i == 'a' or i == 'e' or i == 'i'or i == 'o'or i == 'u'):
      count+=1
  return count

## Return sum of 2 smallest number in a passed list

def sum_two_smallest_numbers(numbers):
  numbers.sort()
  return sum([numbers[0],numbers[1]])

## Return an abbreviated name. Two letters with a period separating A.G

def abbrev_name(name):
  split_name = name.upper().split()
  return "{fl}.{ll}".format(fl=split_name[0][0], ll=split_name[1][0])

## If Beast and Dish have the same first and last letter, return True. Else, return False.

def feast(beast, dish):
  return (beast[0] == dish[0] and beast[-1] == dish[-1])

## To be Senior, first int in pair must be equal or greater than 55, AND second int greater than 7

def open_or_senior(data):
  new_data = []
  for player in data:
    if (player[0] >= 55 and player[1] > 7):
      new_data.append("Senior")
    else:
      new_data.append("Open")
  return new_data

#HEY ANTHONY! You could also use the List Comprehension shortcut and just embed a For Loop inside.

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

## Given a 2D List, First is passengers getting on, Second is passengers getting off. Return number still left on bus after last stop

def number(bus_stops):
  people_left = 0
  for stop in bus_stops:
    people_left += stop[0]-stop[1]
  return people_left

#HEY ANTHONY! The above snippet uses List Comprehension with a For Loop inside. 
#"Perform this operation" for "each stop" in "array list of bus_stops"

def number(bus_stops):
  return sum([stop[0] - stop[1] for stop in bus_stops])

## Given 2 inputs, return who wins in Rock Paper Scissors

def rps(p1, p2):
    if p1 == p2:
      return "Draw!"
    elif (p1 == 'siccors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'rock' and p2 == 'scissors'):
      return "Player 1 won!"
    else:
      return "Player 2 won!"

#HEY ANTHONY! The one below uses a dictionary so that the argument passed in is checked against the value after the colon.
#You subtract the 2 from each other and Voila! You get the index of the result. 

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

## Given a string of words, return the length of the shortest word(s).

def find_short(s):
  return min(len(word) for word in s.split())
  
## Given a string of digits, replace < 5 with 0, replace >=5 with 1

def fake_bin(x):
  binary = []
  for num in x:
    if int(num) >= 5:
      binary.append("1")
    else:
      binary.append("0")
  return "".join(binary)

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

#HEY ANTHONY! I'm pretty sure you were trying to do this. Just couldn't figure out how to write it. 
#You're going to join together the result of the loop with an empty string. 

## Given a float representing speed in km/h, return integer representing mph

def cockroach_speed(s):
    return int(s * 27.777778)

def cockroach_speed(s):
    return s // 0.036

#HEY ANTHONY! Rather than converting it to an integer, there is a way to round to the nearest whole integer
#using this operator. Gets the same result without invoking a constructor. 

## Given an array of integers AND string digits, return the sum

def sum_mix(arr):
  return sum([int(num) for num in arr])

## Given an integer, Mulitply by 8 if integer is even, else Multiply by 9

def simple_multiplication(number):
  return number*8 if (number%2 == 0) else number*9

## If each dragon takes 2 bullets to kill, return True if we have enough bullets. Else return False

def hero(bullets, dragons):
  return bullets/2>=dragons

## Given a "Triangle of Consecutive Odd Numbers", Calculate the sum of the nth row of the triangle 

# 1 --> 1
# 2 --> 3+5 = 8
# 3 --> 7+9+11=27

def row_sum_odd_numbers(n):
  return sum(range(n*(n-1)+1, n*(n+1), 2))

## Remove smallest int from list, return the list. Note: do not mutate original list. 

def remove_smallest(numbers):
  if len(numbers) == 0:
    return
  copied_list = numbers.copy()
  copied_list.remove(min(copied_list))
  return copied_list

def remove_smallest(numbers):
  if len(numbers) == 0:
    return
  numbers.remove(min(numbers))
  return numbers

## Given 2 strings with letters a-z, Return a NEW sorted string (the longest possible) containing UNIQUE letters from s1 OR s2

def longest(a1, a2):
  long_string = a1+a2
  print(long_string)
  return ''.join(sorted(set(long_string)))

print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))