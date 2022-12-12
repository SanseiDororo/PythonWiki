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

                Create arrays of zeros or ones:

                ```
                np.zeros([2,3])
                np.ones([3,2])
                ```

                Numpy array contains only one data type and this is the major difference 
                between ordinary python lists and np arrays.

                To check what kind of data np array stores, we use:

                ```
                array.dtype
                ```

            """
        )

   