# tests/test_map_generation.py

import unittest
import pandas as pd
from firearm_analysis.map_generation import create_maps


class TestMapGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample DataFrame for testing
        cls.df = pd.DataFrame({
            "code": ["KY", "AL", "CA", "OR", "FL"],
            "permit_perc": [53, 62, 10, 15, 95],
            "handgun_perc": [34, 27, 7, 13, 83],
            "longgun_perc": [23, 15, 5, 9, 58],
        })

    def test_create_maps(self):
        try:
            create_maps(self.df)
        except Exception as e:
            self.fail(f"create_maps raised Exception unexpectedly! {e}")


if __name__ == '__main__':
    unittest.main()
