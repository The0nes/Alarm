HOURS = int(input("what hour are you going to bed:"))
MINUTES = int(input("what min is it:"))


if MINUTES >= 40:
    MINUTES -= 40

elif MINUTES <= 39:
    HOURS -= 1
    MINUTES -= 40

if HOURS < 0:
    HOURS = 23
   
if MINUTES < 0:
    MINUTES += 60

 
print(HOURS,":",MINUTES)
