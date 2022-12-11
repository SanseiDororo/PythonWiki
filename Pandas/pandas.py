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
                CHECKING VERSION
                
                ```pd.show_versions()```

                Import declaration:
                
                ```import pandas as pd```

                READING CSV FILE
                
                ```
                df_to_store = pd.read_csv('file.csv')

                #Real world example with more parametres
                pd.read_csv('path_to_file.csv', sep=";", on_bad_lines="skip", lineterminator="")
                
                ```

                Use specific columns and define index
                
                ```df_to_store = pd.read_csv('file.csv', usecols=['col1', 'col2', 'col3'], index_col = 'col1')```


            """
        )

    with st.expander("Data Preparation"):
        st.write(
            """

                In most cases data comes with the headers and unorganized.

                To remove header and tail and define labels, we use the following parametres
                in the pd.read_csv method:

                skiprows = number of rows
                skipfooter = number of rows
                header = None 
                names = array of column names

                Example:

                ```pd.read_csv("cars_raw.csv", skiprows= 2, skipfooter= 1, header = None, names = labels)```

                EXPORTING THE DATA 

                ```df.to_csv("file.csv")```

            """
        )
    
    with st.expander("Importing Data"):
        st.write(
            """
            Importing messy data is the most common task. We first need
            to consolidate the data set before we can start deriving valuable information.

            We can import data from various sources: csv, excel, html. The methods are

            *   pd.read_csv('')
            *  pd.read_excel('')
            * pd.read_html('')   


            SKIPPING ROWS & DELETING UNWANTED ENTRIES

            ```pd.read_csv('filename.csv', skiprows = n)```

            

            SKIPPING FOOTER 

            ```pd.read_csv('filename.csv', skipfooter = n)```


            SKIPPING HEADER

            ```pd.read_csv('filename.csv', Header = None)```


            SETTING LABELS FOR HEADER

            ```pd.read_csv('filename.csv', names = [])```


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
            
            *ascending: defines the order

            *inplace: defines if the result is stored in new df or not

            
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
    with st.expander("Arithmetic Operations"):
        st.write(
            """
            
            With Pandas we can perform arithmetic operations on pandas data series.

            ADDITION 

            ```df.column1.add(df.column2)```
            
            add method allows to define additional arguments:

            * Replacing NaN with 0

            ``` df.column1.add(df.column2, fill_value=0)

                df.column1 + df.column2```

            To store data under new column:

            ```df["new_column"] = df.column1.add(df.column2)```

            EXAMPLE

            ```cars.model_year = cars.model_year.add(1900)```

            MULTIPLICATION

            ``` 
                df.column1 * df.column2 
                df.column1.mul(df.column2, fill_value=0)
            ```

            SUBTRACTION

            ```df.column1.sub(df.column2, fill_value=0)```

        
            DIVISION

            ```df.column1.div(df.column2)```


            """
        )   
    with st.expander("Binning & Discretisation"):
        st.write(
            """
            
            DISCRETIZATION & BINNING

            Bin is subarray or group
            
            ```defining_bins [1,2,3,4,5]```
            
            ```series = pd.cut(df.column, defining_bins, right = False)```
            
            1. parameter - column
            2. parameter - bins (instead of predefined array we can pass integer as an argument. 
               This comes handy when we don't know the edges of the group. 
               Equal bins create equal width bins)
            3. parameter - right, indicate whether bins include right most edge or not
            
            Returns values for the bins
            ```series.value_counts()``` 
            
            CREATE NEW PANDAS SERIES
            
            ```df["column_name"] = series```
            
            ASSIGNING NAMES TO THE GROUP
            
            ```
            
                df.groupby("column_name").column_name1.mean()
            
                group_names = ["", "", "", "", "", ""]
            
            
                Example:
            
                pd.cut(titanic.age, age_bins, right=False, labels=group_names)
            
            ```
            Quantile based discretization function which discretisize series 
            into equal-size buckets based on rank or sample quantities.
            
            ```returns values for the bins```

            EXAMPLE
            
            ```
            Creates 5 groups of equal weight
            pd.qcut(df.column, 5) 
            
            ```
            
            We can as well pass user defined quantiles as a parameter.
            
            ``` 
                pd.qcut(
                df.column, [value1, value2, value3, value4, value5], 
                labels=["label1", "label2", "label3", "label4", "label5"])
            ```
        
       
            """
        )  
    
    with st.expander("Caps & Flors"):
        st.write(
            """
            CAPS & FLOORS

            On dfs we need to define tresholds in order to exclude outliers 
            which may distort the data perspective.In most cases we cut caps and floors.

            Example:

            series_cap = value
            series_floor = value

            Overriding values above setted cap with the new value

            ```
            df.loc[df.column > value, "column_name"] = value
            df.loc[df.column > value, "column_name"] = value
            
            ```
            
            EXAMPLE:

            ```cars.loc[cars.mpg > 40, "mpg"] = 40```


            """
        )

    with st.expander("Custom Functions"):
        st.write(
            """
            CUSTOM FUNCTIONS IN PANDAS

            We can create custom functions in order to filter or manipulate 
            data according to our specific needs.

            Methods to use custom functions are:

            apply()
            applymap()

            EXAMPLE:

            ```def range(series):
                return series.max() - series.min()```

            ```df.apply(range, axis = 0)```

            It is much simpler to use anonymous rather than custom functions

            ```df.apply(lambda x: x.max()- x.min(), axis=0)```

            APPLYING USER DEFINED FUNCTION ON SPECIFIC ROWS WITH THE ILOC OPERATOR

            ```df.iloc[:, 1:3].applymap(lambda x: x[0])```

            CUSTOM FUNCTION FOR DEFINING RANGE BETWEEN HIGHEST 
            AND LOWEST VALUE OF NUMERICAL COLUMNS

            ```df.iloc[:, :-2].apply(lambda x: x.max() - x.min(), axis = 0)```

            """
        )  

    with st.expander("Filtering"):
        st.write(
            """
            
            FILTERING DATA

            Creating masks to isolate the data:

            ```
                mask1 - returns array of the boolean values
                mask1 = df.column1 == "12"
                mask2 = df.column2 == "string"                
            ``


            Easier method for filtering the data without creating masks is:
            
            ```df.loc[(df.column1 == "value") & (df.column2 == value)]```
            

            We can use mask to perform filtering on the dataframes

            ```
            value_12 = df.loc[mask1].copy()
            ```
            
            AND OPERATOR

            ```
            value_12_string = df.loc[mask1 & mask2].copy()
            ```

            BETWEEN OPERATOR

            ```
            returns values of the column1 between 1 and 5
            value_between = df.loc[df.column1.between(1,5)].copy()
            ```

            NOT OPERATOR 

            is designated by the tilde sign ~

            ```
            returns records which doesn't have values 12 and 13 but just the second and the third column
            not_12_13_value = df.loc[~df.column1.isin(12,13), ["column2","column3]].copy()
            ```

            MANIPULATING ELEMENTS IN THE DATA FRAME

            Defining value for the whole panda series

            ```
            column1_40 = df.loc[df.column1 > 40].copy()
            column1_40 = 40
            ```
            
            Changes all the values of column1 which are greater than 40 to the value 40

            ** Chaining indexes should be avoided. **

            
            When we want to filter the data we first need to make data mask.

            ```
            mask1 = df.column == value
            mask2 = df.column < value

            This creates a boolean series.
            ```
            To filter the data we need to:

            ```filtered_data = df.loc[mask1].copy()```

            We can as well define varios conditions when filtering the data:

            ```filtered_data = df.loc[mask1 & mask2].copy()```

            OPERATORS

            AND
            
            ```filtered_data = df.loc[mask1 & mask2].copy```

            NOT
            
            ```
            not_value1_2 = df.loc
            [~df.column.between(value1, value2), 
            ["column1", "column2"]].copy()
            ```

            BETWEEN
            
            ```filtered_data = df.loc
            [df.column.between(value1,value2, inclusive=True)]
            ```
            ISIN
            
            ```filtered_data = df.loc
            [df.column.isin([value1,value2]), 
            ["column1","column2"] inclusive=True)]
            ```
            
            CHAINING METHODS

            ```df[df["column1]=="value"]["column2"].value_counts()```

            Example

            ```
                bank[bank["employee"]=="unemployed"]["education"].value_counts()
                bank[bank["employee"]=="unemployed"]["age"].mean()
            ```        

            """
        )  

    with st.expander("Grouping"):
        st.write(
            """
            Group by operation is very useful and important 
            in the data analysis process, since it returns aggregated data

            CREATE GROUP BY OBJECT:

            ```df.groupby("key1","key2")```

            To see the groups produced, we need to store the object into the 
            df and call group methods.

            ```
            df = df.groupby(["key1","key2"])
            df.groups
            ```
            

            CHAINING METHODS

            ```
            df_mean = df.groupby("key").columname.mean()
            ```

            EXAMPLE:
            
            ```
            mpg_by_year = cars.groupby("model_year").mean().round(2)

            mpg_year_origin = cars.groupby(["model_year", "origin"]).mpg.mean().unstack().round(2)
            ```
        

            ADVANCED AGGREGATIONS

            With the aggregation function which accepts various parametres, we can define 
            various aggregated values

            ```
            df = df.groupby("key1", "key2").column.agg(["min","max"]).unstack().round(2)
            ```

            EXAMPLE
            
            ```
            cars.groupby(["model_year", "origin"]).mpg.agg(["mean", "max", "min"]).unstack().round(2)
            ```
            
            APPLYING CUSTOM METHODS

            With the groupby objects we can aswell use the custom methods.

            Step one is to provide the method:

            EXAMPLE
            ```
                def get_most_efficient(group):
                    return group.nlargest(n = 2, columns = "mpg").loc[:, ["name", "mpg"]]
            ```
            
            Step 2 is to apply it
            
            EXAMPLE

            ```
            most_eff = cars.groupby(["model_year", "origin"]).apply(get_most_efficient)
            ```
            
            CREATING NEW PANDAS SERIES AND STORING ITS VALUES TO NEW COLUMN

            ```
            df["new_column_name"] = df.groupby(["key1", "key2"]).transform("mean").round(2)
            ```
            
            EXAMPLE
            
            ```
            cars["group_mpg"] = cars.groupby(["model_year", "origin"]).mpg.transform("mean").round(2)
            ```

            """
        ) 
    with st.expander("Arithmetic Operations"):
        st.write(
            """
            
            
 


            """
        )  

    with st.expander("Arithmetic Operations"):
        st.write(
            """
            
            
 


            """
        )    