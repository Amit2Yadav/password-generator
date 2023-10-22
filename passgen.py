#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passmap=[letters,numbers,symbols]
password_letter=""
password_number=""
password_symbol=""
total_password=nr_letters+nr_symbols+nr_numbers
for l in range(1,nr_letters+1):
  password_letter+=random.choice(letters)
for l in range(1,nr_numbers+1):
  password_number+=random.choice(numbers)
for l in range(1,nr_symbols+1):
  password_symbol+=random.choice(symbols)
p_list=[]
p_str=""
password_string=password_letter+password_number+password_symbol
for p in password_string:
  p_list+=p
random.shuffle(p_list)
for p in p_list:
  p_str+=p
print(p_str)
  
