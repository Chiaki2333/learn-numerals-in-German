#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Github: https://github.com/Chiaki2333/learn-numerals-in-German
version: 1.0
'''

import math

num19 = [
    "null",
    "eines",
    "zwei",
    "drei",
    "vier",
    "fünf",
    "sechs",
    "sieben",
    "acht",
    "neun",
    "zehn",
    ##########################
    "elf",
    "zwölf",
    "dreizehn",
    "vierzehn",
    "fünfzehn",
    "sechzehn",
    "siebzehn",
    "achtzehn",
    "neunzehn"
]

num_zig = [
    "",
    "",
    "zwanzig",
    "dreißig",
    "vierzig",
    "fünfzig",
    "sechzig",
    "siebzig",
    "achtzig",
    "neunzig"
]

# Get the German number from 0 to 19
def get_german_num_0_19(number):
    number = abs(float(number))
    if number<=19:
        if int(number) == 1:
            return "ein"
        else:
            return(num19[int(number)])
    else:
        return("Error:get_german_num_0_19")

# Get the German number from 20 to 99
def get_german_num_20_99(number):
    number = abs(float(number))
    if 20<=number and number<100:
        if int(number)%10 == 0:
            return(num_zig[int(number)//10])
        else:
            return(get_german_num_0_19(int(number)%10) + "und" + num_zig[int(number)//10])
    else:
        return("Error:get_german_num_20_99")

# Get the German number from 100 to 999
def get_german_num_100_999(number):
    number = abs(float(number))
    if 100<=number and number<1000:
        if int(number)%100 == 0:
            return(get_german_num_0_19(int(number)//100) + "hundert")
        else:
            return(get_german_num_0_19(int(number)//100) + "hundert" + get_german_num_20_99(int(number)%100))
    else:
        return("Error:get_german_num_100_999")

# Get the German number from 0 to 999
def get_german_num_0_999(number):
    number = float(number)
    flag = True if number>=0 else False
    number = abs(number)
    
    #print(number)
    if number<20:
        if int(number)==1:
            return "eins"
        else:
            return(get_german_num_0_19(number))
    elif 20<=number and number<100:
        return(get_german_num_20_99(number))
    elif 100<=number and number<1000:
        return(get_german_num_100_999(number))
    else:
        pass
        
if __name__ == "__main__" :
    while True:
        num = input("Please input a non-negative integer(0~999):")
        print(get_german_num_0_999(num))
        print("="*20)
