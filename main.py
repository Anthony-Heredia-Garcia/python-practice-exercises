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
  
print(first_non_consecutive(myList))
      
    
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