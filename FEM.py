__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula'
__license__ = 'MIT License'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Class holder file that creates necessary objects for FEM"""

# Imports
import numpy as np
import sympy as sym

class Node():
    # Class vars
    TOTAL_NODES = 1

    # Init
    def __init__(self, x: float, y: float = 0, z: float = 0) -> None:
        # Coordinates
        self.__x = x
        self.__y = y
        self.__z = z

        # Give node a number
        self.__num = Node.TOTAL_NODES

        # Increase total node counter
        Node.TOTAL_NODES += 1

    # Properties
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, val: float) -> None:
        self.__x = val

    # Properties
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, val: float) -> None:
        self.__y = val

    # Properties
    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, val: float) -> None:
        self.__z = val

    @property
    def num(self) -> int:
        return self.__num


class Element():
    # Class vars
    TOTAL_ELEMENTS = 0

    # Init
    def __init__(self, n1: Node, n2: Node, A: float, E: float):
        # Constants
        self.__n1 = n1
        self.__n2 = n2
        self.__le = np.sqrt((self.__n2.x - self.__n1.x)**2 + (self.__n2.y - self.__n1.y)**2 + (self.__n2.z - self.__n1.z)**2)
        self.__A = A
        self.__E = E

        # Created values
        self.__l = (self.__n2.x - self.__n1.x)/self.__le
        self.__m = (self.__n2.y - self.__n1.y)/self.__le
        self.__n = (self.__n2.z - self.__n1.z)/self.__le

        # Forces
        self.__fx = sym.symbols('f_x')
        self.__fy = sym.symbols('f_y')
        self.__fz = sym.symbols('f_z')
        self.__fsx1 = sym.symbols('f_sx_1')
        self.__fsy1 = sym.symbols('f_sy_1')
        self.__fsz1 = sym.symbols('f_sz_1')
        self.__fsx2 = sym.symbols('f_sx_2')
        self.__fsy2 = sym.symbols('f_sy_2')
        self.__fsz2 = sym.symbols('f_sz_2')

        # Increase total element count
        Element.TOTAL_ELEMENTS += 1

    # Properties
    @property
    def n1(self) -> Node:
        return self.__n1

    @property
    def n2(self) -> Node:
        return self.__n2

    @property
    def le(self) -> float:
        return self.__le

    @property
    def A(self) -> float:
        return self.__A

    @property
    def E(self) -> float:
        return self.__E

    @property
    def l(self) -> float:
        return self.__l

    @property
    def m(self) -> float:
        return self.__m

    @property
    def n(self) -> float:
        return self.__n

    @property
    def fx(self) -> sym.Symbol:
        return self.__fx

    @property
    def fy(self) -> sym.Symbol:
        return self.__fy

    @property
    def fz(self) -> sym.Symbol:
        return self.__fz

    @property
    def fsx1(self) -> sym.Symbol:
        return self.__fsx1

    @property
    def fsy1(self) -> sym.Symbol:
        return self.__fsy1

    @property
    def fsz1(self) -> sym.Symbol:
        return self.__fsz1

    @property
    def fsx2(self) -> sym.Symbol:
        return self.__fsx2

    @property
    def fsy2(self) -> sym.Symbol:
        return self.__fsy2

    @property
    def fsz2(self) -> sym.Symbol:
        return self.__fsz2