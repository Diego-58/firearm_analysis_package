# tests/test_state_analysis.py

import unittest
import pandas as pd
from firearm_analysis.state_analysis import state_percentage


class TestStateAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample DataFrame for testing
        cls.df = pd.DataFrame({
            "month": ["2020-01", "2020-02"],
            "state": ["Kentucky", "Kentucky"],
            "permit": [100, 150],
            "handgun": [200, 250],
            "long_gun": [300, 350],
        })

    def test_state_percentage(self):
        result_df = state_percentage("Kentucky")
        self.assertIn("permit_perc", result_df.columns)
        self.assertIn("handgun_perc", result_df.columns)
        self.assertIn("longgun_perc", result_df.columns)


if __name__ == '__main__':
    unittest.main()
