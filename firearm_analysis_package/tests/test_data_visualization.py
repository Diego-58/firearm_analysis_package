# tests/test_visualization.py

import unittest
import pandas as pd
# from firearm_analysis.visualization import time_evolution


class TestVisualization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample DataFrame for testing
        cls.df = pd.DataFrame({
            "year": ["2020", "2021", "2022", "2023", "2024"],
            "permit": [100, 113, 115, 114, 118],
            "handgun": [200, 193, 190, 195, 192],
            "long_gun": [300, 320, 330, 310, 315],
        })

    def test_time_evolution(self):
        try:
            time_evolution(self.df)
        except Exception as e:
            self.fail(f"`time_evolution()` raised Exception unexpectedly! {e}")


# if __name__ == '__main__':
#     unittest.main()
