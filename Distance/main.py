#!/usr/lib/python3.3

import os
#from decimal import Decimal

line_blank = "  :" + ' '*74 + ":"
line_dashed = "  :" + '-'*74 + ":"

pad = ' '*19

prompt_distance = "How far was the activity pursued? "
prompt_rate = "At what speed was the activity pursued? "
prompt_hours = "For how many hours was the activity pursued? "
prompt_minutes = "For how many minutes was the activity pursued? "
prompt_seconds = "For how many seconds was the activity pursued? "
prompt_info = ">>> "

result_set = []

title_distance = "  :" + " " * 29 + "<<< Distance >>>" + " " * 29 + ":"
title_rate = "  :" + " " * 31 + "<<< Rate >>>" + " " * 31 + ":  "
title_time = "  :" + " " * 31 + "<<< Time >>>" + " " * 31 + ":  "
title_cols = "  :" + " " * 12 + "Distance" + " " * 16 + "Rate" + " "* 16 + "Time" + " " * 14 + ":"
title_seps = "  :" + " " * 12 + "--------" + " " * 16 + "----" + " "* 16 + "----" + " " * 14 + ":"

distance = 0.0
rate = 0.0
time = 0.0

def cls():
    os.system("cls")
#    print("\x1B[2J")

def dummyProc(something):
    pass
    
def GetRate():
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if util_isNumber(rate):
                return float(rate)
            else:
                print(rate + " is not a valid rate of speed.  Press any key to continue.")
                rate = input()
        else:
            print("You must enter a valid number")

def GetSolutionType():

    tries = 0
    prompt = "Are you looking for [d]istance, [r]ate or [t]ime? \n  > "

    err_msg = " is not a valid 'distance = rate * time' problem.  Please press any key to continue."

    fail_msg = "\n\n\n" + " "*30 + "Three strikes you're out!"

    while tries < 3:
        tries += 1
        cls()
        for i in range(30): print()
        dummyProc(i)

        sol_type = input(prompt)

        if len(sol_type) > 0:
            if sol_type.lower() in("distance", "rate", "time"):
                return sol_type[0].lower()
            elif sol_type.lower() in("d", "r", "t"):
                return sol_type.lower()
            else:
                sol_type = input("\n"" + sol_type + """ +  err_msg)
        else:
            return 0 #empty input = quit

    tries = input(fail_msg)
    return 0

def GetTime():

    got_time = 0
    thisTime = 0
    while not got_time:
        hours = input(prompt_info + prompt_hours)
        if len(hours) == 0:
            got_time = 1 
        else:
            if util_isNumber(hours):
                got_time = 1
                thisTime = int(hours)*60*60
            else:
                print(hours + " is not a valid number of hours.  Press any key to continue.")
                hours = input()

    got_time = 0
    while not got_time:
        minutes = input(prompt_info + prompt_minutes)
        if len(minutes) == 0:
            got_time = 1
        else:
            if util_isNumber(minutes):
                got_time = 1
                thisTime += int(minutes)*60
            else:
                print(minutes + " is not a valid number of minutes.  Press any key to continue.")
                minutes = input()

    got_time = 0
    while not got_time:
        seconds = input(prompt_info + prompt_seconds)
        if len(seconds) == 0:
            got_time = 1
        else:
            if util_isNumber(seconds):
                got_time = 1
                thisTime += int(seconds)
            else:
                print(seconds + " is not a valid number of minutes.  Press any key to continue.")
                seconds = input()

#thisTime = float(thisTime)/60/60
             
    return thisTime # = Total seconds

def util_inStr(string, substring):
    "Reminder: the caller must check for a return value of -1 (not found)"
    loc = -1 #--> Because Python starts counting at zero, search_string
#                 could be at the zeroth position.  Bah!

    string = str(string) #--> In case it ain't a string!
    substring = str(substring) #--> Ditto

#    print('string = ' + string + ", substring = " + substring)
    for char in string:
        loc += 1 # Starts us off at position zero
        if char == substring[0] and substring == string[loc:loc + len(substring)]:
            return loc

    return -1 # substring not in string

def util_isNumber(string):

    string = str(string) #-> Just in case...
    decimal_counter = 0

    for char in string:
        if char == ".":
            decimal_counter += 1
            if decimal_counter > 1:
                return 0
        elif char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return 0

    return 1

def util_roundFractionalsToOne(fractionals):
    fractionals = str(fractionals)
    if len(fractionals) > 1:
        if int(fractionals[0]) < 9:
            while len(fractionals) > 2:
                lastDigit = int(fractionals[-1])
                if lastDigit > 4:
                    fractionals = str(int(fractionals) + 10 - lastDigit)
                fractionals = fractionals[:len(fractionals) - 1]
            if int(fractionals[0]) < 9 and int(fractionals[1]) < 4:
                fractionals = int(fractionals[0]) + 1

    return fractionals

def util_listToString(some_list):
    retVal = ""
    for char in some_list:
        retVal += str(char)

    return retVal

def util_formatNumber(value, number_of_decimal_places = 0, commas_desired = 0):

    #==> Check that the numeric inputs are valid
    if not util_isNumber(value):
        return "Error: " + str(value) + " is not a number"
    if not util_isNumber(number_of_decimal_places):
        return "Error: " + str(number_of_decimal_places) + " is not a number"
    if not util_isNumber(commas_desired):
        return "Error: commas = " + str("'" + commas_desired + "'") + "? commas must be either 0 (No) or not 0 (Yes)"

#-------------------------------------------------------------------------------------------------

    i_dec_places    = int(number_of_decimal_places)
    i_commas        = int(commas_desired)

    number          = str(value)

    integer_part    = ""
    fractional_part = ""

    dec_loc = util_inStr(number, ".")
    print("dec_loc = " + str(dec_loc))


    if dec_loc == -1:
        integer_part = number
    elif dec_loc == 0:
        integer_part = "0"
        fractional_part = number[1:]
    else:
        integer_part    = number[:dec_loc]
        fractional_part = number[dec_loc + 1:]

    print("i_dec_places = " + str(i_dec_places))

#-------------------------------------------------------------------------------------------------

    diff = i_dec_places - len(fractional_part)

    if i_dec_places > 0 and diff > -1: number += '0' * diff

    if i_dec_places > 0 and diff < 0:
        fracts_to_keep = fractional_part[:diff]
        if fracts_to_keep[-1] != '9': #--> only round if last keeper is less than 9
            fracts_to_round = fractional_part[diff:]
            if len(fracts_to_round) > 1:
                fracts_to_round = util_roundFractionalsToOne(fracts_to_round)
            if int(fracts_to_round) > 4:
                fracts_to_keep = str(int(fracts_to_keep) + 1)

        number = (integer_part + '.' + fracts_to_keep)

    if i_dec_places == 0:
        if len(fractional_part) > 0:
            test_dec = util_roundFractionalsToOne(fractional_part)
            #print("n = " + number, "t =" + test_dec, "i = " + integer_part, "f =" + fractional_part)
            if int(test_dec) > 4: integer_part = str(int(integer_part) + 1)
        number = integer_part

    if i_commas:
        integer_part = "0"
        fractional_part = "0"
        dec_loc = util_inStr(number, ".")

        if dec_loc == -1:
            integer_part = number
        elif dec_loc == 0:
            integer_part = "0"
            fractional_part = number[1:]
        else:
            integer_part = number[:dec_loc]
            fractional_part = number[dec_loc + 1:]

        if len(integer_part) > 3:
            commad = ""
            templist = list(integer_part)
            templist.reverse()
            integer_part = util_listToString(templist)
            while len(integer_part) > 3:
                commad += integer_part[0:3] + ','
                integer_part = integer_part[3:]
            commad += integer_part
            templist = list(commad)
            templist.reverse()
            integer_part = util_listToString(templist)

        if dec_loc == -1:
            number = integer_part
        else:
            number =  integer_part + '.' + fractional_part

    return number    
    
def PopScreen(title, output_line = []):
    cls()
    print()
    print(line_dashed)
    print(line_blank)
    print(title)
    print(line_blank)
    print(line_dashed)
    print(line_blank)
    print(title_cols)
    print(title_seps)
#   print("  :          1         2        3")
#   Print("  :0123456789012345678901234567890")

#############    trips = 0   


    # ==> Populate the matrix with the calculated info
    for i in result_set: # result_set is a list of lists...
        disp = (pad + str(i[0])[:14])
        disp += (pad + str(i[1])[:14])
        disp += (pad + str(i[2])[:14])
        disp += " "*14
        print("  :" + disp + ":")

    #==> Populate the matrix with the info we're working on:
    if len(output_line) > 0:
        disp = (pad + str(output_line[0]))[len(output_line[0]) - 1:]
        disp += (pad + str(output_line[1]))[len(str(output_line[1])) - 1:]
        disp += (pad + str(output_line[2]))[len(str(output_line[2])) - 1:]
        disp += " " * 14
        print("  :" + disp + ":")

    for i in range(29-len(result_set)):
        print(line_blank)

    print(line_dashed)
    print()

def SolutionForDistance():
    '''
        output_line[0] = distance
        output_line[1] = rate
        output_line[2] = time
    '''
    PopScreen(title_distance)

    output_line = ["?", "?", "?"] #--> Distance = Rate * Time
    rate = GetRate()
    output_line[1] = util_formatNumber(rate, 2, 1)

    PopScreen(title_distance, output_line)

    #Get_Time()
    #Calculate distance
    time = GetTime()
    output_line[2] = util_formatNumber(float(time)/60/60, 2, 1)
    PopScreen(title_distance, output_line)
    input(prompt_info)

def SolutionForRate():
    PopScreen(title_rate)

def SolutionForTime():
    PopScreen(title_time)

def SolveProblem(sol_type):

    if sol_type == "d":
        SolutionForDistance()
    elif sol_type == "r":
        SolutionForRate()
    elif sol_type == "t":
        SolutionForTime()
    else:
        cls()
        quit()

def util_InStr(string, substring):
    "Reminder: the caller must check for a return value of -1 (not found)"
    loc = -1 #--> Because Python start counting at zero, search_string
#                 could be at the zeroth position.  Bah!

    string = str(string) #--> In case it ain't a string!
    substring = str(substring) #--> Ditto

    for char in string:
        loc += 1 # Starts us off at position zero
        if char == substring[0] and substring == string[loc:loc + len(substring)]:
            return loc
 
    return -1 # substring not in string

def util_IsInt(value):
    if util_isNumber(value):
        if float(value) % int(value) == 0.0:
            return 1

    return 0

def main():
    SolveProblem(GetSolutionType())

if __name__ == '__main__':
    main()
