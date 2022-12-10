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
                ```
                    df_to_store = pd.read_csv('file.csv')

                    #Real world example with more parametres
                    df_to_store = pd.read_csv('path_to_file.csv', sep=";", on_bad_lines="skip", lineterminator="\n")
                
                ```

                * Use specific columns and define index
                ```df_to_store = pd.read_csv('file.csv', usecols=['col1', 'col2', 'col3'], index_col = 'col1')```


            """
        )

    with st.expander("Dataframe Inspection"):
        st.write(
            """
            
                1.Get first ten rows
                ```df.head(n=10)```

                2.Get last 5 rows
                ```df.tail(n=5)```

                3.Gather metadata about the df
                ```df.info()```

                4.Gather aggregated data about the Dataframe
                ```df.describe()```

                5. Discover shape of the data DataFrame
                ```df.shape (returns number of rows and colums)```


            """
        )
       
