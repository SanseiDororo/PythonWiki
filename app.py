#Dependencies
import streamlit as st


from Intro.intro import intro
from Blocks.building_blocks import building_blocks
from Numeric.numeric import numeric_types
from Functions.functions import functions
from Sequences.sequences import sequences
from Zen.zen import zen
from Standard.standard import standard_library
from External.external import external_libraries
from Distributing.distributing import distributing


the_truth = zen()

def main():
    
    menu = ['Intro', 'Building Blocks', 'Numeric Types', 'Functions',
            'Sequences', 'Standard Library', 'External Libraries',
            'Distributing',
            ]
    sub_page = st.sidebar.selectbox('Menu', menu)

    if sub_page == 'Intro':
        intro()
    elif sub_page == 'Building Blocks':
        building_blocks()
    elif sub_page == 'Numeric Types':
        numeric_types()
    elif sub_page == 'Functions':
        functions()
    elif sub_page == 'Sequences':
        sequences()
    elif sub_page == 'Standard Library':
        standard_library()
    elif sub_page == 'External Libraries':
        external_libraries()
    elif sub_page == 'Distributing':
        distributing()
    else:
        pass
    


if __name__ == '__main__':
    main()