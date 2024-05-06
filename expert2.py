class HelpDeskExpertSystem:
    def __init__(self):
        self.queries = {
            'printer': "Please try the following steps:\n1. Check if the printer is turned on.\n2. Make sure there is paper in the tray.\n3. Restart the printer and try printing again.",
            'internet': "Please try the following steps:\n1. Check if the Ethernet cable is properly connected.\n2. Restart your router or modem.\n3. Contact your internet service provider if the issue persists.",
            'password': "If you forgot your password, please reset it using the 'Forgot Password' option on the login page."
        }

    def get_solution(self, query):
        return self.queries.get(query.lower(), "I'm sorry, I don't have a solution for that issue.")

    def display_menu(self):
        print("Menu:(problems)")
        print("1. Printer")
        print("2. Internet")
        print("3. Password")
        print("4. Exit")

# Example usage:
expert_system = HelpDeskExpertSystem()
while True:
    expert_system.display_menu()
    user_choice = input("Please select an option (1/2/3/4): ")

    if user_choice == '1':
        solution = expert_system.get_solution('printer')
    elif user_choice == '2':
        solution = expert_system.get_solution('internet')
    elif user_choice == '3':
        solution = expert_system.get_solution('password')
    elif user_choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please select again.")
        continue

    print("Solution:", solution)
    continue_option = input("Do you want to continue? (yes/no): ")
    if continue_option.lower() != 'yes':
        
        break
