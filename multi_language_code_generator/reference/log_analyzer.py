"""Reference implementation: Apache access log analyzer (baseline, Python)."""


class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        """Parse an Apache log line and return its HTTP status code.

        Raises ValueError if the line is malformed.
        """
        parts = line.split()
        if len(parts) < 9:
            raise ValueError(f"Malformed log line: {line!r}")
        try:
            return {"status": int(parts[8])}
        except ValueError:
            raise ValueError(f"Invalid status code in line: {line!r}")

    def analyze(self, lines: list) -> dict:
        """Return total number of requests and error rate (status >= 400) in %."""
        lines = [l for l in lines if l.strip()]  # blank sətirləri ignore et
        total = len(lines)
        if total == 0:
            return {"total_requests": 0, "error_rate": 0.0}
        errors = sum(1 for l in lines if self.parse_line(l)["status"] >= 400)
        return {"total_requests": total, "error_rate": (errors / total) * 100}
