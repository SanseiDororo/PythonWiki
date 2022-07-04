#Dependencies
import streamlit as st


from Intro.intro import intro
from Blocks.building_blocks import building_blocks
from Numeric.numeric import numeric_types
from Functions.functions import functions
from Zen.zen import zen
from Standard.standard import standard_library

the_truth = zen()

def main():
    
    menu = ['Intro', 'Building Blocks', 'Numeric Types', 'Functions','Standard Library']
    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    elif sub_page == 'Building Blocks':
        building_blocks()
    elif sub_page == 'Numeric Types':
        numeric_types()
    elif sub_page == 'Functions':
        functions()
    elif sub_page == 'Standard Library':
        standard_library()
    else:
        pass
    


if __name__ == '__main__':
    main()