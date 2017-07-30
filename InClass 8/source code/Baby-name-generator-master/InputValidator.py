__author__ = 'himanabdollahpouri'
def validateGender(x):
    try:
        return x.lstrip()!='b' and x.lstrip()!='g'
    except ValueError:
        return False
def validateOrder(x):
    try:
        return x<1
    except ValueError:
        return False
def validateMinimumLength(x):
    try:
        return x<1
    except ValueError:
        return False

def validateMaximumLength(x):
    try:
        return x>20
    except ValueError:
        return False
def validateCount(x):
    try:
        return x>1000
    except ValueError:
        return False