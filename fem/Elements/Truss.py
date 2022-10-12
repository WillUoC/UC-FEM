__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula, Will Black'
__license__ = 'GNU GPLv3'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Defines the truss element"""

# Imports
from ..core.core import Node, _Element

# Typing Imports
from typing import Any

class Truss(_Element):
    def __init__(self, n1: Node, n2: Node, rho: float, A: float, E: float, Iz: float) -> None:
        """Initializes a Truss member.

        Args:
            n1 (Node): node 1.
            n2 (Node): node 2.
            rho (float): the density.
            A (float): the cross sectional area.
            E (float): Young's modulus.
            Iz (float): the second moment of inertia.
        """
        # Init Element
        super().__init__(n1, n2, rho, A, E, Iz)

        # Truss forces
        self.__fx = None

    # Properties
    @property
    def fx(self) -> Any:
        return self.__fx

    @fx.setter
    def fx(self, val: float) -> None:
        self.__fx = val