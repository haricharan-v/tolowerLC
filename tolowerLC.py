def lower_case_converter(user_input):
    mod_user_input = user_input.lower()
    return mod_user_input


str_usr_inp = input("Input a word or phrase for lowercase conversion: ")
function_call1 = lower_case_converter(str_usr_inp)
print(function_call1)
