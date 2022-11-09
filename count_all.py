def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    d={}
    q=0
    s=0
    for i in range(len(txt)):
        if txt[i].isalpha():
            q+=1
        if txt[i].isdigit():
            s+=1
    d.setdefault("LETTERS",q)
    d.setdefault("DIGITS",s)

    return d
print(count_all("Hello World"))