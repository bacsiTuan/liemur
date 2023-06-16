### This is the solution for alaTest / ValueChecker (ICSS) challenge 2023

<p>The solution belonged to Dao Cong Tuan (tuandao864@gmail.com) </p>
<p>I used excel file to stored input and output data, input file named "calculate_price.xlsx" and the output file will be generated after run the program. This is the basic core function of the idea and can be implement with more design to make the program run with configable file not with hard code </p>

<p>There are 2 function in the repo</p>
<ul>
	<li>calculate price with single thread</li>
 	<li>calculate price with multithread(give performance x2.5 with 1500 records, and will be more diffrence with larger data set) </li>
</ul>

<p>How to run:</p>

``` bash
pip install -r requirements.txt
```

``` bash
python main.py
```

<p><b>If it is not possible to dial a numbers with operator, the value will be Zero</b></p>

### input file: calculate_price.xlsx
### output file: output.xlsx and output_multithread.xlsx
