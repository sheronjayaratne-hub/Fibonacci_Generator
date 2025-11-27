import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import FibonacciGenerator as fib

class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Generator App")
        self.root.geometry("700x600")
        self.root.configure(bg='#f5f5f5')
        
        # Create main container
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_label = tk.Label(main_frame, 
                               text="Fibonacci Sequence Generator", 
                               font=('Arial', 16, 'bold'),
                               fg='#2c3e50',
                               bg='#f5f5f5')
        header_label.pack(pady=(0, 20))
        
        # Input Section
        input_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="15")
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Method selection
        ttk.Label(input_frame, text="Select Method:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.method_var = tk.StringVar(value="list")
        methods = [("Generate List", "list"), ("Use Generator", "generator"), ("Use Class", "class")]
        
        for i, (text, value) in enumerate(methods):
            ttk.Radiobutton(input_frame, text=text, variable=self.method_var, 
                           value=value).grid(row=0, column=i+1, sticky=tk.W, padx=(0, 15))
        
        # Input type
        ttk.Label(input_frame, text="Input Type:").grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(15, 0))
        self.input_type_var = tk.StringVar(value="count")
        ttk.Radiobutton(input_frame, text="Count", variable=self.input_type_var, 
                       value="count", command=self.toggle_input).grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(input_frame, text="Max Value", variable=self.input_type_var, 
                       value="max_value", command=self.toggle_input).grid(row=1, column=2, sticky=tk.W)
        
        # Value input
        ttk.Label(input_frame, text="Value:").grid(row=2, column=0, sticky=tk.W, padx=(0, 10), pady=(15, 0))
        self.value_entry = ttk.Entry(input_frame, width=15, font=('Arial', 11))
        self.value_entry.grid(row=2, column=1, sticky=tk.W, pady=(15, 0))
        self.value_entry.insert(0, "10")
        
        # Check Fibonacci option
        self.check_var = tk.BooleanVar()
        ttk.Checkbutton(input_frame, text="Check if Fibonacci number", 
                       variable=self.check_var).grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=(15, 0))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Button(button_frame, text="Generate Sequence", 
                  command=self.generate_sequence).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Clear Results", 
                  command=self.clear_results).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Check Number", 
                  command=self.check_number).pack(side=tk.LEFT)
        
        # Results Section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(results_frame, 
                                                     height=15, 
                                                     font=('Consolas', 10),
                                                     wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to generate Fibonacci sequence...")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, pady=(10, 0))
    
    def toggle_input(self):
        pass
    
    def generate_sequence(self):
        try:
            value = int(self.value_entry.get())
            method = self.method_var.get()
            input_type = self.input_type_var.get()
            
            self.results_text.delete(1.0, tk.END)
            
            if input_type == "count":
                if value <= 0:
                    messagebox.showerror("Error", "Please enter a positive number!")
                    return
                
                self.results_text.insert(tk.END, f"First {value} Fibonacci numbers:\n")
                self.results_text.insert(tk.END, "="*40 + "\n")
                
                if method == "list":
                    sequence = fib.fibonacci_list(value)
                    self.results_text.insert(tk.END, f"Method: fibonacci_list({value})\n")
                
                elif method == "generator":
                    sequence = list(fib.fibonacci_generator(value))
                    self.results_text.insert(tk.END, f"Method: fibonacci_generator({value})\n")
                
                elif method == "class":
                    fib_class = fib.Fibonacci(max_count=value)
                    sequence = list(fib_class)
                    self.results_text.insert(tk.END, f"Method: Fibonacci(max_count={value})\n")
                
                # Display sequence
                self.results_text.insert(tk.END, f"\nSequence: {sequence}\n")
                self.results_text.insert(tk.END, f"\nTotal numbers: {len(sequence)}\n")
                
            else:  # max_value
                if value < 0:
                    messagebox.showerror("Error", "Please enter a non-negative number!")
                    return
                
                self.results_text.insert(tk.END, f"Fibonacci numbers up to {value}:\n")
                self.results_text.insert(tk.END, "="*40 + "\n")
                
                fib_class = fib.Fibonacci(max_value=value)
                sequence = list(fib_class)
                
                self.results_text.insert(tk.END, f"Method: Fibonacci(max_value={value})\n")
                self.results_text.insert(tk.END, f"\nSequence: {sequence}\n")
                self.results_text.insert(tk.END, f"\nTotal numbers: {len(sequence)}\n")
            
            # Additional info
            self.results_text.insert(tk.END, f"\nGolden Ratio approximation: {self.calculate_golden_ratio(sequence)}\n")
            
            self.status_var.set(f"Successfully generated {len(sequence)} Fibonacci numbers")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def check_number(self):
        """Check if a number is in Fibonacci sequence"""
        try:
            value = int(self.value_entry.get())
            
            is_fib = fib.is_fibonacci_number(value)
            result_text = f"Number {value} "
            result_text += "IS a Fibonacci number!" if is_fib else "is NOT a Fibonacci number"
            
            # Show recursive calculation for smaller numbers
            if value <= 35 and is_fib:
                try:
                    # Find which position it is
                    pos = self.find_fibonacci_position(value)
                    recursive_val = fib.fibonacci_recursive(pos)
                    result_text += f"\n\nPosition in sequence: F({pos})"
                    result_text += f"\nRecursive calculation: fibonacci_recursive({pos}) = {recursive_val}"
                except:
                    pass
            
            messagebox.showinfo("Fibonacci Check", result_text)
            self.status_var.set(f"Checked number {value} - {'Fibonacci' if is_fib else 'Not Fibonacci'}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer!")
    
    def find_fibonacci_position(self, num):
        """Find the position of a Fibonacci number in the sequence"""
        a, b = 0, 1
        position = 0
        while a <= num:
            if a == num:
                return position
            a, b = b, a + b
            position += 1
        return -1
    
    def calculate_golden_ratio(self, sequence):
        """Calculate golden ratio approximation from sequence"""
        if len(sequence) >= 3:
            try:
                ratio = sequence[-1] / sequence[-2]
                return f"≈ {ratio:.8f}"
            except:
                return "N/A"
        return "N/A"
    
    def clear_results(self):
        """Clear the results text area"""
        self.results_text.delete(1.0, tk.END)
        self.status_var.set("Results cleared")

def main():
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()