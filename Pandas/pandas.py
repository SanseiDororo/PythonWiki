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
    
    with st.expander("Statistics"):
        st.write(
            """
            
                # DATAFRAME METHODS

                returns basic statistics 
                
                ```df.describe()```         
                
                returns non missing values for each column or row
                
                ```df.count()```

                returns average value. Axis parameter selects row
                
                ```df.mean(axis = )```

                returns the total of numerical values
                
                ```df.sum()```

                returns the median of values
                
                ```df.median()```

                returns the minimum of values
                
                ```df.min()```             
                
                returns the maximum of values
                
                ```df.max()```

                returns the index where the maximum value occurs
                
                ```df.idxmax()```           
                
                returns the index where the minimum value occurs
                
                ```df.idxmin()```

                returns the absolute value of values
                
                ```df.abs()```

                returns the standard deviation
                
                ```df.std()```

                return the variance
                
                ```df.var()```

                return the covariance between two Series or 
                a covariance matrix for all columns combinations in DataFrame 
                
                ```df.cov()```

                returns correlation between two Series 
                or a correlation matrix for all columns in a DataFrame
                
                ```df.corr()```             
                
                gets specific quantile
                
                ```df.quantile()```        
                
                returns cumulative sum
                
                ```df.cumsum()```          
                
                returns cumulative minimum
                
                ```df.cummin()```           
                
                returns cumulative maximum
                
                ```df.cummax()```           
                

                #SERIES METHODS
                
                gets distinct values od the column
                
                ```series.unique()```           
                
                returns frequency of values
                
                ```series.value_counts()```      

                gets the most common value of the series
                
                ```series.mode()```             
                
                its acummulative sum
                
                ```df.column.cumsum()```        
                
                returns corellation between 2 integer values (very useful)
                
                ```df.column.corr()```           



                #INDEX METHODS

                argmax()                  - finds the location of maximum value in the index
                argmin()                  - finds the location of minimum value in the index
                contains()                - check whether the index contains a value
                equals()                  - compare the index to another Index object for equality
                isin()                    - check if the index values are in list of values and return an array of Booleans
                max() / min()             - find the min max value in the index
                nunique()                 - get number of unique values in the index
                value_counts()            - create frequency table for the unique values in the index

                

                #AGGREGATION

                df.groupby(["col1", "col2", "col3"]).col.agg[("mean","min","max")]



            """
        )
       
