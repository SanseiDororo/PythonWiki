import streamlit as st


def pandas():
    st.header("Pandas")
    st.write("")
    st.write(
        """
            Pandas is Python library designed for data analysis and manipulation. 
            It provides a variety of tools and functions that make 
            it easy to work with data in Python, including data structures for storing
            data, tools for reading and writing data from various sources, and functions 
            for performing operations on the data. Pandas is often used in conjunction with 
            other libraries like NumPy and Matplotlib for data analysis and visualization.  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Basics"):
        st.write(
            """
                * Checking pandas Version:
                  ```pd.show_versions()```

                * Import declaration:
                ```import pandas as pd```

                * Reading the csv_file:
                ```df_to_store = pd.read_csv('file.csv')```

                * Defining the output colums and index
                ```df_to_store = pd.read_csv('file.csv', usecols=['col1', 'col2', 'col3'], index_col = 'col1')```


            """
        )

    with st.expander(""):
        st.write(
            """
                

            """
        )
       
