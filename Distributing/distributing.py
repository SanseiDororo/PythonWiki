import streamlit as st


def distributing():
    st.header('Distributing')
    st.write("")
    st.write('''
            This section covers different ways to package and distribute python code.
            By convenction python files are considered as modules, while folders containing
            __init__.py file are considered as packages. There are several ways to organise
            and automatically package your code and add additional metadata information.

    
    ''')
    st.write("")
    
    st.write("")
    st.write("")
    
    with st.expander('Setuptools'):
        st.write('''
            Setuptools library provides toolset to build, package and distribute python code.
            It is a thin wraper build around distutils. In order to build a python code as a 
            consistent package setup.py (now being discouredged in favour of pyproject.toml)
            needs to be provided. 
            
                Non extensive example of the setup.py file

                # !/usr/bin/env python
                # type: ignore

                from setuptools import setup, find_packages
                from itertools import chain


                requirements = [
                    'python_package 1.7.*',
                    'can be github repo,
                ]


                extras = dict(
                    dev=[
                        'additional package for specific purpose',
                    ],
                    
                    debug=[
                        'debug_package',
                    ],
                    
                    test=[
                        'testing_package'
                    ],
                )


                # generate an extras entry that installs all requirements
                extras['all'] = list(chain.from_iterable(extras.values()))

                #Additional metadata
                setup(
                    name='name of the package',
                    version='0.1.0',
                    description='',
                    keywords='',
                    classifiers=[
                        'Programming Language :: Python',
                    ],
                    author='',
                    author_email='',
                    license='',
                    url='',
                    packages=find_packages(),
                    include_package_data=True,
                    python_requires='>=3.10',
                    # data_files=[],
                    zip_safe=False,
                    install_requires=requirements,
                    extras_require=extras,
                )

            Package is installed with:

                    pip install -e .

            Dot stands for the current directory, while -e flag means editable.

            Additional resources:

            [Practical guide](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/)

            [Writting setup script](https://docs.python.org/3/distutils/setupscript.html)

            [Extensive template](https://github.com/pypa/sampleproject) 
        
        ''')

    