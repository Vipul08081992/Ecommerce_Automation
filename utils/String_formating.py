#For Add to cart button
#make string lowercase and repalce white space with Dash
def format_string_low_replace(input_string):
    formatted_string = input_string.lower().replace(" ", "-")
    return formatted_string