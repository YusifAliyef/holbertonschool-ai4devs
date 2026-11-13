"""Task model and filtering feature."""
from dataclasses import dataclass
from datetime import date
from typing import List, Optional

VALID_STATUSES = ("todo", "in_progress", "done")


@dataclass
class Task:
    id: int
    title: str
    status: str = "todo"
    due_date: Optional[date] = None

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("title must not be empty")
        if self.status not in VALID_STATUSES:
            raise ValueError(f"invalid status: {self.status!r}")

    def is_overdue(self, today: Optional[date] = None) -> bool:
        """A task is overdue if it has a past due date and is not done."""
        today = today or date.today()
        return (
            self.due_date is not None
            and self.due_date < today
            and self.status != "done"
        )


def filter_tasks(
    tasks: List[Task],
    status: Optional[str] = None,
    due_before: Optional[date] = None,
    due_after: Optional[date] = None,
    overdue_only: bool = False,
    today: Optional[date] = None,
) -> List[Task]:
    """Filter tasks by status and due date, sorted by due date.

    Tasks without a due date are placed at the end.
    """
    if status is not None and status not in VALID_STATUSES:
        raise ValueError(f"invalid status: {status!r}")
    if due_before and due_after and due_after > due_before:
        raise ValueError("due_after must not be later than due_before")

    result = []
    for task in tasks:
        if status is not None and task.status != status:
            continue
        if due_before is not None and (
            task.due_date is None or task.due_date > due_before
        ):
            continue
        if due_after is not None and (
            task.due_date is None or task.due_date < due_after
        ):
            continue
        if overdue_only and not task.is_overdue(today):
            continue
        result.append(task)

    return sorted(
        result,
        key=lambda t: (t.due_date is None, t.due_date or date.max, t.id),
    )


def summarize(tasks: List[Task]) -> dict:
    """Return the number of tasks per status."""
    counts = {s: 0 for s in VALID_STATUSES}
    for task in tasks:
        counts[task.status] += 1
    return counts
