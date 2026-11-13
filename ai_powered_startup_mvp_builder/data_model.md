# Data Model - Student Task Planner App

## Entity: Task
| Field | Type | Notes |
|-------|------|-------|
| id | string | Unique identifier |
| title | string | Required |
| subject_id | string | Reference to Subject |
| deadline | date | Due date |
| priority | string | low, medium or high |
| completed | boolean | Default false |
| created_at | datetime | Creation time |

## Entity: Subject
| Field | Type | Notes |
|-------|------|-------|
| id | string | Unique identifier |
| name | string | Course name, for example Math |
| color | string | Optional label color |

## Entity: Reminder
| Field | Type | Notes |
|-------|------|-------|
| id | string | Unique identifier |
| task_id | string | Reference to Task |
| remind_at | datetime | When to show the reminder |
| dismissed | boolean | Default false |

## Relationships
- One Subject has many Tasks.
- One Task has zero or many Reminders.
