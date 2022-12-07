import streamlit as st


def tensor():
    st.header("Machine Learning With TensorFlow")
    st.write("")
    st.write(
        """
            This section covers TensorFlow framework. It presupposes basic knowledge
            of Machine Learning and Statistics. There are several amazing resources to start with.

            * [Rules of Machine Learning by Google](https://developers.google.com/machine-learning/guides/rules-of-ml)  
    
    """
    )
    st.write("")

    st.write("")
    st.write("")

    with st.expander("Basics"):
        st.write(
            """
                Machine Learning is useful approach in case of:

                * Challenges whith extensive list of rules
                * Constantly changing environments
                * Gathering insights from extensive collections of data

                Machine learning can be used on any subject which can be represented
                with numbers.

            """
        )

    with st.expander("Neural Networks"):
        st.write(
            """
                At a high level, a neural network is a type of machine learning algorithm 
                modeled after the structure and function of the human brain. It's called 
                a "neural network" because it is made up of many small processing nodes 
                that are connected together, just like neurons in the brain.
                At a more detailed level, a neural network typically consists of multiple 
                layers of interconnected nodes. Each node in a layer receives input from 
                some number of nodes in the previous layer, performs a computation on that 
                input, and passes the result on to one or more nodes in the next layer. 
                The inputs and computations performed at each node are determined by the 
                network's configuration, which is often learned from data through a process 
                called training.
                
                During training, the network is presented with many examples of the type of 
                input data it will encounter at runtime, along with the corresponding correct
                output. The network uses this training data to adjust its configuration so that 
                it can produce the correct output for a given input. This process of adjusting 
                the network's configuration is called optimization, and it typically involves 
                adjusting the network's weights and biases, which are numeric parameters that 
                control the computation performed at each node.

                Once the network has been trained, it can be used to make predictions on new, 
                unseen data. To do this, the new input data is passed through the network, 
                layer by layer, and the final output is produced by the last layer of the network.
                Because the network has been trained to produce correct outputs for a given type 
                of input, it can often make accurate predictions on new data of the same type.

                Overall, neural networks are a powerful tool for performing complex computations 
                and can be used for a wide range of applications, such as image and speech 
                recognition, natural language processing, and many others.

            """
        )
       
