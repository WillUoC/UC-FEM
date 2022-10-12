__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula, Will Black'
__license__ = 'GNU GPLv3'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Class holder file that creates necessary objects for FEM"""

# Imports
import numpy as np

# Typing
from typing import Any

class Node():
    # Class vars
    TOTAL_NODES = 0

    # Init
    def __init__(self, x: float, y: float = 0) -> None:
        """Initializes a Node object.

        Args:
            x (float): the x-coordinate.
            y (float, optional): the y-coordinate. Defaults to 0.
            z (float, optional): the z-coordinate. Defaults to 0.
        """
        # Coordinates
        self.__x = x
        self.__y = y

        # Forces
        self.__fx = None
        self.__fy = None

        # Moments
        self.__Mz = None

        # Displacements
        self.__D1 = None
        self.__D2 = None
        self.__D3 = None

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

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, val: float) -> None:
        self.__y = val

    @property
    def fx(self) -> Any:
        return self.__fx

    @fx.setter
    def fx(self, val: float) -> None:
        self.__fx = val

    @property
    def fy(self) -> Any:
        return self.__fy

    @fy.setter
    def fy(self, val: float) -> None:
        self.__fy = val

    @property
    def Mz(self) -> Any:
        return self.__Mz

    @Mz.setter
    def Mz(self, val: float) -> None:
        self.__Mz = val

    @property
    def D1(self) -> Any:
        return self.__D1

    @D1.setter
    def D1(self, val: float) -> None:
        self.__D1 = val

    @property
    def D2(self) -> Any:
        return self.__D2

    @D2.setter
    def D2(self, val: float) -> None:
        self.__D2 = val

    @property
    def D3(self) -> Any:
        return self.__D3

    @D3.setter
    def D3(self, val: float) -> None:
        self.__D3 = val

    @property
    def num(self) -> int:
        return self.__num

class _Element():
    # Class vars
    TOTAL_ELEMENTS = 0

    # Init
    def __init__(self, n1: Node, n2: Node, rho: float, A: float, E: float, Iz: float) -> None:
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
        self.__le = np.sqrt((self.__n2.x - self.__n1.x)**2 + (self.__n2.y - self.__n1.y)**2)
        self.__rho = rho
        self.__A = A
        self.__E = E
        self.__Iz = Iz

        # Created values
        self.__lx = (self.__n2.x - self.__n1.x)/self.__le
        self.__mx = (self.__n2.y - self.__n1.y)/self.__le

        self.__ly = -(self.__n2.x - self.__n1.x)/self.__le
        self.__my = (self.__n2.y - self.__n1.y)/self.__le

        # Increase total element count
        _Element.TOTAL_ELEMENTS += 1

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
    def rho(self) -> float:
        return self.__rho

    @rho.setter
    def rho(self, val: float) -> None:
        self.__rho = val

    @property
    def A(self) -> float:
        return self.__A

    @property
    def E(self) -> float:
        return self.__E

    @property
    def Iz(self) -> float:
        return self.__Iz

    @property
    def lx(self) -> float:
        return self.__lx

    @property
    def mx(self) -> float:
        return self.__mx

    @property
    def ly(self) -> float:
        return self.__ly

    @property
    def my(self) -> float:
        return self.__my