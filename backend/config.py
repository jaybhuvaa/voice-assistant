import re

def isValidFormat(text):
    rollno = re.compile("^it [0-9]{1,3}$")

    if rollno.match(text):
       return True
    else:
        return False

# print(isValidFormat("IT012"))
# print(isValidFormat("it012"))
def isInRange(mk):
    min_marks=0
    max_marks=36
    
    if min_marks <= mk <= max_marks:
        return True
        print("in range")
    else:
        return False
        print("not in range")    
        
# isInRange(-1)
# isInRange(0)
# isInRange(25)
# isInRange(36)
# isInRange(56)
    