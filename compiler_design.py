import ast
from tabulate import tabulate


def error_msg_generator(ID):
    # ID each errors with different numbers and use switch case to print the errors
    switcher = {
        1: "Invalid Data Type! Might be a spelling mistake. Try again.",
        2: "Value doesn't match with data type!",
        3: "Variable already exists! Choose another name."
    }
    print(switcher.get(ID))


def type_matching(val, var_type):
    return type(ast.literal_eval(val)).__name__ == var_type

def string_input_checking(chunk):
    # If ',' not found then returns whole string
    for i in chunk.split(','):
        try:
            ast.literal_eval(i.split('=')[1])
            error_msg_generator(2)
            return
        except ValueError:
            if '=' in i:
                name, val = i.split('=')
                name_list.append(name)
                val_list.append(val)
            else:
                name_list.append(i)
                val_list.append('Null')
    # try:  # Input checking in case of string.
    #     ast.literal_eval(ele.split('=')[1])
    # except :
    #     if var_type != type(ele.split('=')[1]).__name__:
    #         error_msg_generator(2)
    #         return
    #     name_list.append(ele.split[0])
    #     val_list.append(ele.split[1])

def symbol_table_insert(inp):
    if inp.split(' ')[0] not in ('int', 'float', 'str', 'bool'):
        error_msg_generator(1)
        return
    var_type, chunk = inp.split(' ')
    if var_type == 'str':
        string_input_checking(chunk)
    if ',' in chunk:
        tmp = chunk.split(',')
        for ele in tmp:

            if '=' in ele:
                if type_matching(ele.split('=')[1], var_type) is False:
                    # if not isinstance(ele.split('=')[1], var_type):
                    error_msg_generator(2)
                    return
                name, val = ele.split('=')
                if name in name_list:
                    error_msg_generator(3)
                    return
                name_list.append(name)
                val_list.append(val)
            else:
                name_list.append(ele)
                val_list.append('Null')
            type_list.append(var_type)
    else:
        if '=' in chunk:
            string_input_checking(chunk)
            if type_matching(chunk.split('=')[1], var_type) is False:
                error_msg_generator(2)
                return
            name, val = chunk.split('=')
            if name in name_list:
                error_msg_generator(3)
                return
            name_list.append(name)
            val_list.append(val)
        else:
            name_list.append(chunk)
            val_list.append('Null')
        type_list.append(var_type)

    return name_list, val_list, type_list


def remove_data(name):
    try:
        idx = name_list.index(name)
        name_list[idx] = val_list[idx] = type_list[idx] = 'Null'
    except ValueError:
        error_msg_generator()
        # print(f"Wrong Name! Table doesn't contain {name}!")


def update_data(name):
    try:
        idx = name_list.index(name)
        type_list[idx] = input(f'Enter the new type for {name}')
        val_list[idx] = input(f'Enter the new value for {name}')
    except ValueError:
        print("Wrong input given! Try again.")


def display():
    # print(name_list)
    # print(val_list)
    # print(type_list)
    tmp = [[i+1, name_list[i], type_list[i], val_list[i]] for i in range(len(name_list))]
    col_name = ["SL", "NAME", "TYPE", "VALUE"]
    print(tabulate(tmp, headers=col_name, tablefmt='fancy_grid'))


if __name__ == '__main__':
    name_list = []
    val_list = []
    type_list = []

    x = True
    while x:
        print("""\nPress 1 to Insert Data:
Press 2 to Remove Data:
Press 3 to Update Data:
Press 4 to Display Data:
Press 5 to exit:\n""")

        x = input("Enter an option: ")
        if x == '1':
            while True:
                data = input("Enter a Data or Type / to exit: ")
                if data == "/":
                    break
                else:
                    symbol_table_insert(data)
        elif x == '2':
            Name = input("Enter name to remove the row: ")
            remove_data(Name)
        elif x == '3':
            update_data(input("Enter Name of the row to update: "))
        elif x == '4':
            display()
        elif x == '5':
            exit()
