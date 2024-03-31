def convert_string_to_float(element):
    ele_list=element.split(" ")
    string=ele_list[1]
    try:
        return float(string)
    except ValueError:
        print("Error: Cannot convert '{}' to float.".format(string))
        return None

