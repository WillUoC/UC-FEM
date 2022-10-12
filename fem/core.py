__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula'
__license__ = 'MIT License'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Class holder file that creates necessary objects for FEM"""

# Imports
import numpy as np

class Node():
    # Class vars
    TOTAL_NODES = 0

    # Init
    def __init__(self, x: float, y: float = 0, z: float = 0) -> None:
        """Initializes a Node object.

        Args:
            x (float): the x-coordinate.
            y (float, optional): the y-coordinate. Defaults to 0.
            z (float, optional): the z-coordinate. Defaults to 0.
        """
        # Coordinates
        self.__x = x
        self.__y = y
        self.__z = z

        # Forces
        self.__fx = 0
        self.__fy = 0
        self.__fz = 0

        # Increase total node counter
        Node.TOTAL_NODES += 1

        # Give node a number
        self.__num = Node.TOTAL_NODES

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
    def fx(self) -> float:
        return self.__fx

    @fx.setter
    def fx(self, val: float) -> None:
        self.__fx = val

    @property
    def fy(self) -> float:
        return self.__fy

    @fy.setter
    def fy(self, val: float) -> None:
        self.__fy = val

    @property
    def fz(self) -> float:
        return self.__fz

    @fz.setter
    def fz(self, val: float) -> None:
        self.__fz = val

    @property
    def num(self) -> int:
        return self.__num

class Element():
    # Class vars
    TOTAL_ELEMENTS = 0

    # Init
    def __init__(self, n1: Node, n2: Node, A: float, E: float) -> None:
        """Initializes an Element object.

        Args:
            n1 (Node): node 1.
            n2 (Node): node 2.
            A (float): cross sectional area.
            E (float): Young's modulus.
        """
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