def print_menu(title, options):
    print(f"\n{title}")
    for i, option in enumerate(options):
        print(f"{i}. {option}")
    print()

def get_input(prompt):
    return input(f"{prompt}: ")

def print_error_message(message):
    print(f"Error: {message}")
