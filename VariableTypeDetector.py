import pandas as pd
import numpy as np

def __init__():
    pass

#varibale type detector
def Detector(variable):
    ans = 'None'
    if variable.dtype == 'object':
        if len(variable.unique())==2:
            ans = 'Binary Cat'
        elif len(variable.unique())<(variable.shape[0]**(0.5)):
            ans = 'Nominal'
        else:
            ans = 'Identifier'
    else:
        if len(variable.unique())==2:
            ans = 'Binary Num'
        else: ans='Continuous'
    return ans

