class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        try:
            parts = line.split()
            if len(parts) > 8:
                return {"status": int(parts[8])}
            return {"status": 200}
        except (IndexError, ValueError):
            return {"status": 200}

    def analyze(self, lines: list) -> dict:
        if not lines:
            return {"total_requests": 0, "error_rate": 0.0}
        total = len(lines)
        errors = sum(1 for l in lines if self.parse_line(l)["status"] >= 400)
        return {"total_requests": total, "error_rate": (errors / total) * 100}
