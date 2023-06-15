import unittest
import time
from utils.calculate_price import calculate, multithread_calculate
class TestCalculate(unittest.TestCase):

    def test_calculate_single_thread(self):
        file_input = 'calculate_price.xlsx'
        start_time_t1 = time.time()
        calculate(file_input)
        print(round((time.time() - start_time_t1) * 1000))

    def test_calculate_multithread(self):
        file_input = 'calculate_price.xlsx'
        start_time_t1 = time.time()
        multithread_calculate(file_input)
        print(round((time.time() - start_time_t1) * 1000))


if __name__ == '__main__':
    unittest.main()