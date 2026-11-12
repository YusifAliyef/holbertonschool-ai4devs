import json
import re
import sys
from collections import Counter

LINE_RE = re.compile(
    r'^(\S+) \S+ \S+ \[[^\]]+\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+|-)$'
)


def analyze(lines):
    total = errors = total_bytes = malformed = 0
    ips = set()
    statuses = Counter()
    paths = Counter()

    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        m = LINE_RE.match(line)
        if not m:
            malformed += 1
            continue
        ip, _method, path, _proto, status, size = m.groups()
        path = path.split("?", 1)[0]
        total += 1
        ips.add(ip)
        statuses[status] += 1
        paths[path] += 1
        if 400 <= int(status) <= 599:
            errors += 1
        if size != "-":
            total_bytes += int(size)

    rate = round(errors / total * 100, 2) if total else 0.0
    top = sorted(paths.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
    return {
        "total_requests": total,
        "unique_visitors": len(ips),
        "error_count": errors,
        "error_rate": rate,
        "total_bytes": total_bytes,
        "status_counts": {k: statuses[k] for k in sorted(statuses)},
        "top_paths": [{"path": p, "count": c} for p, c in top],
        "malformed_lines": malformed,
    }


def main(argv):
    if len(argv) != 2:
        print("Usage: log_analyzer.py <path-to-log-file>", file=sys.stderr)
        return 1
    try:
        with open(argv[1], encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError as e:
        print(f"Error: cannot open file: {e}", file=sys.stderr)
        return 1
    print(json.dumps(analyze(lines), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
