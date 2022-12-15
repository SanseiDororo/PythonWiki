import streamlit as st



def numpy():
    st.header("Numpy")
    st.write("")
    st.write(
        """
            NumPy is a powerful library for working with numerical data in Python. 
            It provides a wide range of functions and methods that allow you to manipulate 
            and analyze numerical data with ease.

            NumPy is particularly useful for working with large, multi-dimensional arrays of data. It provides a high-performance multidimensional array object, as well as tools for working with these arrays. This makes NumPy a useful tool for scientific computing, machine learning, and other fields that involve large amounts of numerical data.  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("DataTypes & Attributes"):
        st.write(
            """
                Numpy main object is ndarray which stands for n-dimensional array.

                Lists can be converted into ndarray with the np.array function.

                ```
                #CHANGING PYTHON LIST INTO ARRAY
                l = list(range(1,11)) 

                Change list into numpy array container

                array = np.array(l)

                ```

            """
        )

    with st.expander("Arrays"):
        st.write(
            """
                There are numerous ways to create arrays with numpy.

                Create arrays of zeros or ones:

                ```
                #Zeros array
                np.zeros([2,3])
                
                #Ones array
                np.ones([3,2])

                #Range array
                np.arange(start,stop,step)

                #Random array
                random_array = np.random.randint(1,25, size=(2,2))
                ```

                Numpy array contains only one data type and this is the major difference 
                between ordinary python lists and np arrays.

                To check what kind of data np array stores, we use:

                ```
                array.dtype
                ``` 

            """
        )

    with st.expander("Random"):
        st.write(
            """
                Numpy provides several methods for generating random numbers.

                The key for creating random numbers is defined by the seed.

                ```
                np.random.seed()

                ```
                To create random array of any shape, we can use

                ```
                np.random.random()

                ```

                To find unique values in array, we can use

                ```
                np.unique('given array')
                ```
                

            """
        )

    with st.expander("Matrices"):
        st.write(
            """
                One dimensional array is refered as a vector, while arrays of
                higher dimensions are refered as matrices.

                We can retrieve elements in matrices by indexing.

                ```
                array[0] => returns first row
                array[0][0] => returns first element of the first row
                array[:1,:1] => returns first element of the first row
                array[:3,:1] => returns first element for the first three rows
                ```

                

            """
        )
    with st.expander("Manipulation"):
        st.write(
            """
                Numpy allows vector operations. We can perform
                arithmetic operations for given n dimensional arrays.

                ```
                a_one = [1,2,3]
                a_ones = [1,1,1]

                a_one + a_ones = [2,3,4]
                a_one - a_ones = [0,2,3]

                ``` 

                When performing arithmetic operations on n dimensional array numpy uses
                broadcasting. It is extremely important to understand associated limitations.
                
                [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)

            """
        )
    

   