import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
t_ch = int(input("Enter the no. of character password you want to generate"))
n_u = int(input("Enter the no. of uppercase letter you want in password"))
n_d = int(input("Enter the no. of digit you want in password"))
n_s = int(input("Enter the no. of special symbol you want in password except space"))
n_l = t_ch - (n_u + n_d + n_s)

password = ""

while n_u>0 or n_d>0 or n_s>0 or n_l>0:
    if n_u>0:
        uppercaseLetter =chr(random.randint(65,90))
        password = password + uppercaseLetter
        n_u = n_u - 1
    elif n_l>0:
        lowercaseLetter = chr(random.randint(97,122))
        password = password + lowercaseLetter
        n_l = n_l - 1
    elif n_d>0:
        digit = chr(random.randint(48,57))
        password = password + digit
        n_d = n_d -1
    else:
        symbol = chr(random.randint(33,47) or random.randint(58,64) or random.randint(91,96) or random.randint(123,126) or random.randint(145,149))
        password = password + symbol
        n_s = n_s - 1

password = shuffle(password)

#Ouput
print(password)
