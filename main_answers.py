def l_1():
    ## return the string 'Hello World'
    return 'Hello World'

def l_2(a, b):
    ## return a + b
    return a + b

def l_3(list):
    ## return only the third element from the list
    return list[2]

def l_4(list):
    # return the list sorted alphabetically
    return sorted(list)

def l_5(list):
    # append 'Hello' to the list
    list.append('Hello')
    return list

def l_6(dict):
    # add the value 'World' to the key 'Hello'
    dict['Hello'] = 'World'
    return dict

def l_7():
    # create a dictionary that resolves "One" as 1
    # dict["One"] + dict["Two"] == dict["Three"]
    dict = {"One": 1, "Two": 2, "Three": 3}
    return dict

def l_8(list):
    # change every item in the list to be 'EIGHT'
    newlist = []
    for item in list:
        newlist.append('EIGHT')
    return newlist

def l_9(list):
    # change every item in the list if it is a number to 'NINE'
    newlist=[]
    for item in list:
        if str(item).isdigit():
            newlist.append('NINE')
        else:
            newlist.append(item)
    return newlist

def l_10(a, b):
    ## introduce module
    return a % b

def l_11(list):
    #use modulo to return every odd element of the list
    # TIP: for item in range(len(list))
    #    :   print(list[item])
    newlist = []
    for item in range(len(list)):
        if (item + 1) % 2 == 1:
            newlist.append(list[item])
    return newlist

def l_12(list):
    #remove every list element that starts with 'A', 'a', 'B', or 'b'
    newlist = []
    for item in list:
        if item[0].lower() == 'a' or item[0].lower() == 'b' or item[0].lower() == 'c':
            continue
        newlist.append(item)
    return newlist

def l_13():
    ## intro to datetime
    ## return day-month-year (23-02-2019)
    from datetime import date
    return date.today()

def l_14():
    ## formatting datetime
    ## return saturday 17, june, 2019
    ## return "Tuesday, 19, November 2019" -- all numbers are zero padded
    ## TIP: use datetime.datetime.strftime()
    ## Reference http://strftime.org/
    from datetime import date
    today = date.today().strftime("%A %d, %B %Y")
    return today

def l_15():
    from os.path import abspath, dirname
    ## intro to os
    ## return the absolute file path to this directory of this file
    ## TIP: look into __file__ and os.abspath
    return dirname(abspath(__file__))

def l_16():
    from os.path import abspath, dirname
    from os import listdir
    ## get a directory listing of the dir this file is in
    return listdir(dirname(abspath(__file__)))

def l_17(csv_string):
    ## return comma seperated values as a list
    return csv_string.split(',')
