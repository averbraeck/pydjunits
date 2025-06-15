"""
pydjunits demo to show how units can be used in code.
"""

from pydjunits.units import *

"""main runs the demo"""
if __name__ == "__main__":
    length = Length(60.0, "mi")
    print("the length is", length)
    print("the si of length is", length.asSI())
    duration = Duration(1.0, "h")
    print("the duration is", duration)
    speed = length / duration
    print("length / duration=", type(speed))
    print("speed is", speed, " or ", speed.as_unit("mi/h"), " or ", speed.as_unit("km/h"))
    speed *= 2
    print("double speed is", speed, " or ", speed.as_unit("mi/h"), " or ", speed.as_unit("km/h"))
    strange = SI(42, "mK/s2cd")
    print("Strange unit", strange)
