def fibonacci_generator(n=None):
    a, b = 0, 1
    count = 0
    
    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1

def fibonacci_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence[:n]

def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

class Fibonacci:
    def __init__(self, max_value=None, max_count=None):
        self.max_value = max_value
        self.max_count = max_count
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.max_count and self.count >= self.max_count:
            raise StopIteration
        
        if self.max_value and self.a > self.max_value:
            raise StopIteration
        
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return current

def is_fibonacci_number(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

def get_user_input():
    print("=== Fibonacci Generator ===")
    print("Choose an option:")
    print("1. Generate first N Fibonacci numbers")
    print("2. Generate Fibonacci numbers up to a maximum value")
    print("3. Check if a number is Fibonacci")
    print("4. Get nth Fibonacci number (recursive)")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            n = int(input("How many Fibonacci numbers to generate? "))
            return choice, n
        
        elif choice == 2:
            max_val = int(input("Enter maximum value: "))
            return choice, max_val
        
        elif choice == 3:
            num = int(input("Enter number to check: "))
            return choice, num
        
        elif choice == 4:
            n = int(input("Enter position n (0-indexed): "))
            return choice, n
        
        else:
            print("Invalid choice! Please enter 1-4.")
            return None, None
            
    except ValueError:
        print("Please enter valid integers!")
        return None, None

def main():
    choice, value = get_user_input()
    
    if choice is None:
        return
    
    if choice == 1:
        print(f"\nFirst {value} Fibonacci numbers:")

        fib_gen = fibonacci_generator(value)
        print(list(fib_gen))
   
        print(f"\nUsing list method: {fibonacci_list(value)}")
    
    elif choice == 2:
        print(f"\nFibonacci numbers up to {value}:")
        fib_class = Fibonacci(max_value=value)
        result = list(fib_class)
        print(result)
        print(f"Total numbers generated: {len(result)}")
    
    elif choice == 3:
        if is_fibonacci_number(value):
            print(f"\n{value} IS a Fibonacci number!")
        else:
            print(f"\n{value} is NOT a Fibonacci number!")
    
    elif choice == 4:
        if value < 0:
            print("Please enter a non-negative number!")
        elif value > 35:
            print("Warning: Recursive method is slow for n > 35")
            proceed = input("Do you want to continue? (y/n): ").lower()
            if proceed != 'y':
                return
        
        try:
            result = fibonacci_recursive(value)
            print(f"\nThe {value}th Fibonacci number is: {result}")
        except RecursionError:
            print("Recursion limit exceeded! Use generator method for large n.")

if __name__ == "__main__":
    main()
    while True:
        again = input("\nDo you want to run again? (y/n): ").lower()
        if again == 'y':
            main()
        else:
            print("Thank you for using Fibonacci Generator!")
            break