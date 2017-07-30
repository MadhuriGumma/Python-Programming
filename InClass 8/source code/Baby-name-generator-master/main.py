__author__ = 'himanabdollahpouri'

import NameGenerator as ng
import InputValidator as iv


gender = raw_input("Do you want boys names or girls names? b for boys and g for girls ")

# Validating the entered gender in order to only accept 'g' or 'b'
while iv.validateGender(gender):
    gender = raw_input("Wrong input! Please either enter b or g")

minL = input('Enter minimum Length for the names: ')
while iv.validateMinimumLength(minL):
    minL = input('Min length should be at least 1. Enter minimum Length for the names: ')


maxL = input('Enter maximum Length for the names: ')
while iv.validateMaximumLength(maxL):
    maxL = input('Too big! Enter smaller length! less than 20! Enter maximum Length for the names: ')

order = input('Enter the markove model order: ')
while iv.validateOrder(order):
    order = input('Please set the order higher than zero. Enter the markove model order: ')

count = input('how many names you want? ')
while iv.validateCount(count):
    count = input('Are you kidding me?!I am too tired to generate all of these names! select a smaller number. how many names you want? ')


# Calling the generateNewNames of NameGenerator
ng.generateNewNames(minL,maxL,order,count,str(gender))






