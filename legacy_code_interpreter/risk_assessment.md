# Risk Assessment - Legacy CRM

| Risk | Severity | Notes |
|------|----------|-------|
| Hardcoded credentials | High | Database login stored in config.php |
| SQL injection | High | UserAuth::login() builds queries by string concatenation |
| Weak password hashing | High | Passwords hashed with MD5 |
| Deprecated PHP 5.4 and libraries | High | No security patches, relies on removed functions |
| Missing unit tests | Medium | Critical modules like payments are untested |
| Tight coupling | Medium | Makes refactoring difficult |
| N+1 queries in reports | Medium | ReportGenerator is slow on large data |
| No logging | Low | Debugging failures is harder |
