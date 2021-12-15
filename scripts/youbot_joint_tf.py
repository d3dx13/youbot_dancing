from math import pi
from collections.abc import Iterable
import numpy as np

# y_cmd = b + y_center
b = [pi - 0.174345 + 0.000050,
     pi / 2 - 0.437712 + 0.003676 - 0.000169,
     pi + 0.596362 - 0.004473 + 0.000081,
     pi / 2 + 0.218688 - 0.001109 - 0.000437,
     pi - 0.218036 + 0.000138]
b = np.array(b)


# joint_number starts from 0
def tf(joints, joint_number=None):
    if isinstance(joints, Iterable):
        return (b.copy() + np.array(joints)).tolist()
    elif joint_number is not None:
        return b[joint_number] + float(joints)
    else:
        raise Exception("joints must be Iterable or joint_number is not None")
