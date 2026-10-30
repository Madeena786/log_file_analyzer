from collections import Counter
import re
LOG_FILE = "server.log"
def parse_log_line(line):
    pattern = r'(\S+) .*? "\S+ (\S+) HTTP/\S+" (\d+)'
    match = re.search(pattern, line)
    if not match:
        return None
    ip_address = match.group(1)
    endpoint = match.group(2)
    status_code = int(match.group(3))
    return ip_address, endpoint, status_code
def analyze_log_file(filename):
    ip_addresses = Counter()
    endpoints = Counter()
    total_requests = 0
    error_count = 0
    successful_requests = 0
    malformed_lines = 0
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                result = parse_log_line(line)
                if result is None:
                    malformed_lines += 1
                    continue
                ip_address, endpoint, status_code = result
                total_requests += 1
                ip_addresses[ip_address] += 1
                endpoints[endpoint] += 1
                if 200 <= status_code < 400:
                    successful_requests += 1
                if status_code >= 400:
                    error_count += 1
    except FileNotFoundError:
        print("Error: server.log file was not found.")
        return
    print()
    print("========================================")
    print("          LOG FILE ANALYZER")
    print("========================================")
    print()
    print("Total Requests      :", total_requests)
    print("Successful Requests :", successful_requests)
    print("Error Responses     :", error_count)
    print("Malformed Lines     :", malformed_lines)
    print()
    print("---------- TOP IP ADDRESSES ----------")
    for ip, count in ip_addresses.most_common():
        print(ip, "->", count, "requests")
    print()
    print("-------- MOST REQUESTED ENDPOINTS --------")
    for endpoint, count in endpoints.most_common():
        print(endpoint, "->", count, "requests")
    print()
    print("========================================")
    print("Analysis completed successfully.")
    print("========================================")
analyze_log_file(LOG_FILE)






