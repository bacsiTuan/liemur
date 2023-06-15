import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from .operator_data import (
    operator_a,
	operator_b,
)

file_input = 'calculate_price.xlsx'

def calculate(file_input: str) -> None:
	df = pd.read_excel(file_input, sheet_name="Sheet1", converters={'number':str})
	for index, row in df.iterrows():
		df.at[index,'operator a'] = calculate_price(row['number'], operator_a)
		df.at[index,'operator b'] = calculate_price(row['number'], operator_b)
	df.to_excel("output.xlsx", index=False)
        

def multithread_calculate(file_input: str) -> None:
    df = pd.read_excel(file_input, sheet_name="Sheet1", converters={'number':str})
    with ThreadPoolExecutor(max_workers=5) as ex:
        future = {ex.submit(wirte_concurrent_to_excel, (df, index, row)): (index,row) for (index,row) in
                    df.iterrows()}
        as_completed(future)
            
    df.to_excel("output_multithread.xlsx", index=False)

def wirte_concurrent_to_excel(*args) -> None:
    file = args[0][0]
    index = args[0][1]
    row = args[0][2]
    file.at[index,'operator a'] = calculate_price(row['number'], operator_a)
    file.at[index,'operator b'] = calculate_price(row['number'], operator_b)
    
	


def calculate_price(number: str, operator: dict) -> float:
    longest_prefix = ""
    for i in range(len(number)):
        prefix = number[:i + 1]
        if prefix in operator:
            longest_prefix = prefix
    return operator.get(longest_prefix, 0)
