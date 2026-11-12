# Cross-Language Specification - Log Analyzer

## Algorithm
Parse Apache log format and compute:
- Total requests
- Unique visitors
- Error rate

## Inputs
- Sample log files (text format with IP, timestamp, method, status)

## Outputs
- JSON object with statistics (total_requests, unique_visitors, error_rate_percentage)

## Edge Cases
- Empty file
- Malformed log entry
- File with only 200 OK responses
- Missing IP addresses in logs
- Extremely large log file chunks

## Test Cases
1. log_small.txt -> 100 requests, 20 errors, 50 unique visitors
2. log_empty.txt -> 0 requests, 0 errors, 0 unique visitors
3. log_malformed.txt -> 10 valid requests, 5 skipped malformed entries
4. log_success.txt -> 500 requests, 0 errors, 200 unique visitors
5. log_heavy_errors.txt -> 50 requests, 45 errors, 5 unique visitors
