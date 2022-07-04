import streamlit as st


def standard_library():
    st.header('Standard Library')
    st.write("")
    st.write('''
            This section covers modules from the Python Standard Library. 
    
    ''')
    st.write("")
    
    st.write("")
    st.write("")
    
    with st.expander('Argparse'):
        st.write('''
        
        Argparse module is parser for CLI arguments, subcommands and options.

        CLI inputs are important if we want to allow users to execute various 
        parametres of the program by providing specific arguments.

        The most common CLI argument is --help which list array of all
        available arguments with description.

        **USAGE**:

        Industry Grade Python Modules 

        Example:

            import argparse

            #Fibonnaci function
            def fib(n): 
                a,b = 0,1   
                for i in range (n): 
                    a, b = b, a+b,  
                return a    
    
            def main(): 
                parser = argparse.ArgumentParser(description='Count Fibonacci') 
    
                #Define groups  
                group = parser.add_mutually_exclusive_group()   
                group.add_argument("-v", "--verbose", action="store_true")  
                group.add_argument("-q", "--quiet", action ="store_true")   
        
                #Define Arguments   
                parser.add_argument('Number', type=int, help='The fibonnaci number you wish to calculate')  
    
                #Optional Argument  
                parser.add_argument("-o", "--output", help="Output result to a fibonacci.txt file.",    
                action="store_true")    
    
                #Grab created arguments 
                args = parser.parse_args()  
    
                result = fib(args.Number)   
        
                if args.verbose:    
                    print(f'The {str(args.Number)} fibonacci number is {result}')   
                elif args.quiet:    
                    print(result)   
                else:   
                    print(f'Fib {str(args.Number)} = {str(result)}')    
    
                if args.output: 
                    f = open("fibonacci.txt", "a")  
                    f.write(str(result)+'newline')  
    
            if __name__ == '__main__':  
                main()  
                
        Resources:
         
        [Module Library](https://docs.python.org/3/library/argparse.html)
            
        [You Tube](https://www.youtube.com/watch?v=q94B9n_2nf0)
        
        ''')

    with st.expander('Inspect'):
         st.write('''

            Inspect module in Python helps you gather additional information about the objects from the observed code.
            There are several available methods which you can use. The list below is not extensive but
            gives a general perspective.

                import inspect

                #Check if object is a method
                inspect.ismethod(obj)

                #Check if object is function
                inspect.isfunction(obj)

                #Check if object is routine
                inspect.isroutine(obj)

                #Retrieve documentation 
                inspect.getdoc(obj)

                #Retrieve comments
                inspect.getcomments(obj)

                #Get module where object is stored
                inspect.getmodule(obj)

                #Check if object is function
                inspect.isfunction(obj)

            Resources:
            
            [Official Documentation](https://docs.python.org/3/library/inspect.html)    

            ''')
    
    with st.expander('Operator'):
         st.write('''
            Operation module offers functions which corresponds to the intrinsic operators in Python.

            For example:
            
                1. a == b // operator.eq(a,b)
                2. a > b // operator.gt(a,b)
                3. a + b // operator.add(a,b)
            

            [Official Documentation](https://docs.python.org/3/library/operator.html)

         ''')
    
    with st.expander('Datetime'):
         st.write('''


         ''')