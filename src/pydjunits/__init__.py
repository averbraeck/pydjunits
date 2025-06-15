# __init__.py

"""
pydjunits contains a port of the Java djunits package to Python. 
It allows to carry out calculations with strongly typed quantities, where 
addition, subtraction, multiplication and division can be done for 
scalars with an attached quantity. The package has an extensive set of
display unit for each quantity, where calculations to and from the display
unit take place automatically.

Modules
-------
units
    Quantities and units to use in simulations, with 'Duration' as the
    most important one as it can be used as for specifying simulation time.
    

Dependencies
------------
pydjunits is only dependent on standard Python libraries. 
For the unit tests, pytest is used, potentially with pytest-cov to assess 
the test coverage.
"""

# Version of the pydjunits package
__version__ = "1.0.0"