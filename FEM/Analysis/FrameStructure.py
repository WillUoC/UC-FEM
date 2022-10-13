from ..core.core import _Element, Node
import numpy as np

class FrameStructure:
    def __init__(self, elements: list[_Element], nodes: list[Node]):
        self.__elements = elements
        self.__nodes = nodes

    def analyze(self):
        # TODO:combine elements into global frame

        known_forces = np.zeros((len(self.__nodes)*3, 1))
        known_displacements = np.zeros((len(self.__nodes)*3, 1))

        for ind, i in enumerate(self.__nodes):
            known_forces[3*ind] = i.fx
            known_forces[3*ind+1] = i.fy
            known_forces[3*ind+2] = i.Mz

            known_displacements[3*ind] = i.D1
            known_displacements[3*ind+1] = i.D2
            known_displacements[3*ind+2] = i.D3

        print(known_forces)
        print(known_displacements)

        global_stiffness = np.zeros((len(self.__nodes)*3, len(self.__nodes*3)))

        for ind, element in enumerate(self.__elements):
            element.KMF()
            D = [
                element.n1.num*3-2,
                element.n1.num*3-1,
                element.n1.num*3,
                element.n2.num*3-2,
                element.n2.num*3-1,
                element.n2.num*3
            ]

            D.sort()

            element_stiffness_matrix = element.Ke


        return None