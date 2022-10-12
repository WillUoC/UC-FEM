__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula'
__license__ = 'GNU GPLv3'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Define the beam element"""

# Imports
from ..core import Node, Element

class Beam(Element):
    def __init__(self, n1: Node, n2: Node, A: float, E: float) -> None:
        """Initializes a Beam member.

        Args:
            n1 (Node): node 1.
            n2 (Node): node 2.
            A (float): the cross sectional area.
            E (float): Young's modulus.
        """
        # Init Element
        super().__init__(n1, n2, A, E)

        # Truss forces
        self.__fx = 0
        self.__fy = 0

    # Properties
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