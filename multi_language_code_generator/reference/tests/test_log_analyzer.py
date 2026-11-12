import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def make_line(status):
    return (
        '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] '
        f'"GET /index.html HTTP/1.1" {status} 2326'
    )


@pytest.fixture
def analyzer():
    return LogAnalyzer()


def test_parse_status_200(analyzer):
    assert analyzer.parse_line(make_line(200)) == {"status": 200}


def test_parse_status_404(analyzer):
    assert analyzer.parse_line(make_line(404)) == {"status": 404}


def test_parse_status_500(analyzer):
    assert analyzer.parse_line(make_line(500)) == {"status": 500}


def test_parse_malformed_line_raises(analyzer):
    with pytest.raises(ValueError):
        analyzer.parse_line("this is not a log line")


def test_parse_non_numeric_status_raises(analyzer):
    with pytest.raises(ValueError):
        analyzer.parse_line(make_line("abc"))


def test_analyze_empty_list(analyzer):
    assert analyzer.analyze([]) == {"total_requests": 0, "error_rate": 0.0}


def test_analyze_all_success(analyzer):
    result = analyzer.analyze([make_line(200), make_line(301)])
    assert result == {"total_requests": 2, "error_rate": 0.0}


def test_analyze_all_errors(analyzer):
    result = analyzer.analyze([make_line(404), make_line(500)])
    assert result == {"total_requests": 2, "error_rate": 100.0}


def test_analyze_mixed(analyzer):
    lines = [make_line(200), make_line(404), make_line(200), make_line(500)]
    assert analyzer.analyze(lines) == {"total_requests": 4, "error_rate": 50.0}


def test_boundary_399_ok_400_error(analyzer):
    assert analyzer.analyze([make_line(399)])["error_rate"] == 0.0
    assert analyzer.analyze([make_line(400)])["error_rate"] == 100.0


def test_blank_lines_ignored(analyzer):
    lines = [make_line(200), "", "   ", make_line(500)]
    assert analyzer.analyze(lines) == {"total_requests": 2, "error_rate": 50.0}


def test_total_requests_count(analyzer):
    lines = [make_line(200)] * 7
    assert analyzer.analyze(lines)["total_requests"] == 7
