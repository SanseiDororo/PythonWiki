import streamlit as st


def functions():
    st.header('Functions in Python')
    st.write("")
    st.write('''
            This section covers most important segments of functions in Python. 
    
    ''')
    st.write("")
    
    st.write("")
    st.write("")
    
    with st.expander('Basics'):
        st.write('''
            Functions are callables which execute predefined set of code under it's own scope. 
            They can be parameterized. When we call a function with certain parametres, these parametres become arguments 
            of the given function. 
            
            Functions are Python's first class citizens which means they can be passed as parametres to 
            other functions or return another function. This functions are called higher order functions.
            [Functools](https://docs.python.org/3/library/functools.html) module stores various high-order
            function to perform specific tasks.

            Example: Return maximum value of an iterable with the reduce high level function from
            the functools module (built-in max function would do just the same).

                from functools import reduce
                a_list = [1,7,89,212]
                reduce(lambda x, y: x if x > y else y, a_list)
                

            

            Functions can take positional arguments which may or may have not default value. For
            example (def a_func(a,b=20)). We can pass a tuple of remaining positional arguments to 
            function with *args. 

            Functions can as-well take keyword arguments which are returned as a dictionary of key-value
            pairs. Keyword parametres are defined by **kwargs. You can call *args and **kwargs as you like.

            ''')
        st.write('')    
        st.write('''

            | Positional Arguments                  | Keyword Arguments                            |
            |---------------------------------------|----------------------------------------------|
            | Can have default value                | Can have default value                       |
            | *args collects remaining values       | **kwarg collect key-value arguments          |
            | * end of positional arguments         |                                              |
            

            ''')
        st.write('') 
        st.write('''
            [Code Sample:](https://colab.research.google.com/drive/1HrwIlNfjwxE5XohQcK49pB3dvIR6MrAJ?usp=sharing)
        
        ''')

    with st.expander('Documentation And Annotation'):
        st.write('''
            First line of every function, if it is a string, serves for the documentation purposes.
            One or multiline string gets stored into .__doc__ property of the function objects. 
            This helps anybody using function to know it's puprose and the mechanism. Docstring can be
            accessed with help() funtcion or by calling the objec.__doc__ property.

            We can as-well clarify parametres and function's returns with annotations. Annoations
            can be created after: for each parameter and after -> for returns. For example:

                def func_doc(a: 'A beautiful string', b:'int') -> 'str a multiplied b times':
                    return(a*b)

            Functions have properties and methods. We can inspect all the attributes that are available
            for the certain function with the dir() method. For example:

                dir(help)

            [PEP 257 - Docstring Convenctions](https://peps.python.org/pep-0257/)

            [PEP 3107 - Function Annotations](https://peps.python.org/pep-3107/)    
        
        ''')

    with st.expander('Anonymous Functions'):
        st.write('''
            Anonymous functions in Python are single line expressions initialised with
            the keyword lambda. They can be stored in a variable or used as a parameter
            of another function. They can use only single expresseion and cannot be annotaded.

            Example:

                lambda x: x ** 3

                
        
        ''')

    with st.expander('Decorators'):
        st.write('''
            
                
        
        ''')

    