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
                Checking pandas Version:
                
                ```pd.show_versions()```

                Import declaration:
                
                ```import pandas as pd```

                Reading the csv_file:
                
                ```
                df_to_store = pd.read_csv('file.csv')

                #Real world example with more parametres
                pd.read_csv('path_to_file.csv', sep=";", on_bad_lines="skip", lineterminator="")
                
                ```

                Use specific columns and define index
                
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
            
               DATAFRAME METHODS

                Returns basic statistics 
                
                ```df.describe()```         
                
                Returns non missing values for each column or row
                
                ```df.count()```

                Returns average value. Axis parameter selects row
                
                ```df.mean(axis = )```

                Returns the total of numerical values
                
                ```df.sum()```

                Returns the median of values
                
                ```df.median()```

                Returns the minimum of values
                
                ```df.min()```             
                
                Returns the maximum of values
                
                ```df.max()```

                Returns the index where the maximum value occurs
                
                ```df.idxmax()```           
                
                Returns the index where the minimum value occurs
                
                ```df.idxmin()```

                Returns the absolute value of values
                
                ```df.abs()```

                Returns the standard deviation
                
                ```df.std()```

                Return the variance
                
                ```df.var()```

                Return the covariance between two Series or 
                a covariance matrix for all columns combinations in DataFrame 
                
                ```df.cov()```

                Returns correlation between two Series 
                or a correlation matrix for all columns in a DataFrame
                
                ```df.corr()```             
                
                Gets specific quantile
                
                ```df.quantile()```        
                
                Returns cumulative sum
                
                ```df.cumsum()```          
                
                Returns cumulative minimum
                
                ```df.cummin()```           
                
                Returns cumulative maximum
                
                ```df.cummax()```           
                

                SERIES METHODS
                
                Gets distinct values od the column
                
                ```series.unique()```           
                
                Returns frequency of values
                
                ```series.value_counts()```      

                Gets the most common value of the series
                
                ```series.mode()```             
                
                       
                Returns corellation between 2 integer values (very useful)
                
                ```df.column.corr()```           



                INDEX METHODS

                Finds the location of maximum value in the index
                
                ```argmax()```                  
                
                Finds the location of minimum value in the index

                ```argmin()```             
                
                Check whether the index contains a value
                
                ```contains()```               
                
                Compare the index to another Index object for equality
                
                ```equals()```

                Check if the index values are in list of values and return an array of Booleans
                
                ```isin()```                    
                
                Find the min max value in the index
                
                ```max() / min()```             
                
                Get number of unique values in the index
                
                ```nunique()```                 
                
                Create frequency table for the unique values in the index

                ```value_counts()```             
                

                AGGREGATION

                df.groupby(["col1", "col2", "col3"]).col.agg[("mean","min","max")]



            """
        )
    
    with st.expander("Series"):
        st.write(
            """
            
            PANDAS SERIES

            Pandas series is one-dimensional labeled array capable of holding data of any type.

            Example data frame

            |index | column1 | column2 | column2  |
            |------|---------|---------|--------- |
            |row 1 | value   | value   | value    |
            |row 2 | value   | value   | value    |
            |row 3 | value   | value   | value    |
            |row 4 | value   | value   | value    |

            
            CREATING PANDAS SERIES

            To create a series, we can isolate the values of a column and store it in the df.

            ```column1_values = df.column1.copy()```

            WE CAN EXECUTE METHODS IN ORDER TO GATHER BASIC STATISTICS.

            ```column1_values.describe()```


            VALUE COUNT METHOD

            column1_values.value_counts()


            GET RELATIVE FREQUENCES

            ```column1_values.value_counts(normalize = True)```


            SORT VALUES

            ```column1_values.sort_values()```
            
            arguments 
            
            *ascending:defines the order, 
            *inplace:defines if the result is stored in new df or not

            
            GET MAX VALUE IN THE INTEGER BASED SERIES
            
            ```column1_values.max()```


            Creating new pandas series from existing one

            ```new_series = (column1_values / 2)```


            Get unique values

            ```new_series.unique()```

            GET THE LARGEST AND SMALLEST VALUE

            retrieves the largest value of the series in ascending order
            
            ```dataset.nlargest(ascending=True)``` 

            We can stack methods

            ```
            #returns first 3
            datase.nlargest(ascending=True).head(3) 

            #returns 5 smallest values
            datase.nsmallest(ascending=True, n = 5) 
                
            ```
 


            """
        )
       
