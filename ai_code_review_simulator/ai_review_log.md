# AI Review Log - Task Filtering Feature

Reviewed files: `tasks.py`, `test_tasks.py`
Review personas: Security, Performance, Maintainability

## Persona 1: Security Reviewer

### Inline Comments
- (line 15, `Task.__post_init__`) Title is only checked for emptiness. Add a maximum length limit to prevent oversized input.
- (line 14, `__post_init__`) The `id` field is not validated. Ensure it is a positive integer.
- (line 48, `filter_tasks`) The `status` error message echoes user input with `!r`. This is acceptable, but never include it in HTML output without escaping.

### Global Feedback
- Add input sanitization before tasks are stored or displayed in a web interface.

## Persona 2: Performance Reviewer

### Inline Comments
- (line 56, `filter_tasks`) Each task is checked against up to four conditions in a loop. This is fine for small lists, but precompute filter conditions before the loop for large data.
- (line 70, `sorted(...)`) Sorting runs on every call. Cache the sorted result if the same list is filtered many times.
- (line 78, `summarize`) Uses one loop, which is efficient (O(n)). No change needed.

### Global Feedback
- Add a benchmark test with 100,000 tasks to detect performance problems early.

## Persona 3: Maintainability Reviewer

### Inline Comments
- (line 40, `filter_tasks`) The function has many parameters (5). Consider a `TaskFilter` dataclass to group them.
- (line 56, `filter_tasks`) Split the loop body into a helper function such as `_matches(task, ...)` for readability.
- (line 5, `VALID_STATUSES`) Use an `Enum` instead of strings to avoid typos.

### Global Feedback
- Recommend splitting `filter_tasks()` into smaller functions.
- Add error handling and a clear message for empty query results.
- Add type hints and docstrings to `summarize()` return value (use `Dict[str, int]`).
- Add tests for edge cases: empty task list and tasks with the same due date.
