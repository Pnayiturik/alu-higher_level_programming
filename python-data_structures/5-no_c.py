#!/usr/bin/python3
def no_c(my_string):
    def remove_letter(string, letter):
        new_string = ''
        for char in string:
            if char != letter:
                new_string += char
        return new_string

    letter = "C"
    return remove_letter(my_string, letter)
