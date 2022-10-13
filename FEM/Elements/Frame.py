__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula, Will Black'
__license__ = 'GNU GPLv3'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Define the frame element"""

# Imports
import numpy as np

# Custom imports
from FEM.core.core import Node, _Element

# Typing imports
from typing import Any

class Frame(_Element):
    def __init__(self, n1: Node, n2: Node, rho: float, A: float, E: float, Iz: float) -> None:
        """Initializes a frame member.

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

        # Frame forces
        self.__fx = None
        self.__fy = None

    def KMF(self, fx: float, fy: float, m1: float, m2: float) -> None:
        """Sets the Ke, Me, and Fe matrices of the element.

        Args:
            fx (float): the force fx.
            fy (float): the force fy.
            m1 (float): the moment at Node 1 (z-axis).
            m2 (float): the moment at Node 2 (z-axis).
        """
        # Reassign
        self.__fx = fx
        self.__fy = fy
        self.n1.Mz = m1
        self.n2.Mz = m2

        # Matrices
        T = np.array([
            [self.lx, self.mx, 0, 0, 0, 0],
            [self.ly, self.my, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, self.lx, self.mx, 0],
            [0, 0, 0, self.ly, self.my, 0],
            [0, 0, 0, 0, 0, 1]
        ])

        # Rip values
        a = self.le/2
        v = (self.A * self.E)/(2 * a)
        w = (3 * self.E * self.Iz)/(2 * a**3)
        x = (3 * self.E * self.Iz)/(2 * a**2)
        y = (self.E * self.Iz)/a
        z = (2 * self.E * self.Iz)/a

        # Calculate ke
        ke = np.array([
            [v, 0, 0, -v, 0, 0],
            [0, w, x, 0, -w, x],
            [0, x, z, 0, -3, y],
            [-1, 0, 0, v, 0, 0],
            [0, -w, -x, 0, w, x],
            [0, x, y, 0, -x, z]
        ])

        # Rip values
        rho = self.rho
        A = self.A

        # Calculate me
        me = (rho * A * a)/105 * np.array([
            [70, 0, 0, 35, 0, 0],
            [0, 78, 22 * a, 0, 27, -13 * a],
            [0, 22 * a, 8 * a**2, 0, 13 * a, -6 * a**2],
            [35, 0, 0, 70, 0, 0],
            [0, 27, 13 * a, 0, 78, -22 * a],
            [0, -13 * a, -6 * a**2, 0, -22 * a, 8 * a**2]
        ])

        # Rip values
        fsx1 = self.n1.fx
        fsx2 = self.n2.fx
        fsy1 = self.n1.fy
        fsy2 = self.n2.fy
        ms1 = self.n1.Mz
        ms2 = self.n2.Mz

        # Calculate fe
        fe = np.array([
            [self.__fx * a + fsx1],
            [self.__fy * a + fsy1],
            [(self.__fy * a**2)/3 + ms1],
            [self.__fx * a + fsx2],
            [self.__fy * a + fsy2],
            [(self.__fy * a**2)/3 + ms2]
        ])

        # Set Ke, Me, and Fe
        self.__Ke = T.T @ ke @ T
        self.__Me = T.T @ me @ T
        self.__Fe = T.T @ fe

    # Properties
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
    def Ke(self) -> np.ndarray:
        return self.__Ke

    @property
    def Me(self) -> np.ndarray:
        return self.__Me

    @property
    def Fe(self) -> np.ndarray:
        return self.__Fe