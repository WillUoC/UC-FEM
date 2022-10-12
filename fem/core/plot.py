__author__ = 'Justin Panchula'
__copyright__ = 'Copyright 2022'
__credits__ = 'Justin Panchula'
__license__ = 'GNU GPLv3'
__version__ = '1.0.0'
__status__ = 'Production'
__doc__ = """Class holder file that creates necessary objects for FEM"""

# Imports
import pandas as pd
import plotly.express as px

# Custom imports

class Plot():
    def __init__(self) -> None:
        return

    def plot(self, elements: list) -> None:
        # Setup DataFrame
        columns = ['x1', 'y1', 'x2', 'y2', 'rho', 'A', 'E', 'Iz']
        index = []
        df = pd.DataFrame(index=index, columns=columns)
        df.index.name = 'Element'

        # Get all element data
        for ind, i in enumerate(elements):
            df.loc[ind, 'x1'] = i.n1.x
            df.loc[ind, 'y1'] = i.n1.y
            df.loc[ind, 'x2'] = i.n2.x
            df.loc[ind, 'y2'] = i.n2.y
            df.loc[ind, 'rho'] = i.rho
            df.loc[ind, 'A'] = i.A
            df.loc[ind, 'E'] = i.E
            df.loc[ind, 'Iz'] = i.Iz

        print(df)