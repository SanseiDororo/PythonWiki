import streamlit as st

def building_blocks():
    st.header('Python Building Blocks')
    st.write('''
    
        This section covers basic Python building blocks. It
        can serve as a quick Python refresher. Knowing fundamentals is
        always best approach to building complex ontologies.  
    
    ''')
    st.write("")
    st.write("")

    
    with st.expander("Data Typese"):
        st.write('''
            Python has the following built-in data types:

            | Numbers  | Collections            | Callables                 | Singletons        |
            |----------|------------------------|---------------------------|-------------------|
            | Integers | Lists (Sequence)       | User Defined Functions    | None              |       
            | Boleans  | Tuples (Sequence)      | Built-in-Functions        | Not Implemented   |   
            | Complex  | Strings (Sequence)     | Generators                | Elipsis           |   
            | Fractions| Sets                   | Classes                   |                   |   
            |          | Frozen Sets            | Instance Methods          |                   |   
            |          | Dictionaries (Mappings)| Built-in-Methods          |                   |   
            

        ''')
        st.write("")
        st.write("")
        st.write('''
            Everything in Python is an object. Each object type is documented.
            Built-in documentation can be accesed by the help function. 

            For example:

                help(int)
        
        ''')
        
        
    with st.expander("Data mutability"):
        st.write('''    

            Objects in Python fall into the two groups:

            | Mutable     | Immutable                                              |
            |------------ |--------------------------------------------------------|
            | Numbers     | Sets                                                   |
            | Strings     | Lists                                                  |
            | Tuples      | Dictionaries                                           |
            | Frozen Sets | User Defined Classes                                   |
            | U-D Classes | Same as functions                                      |
            

        ''')
    
    with st.expander('Naming Convections'):
        st.write('''
        
            Identifying names in Python are **case-sensitive**. Rules how to use it are precisely
            defined in the [PEP 8](https://peps.python.org/pep-0008/) Style Guide. 

            **CONVENCTIONS**

            * They must star with a letter or the underscore.
            * Can not be reserved words.
            * When identifier starts with single underscore, 
              it means that it is considered as _private object.
            * When identifier starts with double underscore,
              it is used to "mangle" class attributes.
            * When identifier is enclosed with double underscores,
              it means that is reserved system-defined name.  
            *

            
            **PEP 8 Style Guides**


            | Entity    | Convection                                            |
            |----------|--------------------------------------------------------|
            | Packages  | Lowercase, short, no underscores                      |
            | Modules   | Lowercase, short, underscores allowed                 |
            | Classes   | Upper CamelCase                                       |
            | Functions | Lowercase, words separated with underscores           |
            | Variables | Same as functions                                     |
            | Constants | Uppercase, words separated with underscore            |
            

            

        ''')

    with st.expander("Variables"):
        st.write('''
        
         Python is dynamically typed langugae meaning that variables are memory references. 
         They point to the certain addresses in the memory.
         When we create the variable age = 19, we create an object in the memory and
         the reference to this object is variable name i.d. age. In the strict sense age is not
         equal to the 19 but only points or references to the specific memory slot, 
         which holds the object 19. With provided libraries we can count references pointing 
         to the certain memory address.
        
        ''')
        st.write("")
        st.write('''
            In Python we can check the memory address for the specific object with
            the id() function.
        ''')
        memory_input = st.number_input('Please chose the random number', step=1, max_value=100)
        st.write(f'''
            The memory address for your number is:
            {hex(id(memory_input))}
        
        ''')
        st.write("")
        st.write('''
            **VARIABLE EQUALITY**:

            We can check if two variables are referencing the same memory address
            with the **is** identity operator.

            To check equality of the internal object state we use **==** operator.
            It is important to know that this are two very different things.
        
        ''')

    with st.expander('Scopes'):
        st.write('''
           We could define scope as the level of object availability. Every scope level has it's own
           namespace. In Python there is no true cross module or app global scope. 
           The highest scope level is built-in scope which defines objects such as
           True, False, None, print etc. which are available on every level of Python code.

           Built-in scope encloses modules scopes which have their own namespaces. If Python interpreter
           doesn't find reference to a give object on the level of given scope it searches in the enclosing scope
           to find it there. If the object doesn't exist in any scope Python returns name error.

           For example: print is a built-in function which means it is stored on the highest 
           level scope. But we can override it on the module level scope by assigning new object to
           the print reference.

            print = lambda x,y: x+y
            print(5,2) => 7 

        Every python file represents it's own scope defined with the namespace of the file, which
        defines __name__ attribute.
           
            import filename
            filename.__name__ => filename

        Functions creates local scopes which get created when the function is called. For example
        variables and operations exists only inside the function or function scope. When function is 
        called this scope is created.

            def local_scope(a):
                print = (a * 10)
                return print

            local_scope('ten') => tententen...

        Main scopes in Python:

        * Global scope (built-in objects)
        * Module scope (objects inside the module)
        * Local scope (objects inside the functions)
        
        ''')


    with st.expander('Resources'):
        st.write('''
            * [Variable Referencing](https://colab.research.google.com/drive/1iVJ5R5jaI5zmyhofeadwhtvyfpWC6414?usp=sharing)
            * [PEP 8](https://peps.python.org/pep-0008/)
        
        ''')

