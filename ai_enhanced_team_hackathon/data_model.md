# Data Model

## Entity: User
| Field | Type | Description |
|-------|------|-------------|
| id | integer | Primary key |
| username | string | Unique username |
| email | string | Unique email address |
| created_at | datetime | Account creation date |

## Entity: CodeSubmission
| Field | Type | Description |
|-------|------|-------------|
| id | integer | Primary key |
| user_id | integer | Foreign key to User |
| language | string | Programming language of the snippet |
| code | text | Submitted code snippet |
| created_at | datetime | Submission date |

## Entity: AIReview
| Field | Type | Description |
|-------|------|-------------|
| id | integer | Primary key |
| submission_id | integer | Foreign key to CodeSubmission |
| explanation | text | AI explanation of the bug |
| fixed_code | text | AI suggested fixed version |
| confidence | string | High, Medium or Low |
| created_at | datetime | Review date |

## Entity: Vote
| Field | Type | Description |
|-------|------|-------------|
| id | integer | Primary key |
| review_id | integer | Foreign key to AIReview |
| user_id | integer | Foreign key to User |
| helpful | boolean | Whether the suggestion was helpful |

## Relationships
- One User has many CodeSubmissions.
- One CodeSubmission has one AIReview.
- One AIReview has many Votes.
- One User has many Votes.
