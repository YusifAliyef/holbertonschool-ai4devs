# Cross-Language Specification - Apache Access Log Analyzer

## Purpose
One algorithm, specified once, to be implemented identically in several languages
(e.g. Python, JavaScript, Go). All implementations must produce identical JSON
for the same input.

## Algorithm
Read an Apache access log (Common Log Format) line by line and compute:
1. `total_requests` - number of valid entries
2. `unique_visitors` - number of distinct client IPs
3. `error_count` - entries with status 400-599
4. `error_rate` - `error_count / total_requests * 100`, rounded to 2 decimals (0.0 if no requests)
5. `total_bytes` - sum of response sizes (`-` counts as 0)
6. `status_counts` - map of status code -> count
7. `top_paths` - top 3 most requested paths (query string removed), sorted by count desc, then path asc
8. `malformed_lines` - non-empty lines that do not match the format

Steps:
1. For each line: skip if blank (not counted anywhere).
2. Match against: `IP - - [timestamp] "METHOD PATH PROTOCOL" STATUS BYTES`
3. If no match -> `malformed_lines += 1`, continue.
4. Strip everything from `?` onward in PATH.
5. Update counters, IP set and path counts.
6. After the last line, compute error_rate, sort paths, print JSON.

## Input Format
- UTF-8 text file, one entry per line.
- Valid line example:
  `192.168.1.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326`
- STATUS: 3 digits. BYTES: integer or `-`.
- CLI: `analyzer <path-to-log-file>`

## Output Format
JSON printed to stdout, keys in this exact order:

```json
{
  "total_requests": 5,
  "unique_visitors": 3,
  "error_count": 2,
  "error_rate": 40.0,
  "total_bytes": 450,
  "status_counts": {"200": 3, "404": 1, "500": 1},
  "top_paths": [{"path": "/index.html", "count": 3}],
  "malformed_lines": 0
}
```
- `status_counts` keys are strings, sorted ascending.
- Exit code 0 on success, 1 if the file cannot be opened.

## Edge Cases
- Empty file
- File with only blank lines
- Malformed line mixed with valid ones
- Size is `-`
- Query strings (`/search?q=1` and `/search?q=2` are the same path)
- Ties in path counts (resolved alphabetically)
- All requests are errors (rate 100.0)
- Rounding (1 error of 3 -> 33.33)
- Missing file -> error message, exit code 1

## Test Cases

### TC1 - log_small.txt (normal)
```
1.1.1.1 - - [10/Oct/2026:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 100
1.1.1.1 - - [10/Oct/2026:13:55:37 +0000] "GET /about.html HTTP/1.1" 200 200
2.2.2.2 - - [10/Oct/2026:13:55:38 +0000] "GET /index.html HTTP/1.1" 404 50
3.3.3.3 - - [10/Oct/2026:13:55:39 +0000] "POST /login HTTP/1.1" 500 0
2.2.2.2 - - [10/Oct/2026:13:55:40 +0000] "GET /index.html HTTP/1.1" 200 100
```
Expected: total_requests=5, unique_visitors=3, error_count=2, error_rate=40.0,
total_bytes=450, status_counts={"200":3,"404":1,"500":1},
top_paths=[/index.html:3, /about.html:1, /login:1], malformed_lines=0

### TC2 - log_empty.txt (empty file)
Input: (no content)
Expected: total_requests=0, unique_visitors=0, error_count=0, error_rate=0.0,
total_bytes=0, status_counts={}, top_paths=[], malformed_lines=0

### TC3 - log_malformed.txt (garbage line)
```
1.1.1.1 - - [10/Oct/2026:13:55:36 +0000] "GET /a HTTP/1.1" 200 10
this is not a log line
1.1.1.1 - - [10/Oct/2026:13:55:37 +0000] "GET /a HTTP/1.1" 200 10
```
Expected: total_requests=2, unique_visitors=1, error_count=0, error_rate=0.0,
total_bytes=20, status_counts={"200":2}, top_paths=[/a:2], malformed_lines=1

### TC4 - log_all_errors.txt (100% error rate)
```
4.4.4.4 - - [10/Oct/2026:14:00:00 +0000] "GET /x HTTP/1.1" 404 0
5.5.5.5 - - [10/Oct/2026:14:00:01 +0000] "GET /y HTTP/1.1" 503 0
```
Expected: total_requests=2, unique_visitors=2, error_count=2, error_rate=100.0,
total_bytes=0, status_counts={"404":1,"503":1}, top_paths=[/x:1, /y:1], malformed_lines=0

### TC5 - log_dash_bytes.txt (size is "-")
```
6.6.6.6 - - [10/Oct/2026:14:10:00 +0000] "GET /empty HTTP/1.1" 304 -
```
Expected: total_requests=1, unique_visitors=1, error_count=0, error_rate=0.0,
total_bytes=0, status_counts={"304":1}, top_paths=[/empty:1], malformed_lines=0

### TC6 - log_query.txt (query strings, blank line, rounding)
```
7.7.7.7 - - [10/Oct/2026:14:20:00 +0000] "GET /search?q=1 HTTP/1.1" 200 10

7.7.7.7 - - [10/Oct/2026:14:20:01 +0000] "GET /search?q=2 HTTP/1.1" 200 10
8.8.8.8 - - [10/Oct/2026:14:20:02 +0000] "GET /missing HTTP/1.1" 404 5
```
Expected: total_requests=3, unique_visitors=2, error_count=1, error_rate=33.33,
total_bytes=25, status_counts={"200":2,"404":1},
top_paths=[/search:2, /missing:1], malformed_lines=0

## Acceptance Criteria
An implementation passes when its output for TC1-TC6 equals the expected values exactly.
