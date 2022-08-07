# Programmer: Dani Massa

from random import randint

# This function generates a random 5 digit number.
def random_pin():
    pin = randint(10000, 99999)
    return pin

# This function generates a list of a given length containing
# random 5 digit numbers. 
def generate_random_pins(length):
    List = []
    while len(List) < length:
        pin = random_pin()
        List.append(pin)
    return List
    

### DO NOT DELETE THIS LINE: beg testing

# Uncomment the following lines for testing.
# print("Some randomly generated list of pins of different lengths:")
#print(generate_random_pins(4))
#print(generate_random_pins(20))
# print(generate_random_pins(1))
# print(generate_random_pins(9))

