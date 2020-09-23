import streamlit as st

#varibale type detector
def Detector(variable,name):
    ans = 'None'

    # if all([i.isdigit() for i in variable]):
    #     variable = variable.apply(lambda x: int(x))

    if variable.dtype != 'object':
        if len(variable.unique())==2:
            ans = 'Binary'
        elif len(variable.unique())<10: #this is dicey
            ans = 'Categorical'
        elif variable.shape[0] == len(variable.unique()):
            ans = 'Identifier'
        else:
            ans = 'Continuous'

    else:
        if len(variable.unique())==2:
            ans = 'Binary'
            mapper = {variable.unique()[0]:0,variable.unique()[1]:1}
            variable = variable.map(mapper)
            st.write('**Modified the feature \'{}\'**'.format(name))
            st.dataframe({'Key':mapper})
        elif variable.shape[0] == len(variable.unique()):
            ans = 'Identifier'
        else:
            ans = 'Categorical'

    return (ans,variable)

