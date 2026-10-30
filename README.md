### **# Log File Analyzer**



###### **## Project Overview**



The \*\*Log File Analyzer\*\* is a Python-based project that reads a server log file and analyzes the information stored in it.



The program identifies:



\- Total number of requests

\- Successful requests

\- Error responses

\- Malformed log lines

\- Most frequent IP addresses

\- Most requested endpoints



This project demonstrates Python file handling, string processing, regular expressions, `collections.Counter`, functions, exception handling, and basic data analysis.



\---

###### 

###### **## Objective**



The main objective of this project is to build a Python program that can read and analyze server log data.



The project helps understand how server logs can be processed to identify useful information such as:



\- User/request activity

\- Frequently used IP addresses

\- Frequently requested pages

\- Server errors

\- Invalid log entries



\---



###### **## Technologies Used**



\- Python

\- Regular Expressions (`re`)

\- Collections (`Counter`)

\- Text/Log Files

\- File Handling



\---



###### **## Project Structure**



```text

log\_file\_analyzer/

│

├── log\_analyzer.py

├── server.log

└── README.md

```



\---



###### **## Input File**



The project uses a file named:



```text

server.log

```



Example log entry:



```text

192.168.1.10 - - \[30/Oct/2026:10:15:01 +0530] "GET /home HTTP/1.1" 200 1234

```



From this line, the program extracts:



\- IP Address: `192.168.1.10`

\- Endpoint: `/home`

\- Status Code: `200`



\---

###### 

###### **## Main Components**



**### 1. `parse\_log\_line()`**



This function analyzes one log line.



It uses a regular expression to extract:



\- IP address

\- Endpoint

\- HTTP status code



Example:



```python

def parse\_log\_line(line):

&#x20;   pattern = r'(\\S+) .\*? "\\S+ (\\S+) HTTP/\\S+" (\\d+)'

```



If the line is invalid, the function returns:



```python

None

```



\---



**### 2. `analyze\_log\_file()`**



This function performs the main analysis.



It:



\- Opens the log file

\- Reads each line

\- Calls `parse\_log\_line()`

\- Counts IP addresses

\- Counts endpoints

\- Counts successful requests

\- Counts error responses

\- Counts malformed lines

\- Displays the final report



\---



**## Counter**



The project uses:



```python

from collections import Counter

```



`Counter` is used to count repeated values.



For example:



```python

ip\_addresses = Counter()

endpoints = Counter()

```



When an IP address is found:



```python

ip\_addresses\[ip\_address] += 1

```



When an endpoint is found:



```python

endpoints\[endpoint] += 1

```



The `most\_common()` method is then used to display the most frequent values.



\---



###### **## HTTP Status Codes**



The program analyzes HTTP response status codes.



**### Successful Requests**



Status codes from `200` to `399` are considered successful.



```python

if 200 <= status\_code < 400:

&#x20;   successful\_requests += 1

```



**### Error Responses**



Status codes `400` and above are considered errors.



```python

if status\_code >= 400:

&#x20;   error\_count += 1

```



Examples:



```text

200 → Successful

403 → Forbidden

404 → Not Found

500 → Server Error

```



\---



###### **## Malformed Log Lines**



The project also handles invalid log entries.



Example:



```text

This is a malformed log line

```



Instead of crashing, the program counts it:



```python

if result is None:

&#x20;   malformed\_lines += 1

&#x20;   continue

```



This makes the program more reliable.



\---

###### 

###### **## Sample Output**



```text

========================================

&#x20;         LOG FILE ANALYZER

========================================



Total Requests      : 11

Successful Requests : 8

Error Responses     : 3

Malformed Lines     : 1



\---------- TOP IP ADDRESSES ----------

192.168.1.10 -> 5 requests

192.168.1.11 -> 3 requests

192.168.1.12 -> 2 requests

192.168.1.13 -> 1 requests



\-------- MOST REQUESTED ENDPOINTS --------

/home -> 4 requests

/products -> 3 requests

/login -> 2 requests

/about -> 1 requests

/contact -> 1 requests



========================================

Analysis completed successfully.

========================================

```



###### **## How to Run**



**### Step 1: Install Python**



Make sure Python is installed.



Check the Python version:



```bash

python --version

```



\---



**### Step 2: Open the Project Folder**



Open Command Prompt or PowerShell and navigate to the project folder.



Example:



```bash

cd C:\\Users\\madee\\Downloads\\log\_file\_analyzer

```



\---



**### Step 3: Run the Program**



```bash

python log\_analyzer.py

```



The program will read `server.log` and display the analysis.



\---

###### 

###### **## Features**



\- Reads server log files

\- Processes logs line by line

\- Extracts IP addresses

\- Extracts endpoints

\- Extracts HTTP status codes

\- Counts successful requests

\- Counts error responses

\- Detects malformed lines

\- Finds frequently used IP addresses

\- Finds frequently requested endpoints

\- Handles missing log files

\- Uses memory-efficient line-by-line processing



\---



###### **## Exception Handling**



The program handles a missing log file using:



```python

try:

&#x20;   ...

except FileNotFoundError:

&#x20;   print("Error: server.log file was not found.")

```



This prevents the program from terminating unexpectedly when the input file does not exist.



\---



###### **## Future Enhancements**



The project can be improved by adding:



\- Date/time-based analysis

\- Error reports

\- CSV report generation

\- Graphs and charts

\- Filtering by status code

\- Filtering by IP address

\- Top 5 or Top 10 IP addresses

\- Top 5 or Top 10 endpoints

\- GUI interface

\- Web-based dashboard

\- Exporting analysis results to JSON or CSV



\---



###### **## Learning Outcomes**



Through this project, I learned how to:



\- Work with files in Python

\- Read files line by line

\- Use regular expressions

\- Use `collections.Counter`

\- Create reusable functions

\- Handle invalid data

\- Handle exceptions

\- Analyze structured text data

\- Generate a summary report



\---



###### **## Conclusion**



The Log File Analyzer successfully demonstrates how Python can be used to process server log data and extract meaningful information.



The project combines file handling, regular expressions, collections, exception handling, and basic data analysis to create a practical industry-style application.

