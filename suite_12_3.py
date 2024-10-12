import test_12_3
import unittest

runner_suite = unittest.TestSuite()
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_suite)

