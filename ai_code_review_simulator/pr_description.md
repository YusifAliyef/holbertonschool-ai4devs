# Pull Request: Add Task Filtering Feature

## Summary
Implements task filtering by status and due date. Adds `filter_tasks()` to find tasks by status, due date range and overdue state, plus a `summarize()` helper that counts tasks per status.

## Changes
- Added `Task` dataclass with validation in `tasks.py`
- Added `filter_tasks()` in `tasks.py` (status, due_before, due_after, overdue_only)
- Added `is_overdue()` method to the Task model
- Added `summarize()` helper for status counts
- Added 12 new unit tests in `test_tasks.py`

## Context
~110 LOC. Related issue: #42. Users could not find urgent or overdue tasks in a long list, so filtering by status and due date was added to make the task list easier to manage.

## Testing
All existing and new tests pass (`python3 -m pytest ai_code_review_simulator -v`).
