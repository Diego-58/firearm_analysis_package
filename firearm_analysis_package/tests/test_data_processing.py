# tests/test_data_processing.py

import unittest
import pandas as pd
from firearm_analysis.data_processing import (
    read_csv, clean_csv, rename_col, breakdown_date, erase_month,
    groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
)


class TestDataProcessing(unittest.TestCase):

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

    def test_read_csv(self):
        url = "./Data/nics-firearm-background-checks.csv"
        df = read_csv(url)
        self.assertIsInstance(df, pd.DataFrame)

    def test_clean_csv(self):
        df_clean = clean_csv(self.df)
        self.assertIn("permit", df_clean.columns)
        self.assertNotIn("permit_recheck", df_clean.columns)

    def test_rename_col(self):
        df_renamed = rename_col(self.df)
        self.assertIn("long_gun", df_renamed.columns)
        self.assertNotIn("longgun", df_renamed.columns)

    def test_breakdown_date(self):
        df_with_date = breakdown_date(self.df)
        self.assertIn("year", df_with_date.columns)
        self.assertIn("month", df_with_date.columns)

    def test_erase_month(self):
        df_no_month = erase_month(self.df)
        self.assertNotIn("month", df_no_month.columns)

    def test_groupby_state_and_year(self):
        df_grouped = groupby_state_and_year(self.df)
        self.assertIn("state", df_grouped.columns)
        self.assertIn("year", df_grouped.columns)
        self.assertEqual(df_grouped.shape[0], 2)


if __name__ == "__main__":
    unittest.main()
