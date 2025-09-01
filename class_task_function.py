print("----------------Task 1-----------------") 
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(3, 5))
print(sum_two_numbers(9,12))
print(sum_two_numbers(6,7))

print("==============Task 2===================")
def square_number(n):
    return n * n

print(square_number(5)) 
print(square_number(7))

print("==============Task 3===================")
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("John") 

print("==============Task 4===================")
def area_of_rectangle(length, width):
    return length * width

print(area_of_rectangle(4, 6)) 

print("==============Task 5===================")
def perimeter_of_square(side):
    return 4 * side

print(perimeter_of_square(5))

print("==============Task 6===================")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))  
print(celsius_to_fahrenheit(25))  
print(celsius_to_fahrenheit(15))

print("==============Task 7==================")

def find_max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
print(find_max_number(10, 25, 15))
print(find_max_number(9, 7, 5))

print("==============Task 8==================")

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(4))  
print(even_or_odd(7))  
print(even_or_odd(1))

print("==============Task 9===================")
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word.lower(): 
        if char in vowels:
            count += 1
    return count
print(count_vowels("apple"))  
print(count_vowels("BANANA")) 

print("==============Task 10===================")
def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
print(multiply_list([1, 2, 3, 4]))    
print(multiply_list([2, 5, 3]))       
print(multiply_list([]))              

print("===============Task 11===================")
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))

print("==============Task 12====================")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))   
print(is_prime(8))   

print("===============Task 13================")
counter = "I am global"

def scope_demo():
    counter = "I am local"
    print(counter)  # Prints local

print(counter)        
scope_demo()    
print(counter)          

print("===============Task 14=================")
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))  

print("===============Task 15================")

def average_of_list(number):
    if len(number) == 0:
        return 0
    return sum_list(number) / len(number)

print(average_of_list([10, 20, 30])) 

print("===============Task 16================")
def factorial(n):
    if n < 0:
        return None  # Invalid input
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

print("===============Task 17================")
def palindrome_check(word):
    word = word.lower()
    return word == word[::-1]

print(palindrome_check("madam"))
print(palindrome_check("hello"))

print("===============Task 18================")
def convert_minutes_to_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours} hour(s) {mins} minute(s)"

print(convert_minutes_to_hours(130))

print("==============Task 19=================")
def find_min(numbers):
    if len(numbers) == 0:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
print(find_min([5, 2, 8, 1, 9])) 
print(find_min([10,11,12,14,15]))

print("================Task 20 ================")
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(1000, 5, 2)) 

print("================Task 21 ================")
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

print(calculator(4, 2, "+")) 
print(calculator(5, 2, "/")) 

print("================Task 22 ==================")
def string_length(text):
    count = 0
    for _ in text:
        count += 1
    return count

print(string_length("Python")) 

print("================Task 23 ==================")
def grade_student(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 40 <= score <= 49:
        return "D"
    elif 30 <= score <= 39:
        return "E"
    elif 0 <= score <= 29:
        return "F"
    else:
        return "Invalid score"

print(grade_student(85))  
print(grade_student(45))

print("===============Task 24 ====================")
def swap_values(a, b):
    return b, a

print(swap_values(3, 7))   

print("===============Task 25 ====================")
count = 0

def scope_counter():
    global count
    count += 1
    print(f"Count: {count}")

scope_counter() 
scope_counter() 
scope_counter() 

print("================Task 26 ===================")
def calculate_bmi(weight, height):
    if height <= 0:
        return "Invalid height"
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(calculate_bmi(70, 1.75))

print("================Task 27 ====================")
def discounted_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount

print(discounted_price(1000, 20))

print("================Task 28 ====================")
def movie_ticket_price(age):
    if age < 12:
        return 500
    elif age < 18:
        return 700
    elif age < 60:
        return 1000
    else:
        return 600

print(movie_ticket_price(65))

print("===============Task 29 =======================")
def shopping_total(prices):
    return sum_list(prices)

print(shopping_total([500, 300, 200]))

print("================Task 30 =======================")
def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print(convert_to_seconds(1, 1, 1))

print("================Task 31 =======================")

def find_median(numbers):
    if len(numbers) == 0:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

print(find_median([1, 3, 5]))     
print(find_median([1, 2, 3, 4])) 

print("================Task 32 =======================")
def parking_fee(hours):
    if hours <= 2:
        return 200
    else:
        extra = hours - 2
        return 200 + extra * 100
print(parking_fee(5)) 

print("================Task 33 ======================")
def word_count(sentence):
    return len(sentence.split())

print(word_count("I love Python programming"))   

print("================Task 34 ======================")
def capitalize_names(names):
    return [name.capitalize() for name in names]

print(capitalize_names(["john", "mary"]))  

print("================Task 35 =======================")
def student_pass_fail(score):
    return "Pass" if score >= 50 else "Fail"

print(student_pass_fail(80)) 
print(student_pass_fail(35))

print("=================Task 36 ======================")
def calculate_fine(daysLate):
    if daysLate <= 5:
        return daysLate * 20
    elif daysLate <= 10:
        return 5 * 20 + (daysLate - 5) * 50
    else:
        return 5 * 20 + 5 * 50 + (daysLate - 10) * 100

print(calculate_fine(7))  
print(calculate_fine(14))  

print("=================Task 37 ======================")
def convert_currency(amount, rate):
    return amount * rate

print(convert_currency(100, 1500))

print("================Task 38 =======================")
def gas_station_bill(liters, price_per_liter):
    return liters * price_per_liter

print(gas_station_bill(150, 250))

print("===============Task 39 ========================")
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print(is_leap_year(2020)) 
print(is_leap_year(1900)) 
print(is_leap_year(2005)) 

print("================Task 40 ===================")
def password_strength(password):
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    is_long = len(password) >= 8
    if has_digit and has_upper and is_long:
        return "Strong"
    else:
        return "Weak"

print(password_strength("Pass1111")) 
print(password_strength("pass"))

print("=================Task 41===================")
def shirt_order(quantity, price_per_shirt, discount_threshold=10, discount_rate=0.1):
    total = quantity * price_per_shirt
    if quantity >= discount_threshold:
        total -= total * discount_rate
    return total

print(shirt_order(12, 2000)) 

print("=================Task 42 ====================")
def find_mode(numbers):
    if len(numbers) == 0:
        return None
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)

print(find_mode([1, 2, 2,2, 2, 2, 2, 3, 3, 3]))

print("================Task 43 ================")
def student_average(scores):
    if len(scores) == 0:
        return 0
    return average_of_list(list(scores.values()))

print(student_average({"math": 80, "english": 70}))   

print("===============Task 44 =================")
def calculate_age(current_year, birth_year):
    return current_year - birth_year

print(calculate_age(2025, 2000)) 


print("===============Task 45 =================")
def salary_after_tax(salary, tax_rate=0.15):
    return salary * (1 - tax_rate)

print(salary_after_tax(100000))

print("===============Task 46 =================")
def water_bill(units):
    if units <= 30:
        return units * 50
    elif units <= 50:
        return 30 * 50 + (units - 30) * 75
    else:
        return 30 * 50 + 20 * 75 + (units - 50) * 100

print(water_bill(80))   

print("===============Task 47 ==================")
def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

print(find_longest_word("I love programming"))

print("================Task 48 ===================")
def banking_withdraw(balance, withdraw_amount):
    if withdraw_amount <= balance:
        return balance - withdraw_amount
    else:
        return "Insufficient funds"

print(banking_withdraw(1500, 1100)) 
print(banking_withdraw(700, 2600))  

print("=================Task 49 ===================")
def calculate_grade_point(score):
    if score >= 70:
        return 5
    elif score >= 60:
        return 4
    elif score >= 50:
        return 3
    elif score >= 45:
        return 2
    elif score >= 40:
        return 1
    else:
        return 0

print(calculate_grade_point(89)) 
print(calculate_grade_point(40)) 

print("===============Task 50 =================")
def weather_advice(temperature, raining):
    if raining:
        return "Take an umbrella"
    elif temperature > 30:
        return "Wear light clothes"
    elif temperature < 15:
        return "Wear a jacket"
    else:
        return "Weather is fine"

print(weather_advice(35, False))  
print(weather_advice(10, False))  
print(weather_advice(20, True))  
print(weather_advice(25, False))    
