def get_integer_input(): 
    number = int(input("Enter a integer number: "))
    return number

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main(): 
   number = get_integer_input()
   result = check_even_odd(number)
   print(result)
   
if __name__ == "__main__":
    main()
   