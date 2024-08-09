import unittest
from tests.test_convert_date import ConvertDateTests
from tests.test_convert_f_to_c import ConvertTempTests
from tests.test_calculate_mean import CalculateMeanTests
from tests.test_load_data_from_csv import LoadCSVTests
from tests.test_find_min import FindMinTests
from tests.test_find_max import FindMaxTests
from tests.test_generate_summary import GenerateSummaryTests
from tests.test_generate_daily_summary import GenerateDailySummaryTests

runner = unittest.TextTestRunner()

print("Running Tests...\n")
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertDateTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertTempTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(CalculateMeanTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(LoadCSVTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMinTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMaxTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateSummaryTests))))
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateDailySummaryTests))))
