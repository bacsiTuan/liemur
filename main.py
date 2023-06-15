
from utils.calculate_price import calculate, multithread_calculate

if __name__ == '__main__':
    file_input = 'calculate_price.xlsx'
    # calculate price using single thread
    calculate(file_input)
    # calculate price using multithread
    multithread_calculate(file_input)