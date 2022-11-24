# Functions with outputs

# function
def format_name(f_name, l_name):
    """take first and last name and format it"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("TOM", "SEWELL")

print(formated_string)

format_name()  