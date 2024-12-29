from eightGraph import function_manager

class GraphApp:
    def __init__(self, manager):
        self.manager = manager
        self.index = 0  # Start with the first function

    def start(self):
        func_names = self.manager.get_function_names()

        while True:
            # Get the current function by its index
            func_name = func_names[self.index]
            func = self.manager.get_function_by_name(func_name)

            print("\nWould you like to see the plot of the following function?")
            print(func)  # Print function details

            # Ask the user for input
            user_input = input("Type 'yes' to see the plot, 'next' to skip, or 'exit' to quit: ").strip().lower()

            if user_input == 'yes':
                func.plot()
                self.index = (self.index + 1) % len(func_names)  # Move to the next function
            elif user_input == 'next':
                self.index = (self.index + 1) % len(func_names)
            elif user_input == 'exit':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid input. Please type 'yes', 'next', or 'exit'.")

if __name__ == "__main__":
    app = GraphApp(function_manager)
    app.start()
