# Two list to key value pair
def two_list_to_dict(l1,l2):
    result={}
#Check length of the list are equal:
    if len(l1)==len(l2):
        result={l1[i]:l2[i] for i in range(len(l2))}
        return result
    else:
        return "The List should be equal"

