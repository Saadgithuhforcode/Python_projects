import random
import time
operations = ['+', '-', '*',]

Max_bound = 12
Min_bound = 3
Total_problems = input("How many problems do you want to solve? ")
if Total_problems.isdigit():
    Total_problems = int(Total_problems)
else:
    print("Invalid input. Please enter a number.")
    exit()

def generate_problem():
    num_1 = random.randint(Min_bound, Max_bound)
    num_2 = random.randint(Min_bound, Max_bound)
    operation = random.choice(operations)
    
    expr = f"{num_1} {operation} {num_2}"
    answer = eval(expr)
    # when using eval, we need to use strings.
    return expr, answer


wrong = 0

input("Press Enter to start the challenge...")
print("----------------------------------------")

start_time = time.time()

for i in range(Total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input(f'problem {i+1}: {expr} = ')
        if guess == str(answer):
            print("Correct!")
            break
        wrong += 1  
end_time = time.time()
print("----------------------------------------")
total_time = round(end_time - start_time, 2)
if total_time > 60:
    minutes = total_time // 60
    seconds = round(total_time % 60, 2) 
    print(f'It took you {minutes} minutes and {seconds} seconds to complete the challenge with {wrong} wrong answers!')

else:
    print(f'Good boy, you finished the challenge in {total_time} seconds with {wrong} wrong answers!')