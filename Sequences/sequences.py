import streamlit as st


def sequences():
    st.header('Sequences')
    st.write("")
    st.write('''
            This section covers most important aspects of specific type of containers
            called sequences.  
    
    ''')
    st.write("")
    
    st.write("")
    st.write("")
    
    with st.expander('Types'):
        st.write('''

            We have three types of sequences in Python: tuples, lists and strings.
            They share most of the attributes, but they have idiosycratic purpose
            as well. This is overall atributtes list:
            
            |  Tuples       | Lists                  | Strings                   | 
            |---------------|------------------------|---------------------------|
            | indexable     | indexable              | indexable                 |       
            | homo / hetero | homo / hetero          | homogeneous               |    
            | iterable      | iterable               | iterable                  |    
            | indexable     | indexable              | idnexable                 | 
            | immutable     | mutable                | mutable                   |                      
            | fixed length  | arbitrary length       | fixed length              |                      
            | fixed order   | arbitrary order        | fixed order               |
            

            ''')

    with st.expander('Tuples'):
        st.write('''
            Tuples are immutable containers of elements with non-arbitrary positional relevance.
            They can be homogeneous (storing elements of the same type) or heterogeneous
            (storing elements of a different types). Content of a tuple is iterable. 

            According to the non-arbitrary relevance of the elements in the tuple, they are very
            useful for storing various types of data.

            For example:

            * 2D coordinates (x: x axis, y: y axis, z: z axis)
            * Entities (person: name, surname, age | city: name, country, population)

                    #Packing variables into tuple:
                    philosopher = 'Jeremy', 'Bentham', 'Utilitarist'

                    #Unpacking tuple values:
                    name, age, occupation = philosopher

            [Example](https://colab.research.google.com/drive/17nVp9YrOiehbJY64r5G4x5n-E-uK8cYX?usp=sharing)
            ''')
        

    