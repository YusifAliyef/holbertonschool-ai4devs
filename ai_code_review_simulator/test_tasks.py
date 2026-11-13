from datetime import date

import pytest

from tasks import Task, filter_tasks, summarize

TODAY = date(2026, 11, 13)


@pytest.fixture
def tasks():
    return [
        Task(1, "Write report", "todo", date(2026, 11, 20)),
        Task(2, "Fix bug", "in_progress", date(2026, 11, 10)),
        Task(3, "Deploy", "done", date(2026, 11, 5)),
        Task(4, "Plan sprint", "todo", None),
        Task(5, "Review code", "todo", date(2026, 11, 12)),
    ]


def test_task_empty_title_raises():
    with pytest.raises(ValueError):
        Task(1, "   ")


def test_task_invalid_status_raises():
    with pytest.raises(ValueError):
        Task(1, "A", "wrong")


def test_is_overdue_true():
    assert Task(1, "A", "todo", date(2026, 11, 1)).is_overdue(TODAY)


def test_is_overdue_false_when_done():
    assert not Task(1, "A", "done", date(2026, 11, 1)).is_overdue(TODAY)


def test_filter_by_status(tasks):
    result = filter_tasks(tasks, status="todo")
    assert [t.id for t in result] == [5, 1, 4]


def test_filter_invalid_status_raises(tasks):
    with pytest.raises(ValueError):
        filter_tasks(tasks, status="nope")


def test_filter_due_before(tasks):
    result = filter_tasks(tasks, due_before=date(2026, 11, 10))
    assert [t.id for t in result] == [3, 2]


def test_filter_due_after(tasks):
    result = filter_tasks(tasks, due_after=date(2026, 11, 12))
    assert [t.id for t in result] == [5, 1]


def test_filter_invalid_range_raises(tasks):
    with pytest.raises(ValueError):
        filter_tasks(
            tasks, due_after=date(2026, 12, 1), due_before=date(2026, 11, 1)
        )


def test_filter_overdue_only(tasks):
    result = filter_tasks(tasks, overdue_only=True, today=TODAY)
    assert [t.id for t in result] == [2, 5]


def test_no_due_date_sorted_last(tasks):
    assert filter_tasks(tasks)[-1].id == 4


def test_summarize(tasks):
    assert summarize(tasks) == {"todo": 3, "in_progress": 1, "done": 1}
