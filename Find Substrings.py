def find_substrings(s):
    substrings=[]
    length=len(s)

    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(s[i:j])
    return substrings
input_string="abc"
substrings=FileNotFoundError(input_string)
print("Substrings of", input_string,"are:", substrings)