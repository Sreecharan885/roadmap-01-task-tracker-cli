# Utility function to split the commands while considering quoted strings as one
def custom_split(command):
    parsed_list = []
    flag = False
    word = ""
    for i in command:
        if i != ' ' and i != '"':
            word += i
        elif i == ' ':
            if flag == False:
                parsed_list.append(word)
                word = ''
            else:
                word += i
        elif i == '"':
            flag = not flag
    if len(word) != 0:
        parsed_list.append(word)
    return parsed_list