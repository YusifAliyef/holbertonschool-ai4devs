# AI Explanations of Complex Code - Legacy CRM

## Section 1 – PaymentProcessor::validate()

- **Plain English**: Validates the credit card number and expiry date before a payment is sent.
- **Pattern**: Uses deeply nested if-else blocks instead of guard clauses.
- **Issues**: No logging, weak validation, errors are returned as inconsistent strings.
- **Improvements**: Replace with regex/Luhn validation, use early returns, add unit tests.

## Section 2 – UserAuth::login()

- **Plain English**: Checks the username and password against the database and starts a session for the user.
- **Pattern**: Procedural code with a raw SQL query built by string concatenation.
- **Issues**: Vulnerable to SQL injection, passwords hashed with MD5, no brute-force protection.
- **Improvements**: Use prepared statements, switch to bcrypt/password_hash(), add rate limiting.

## Section 3 – ReportGenerator::buildMonthlyReport()

- **Plain English**: Collects all orders of a month, calculates totals per customer and outputs an HTML table.
- **Pattern**: One very long function mixing database access, business logic and HTML output.
- **Issues**: Over 300 lines, hard to test, runs a query inside a loop (N+1 problem), slow on large data.
- **Improvements**: Split into data, calculation and view layers, use a single JOIN query, add pagination.

## Section 4 – Config::load()

- **Plain English**: Reads settings such as database host and credentials into global variables.
- **Pattern**: Global variables and hard-coded values inside the source code.
- **Issues**: Credentials stored in code, hard to change per environment, any module can overwrite settings.
- **Improvements**: Move values to environment variables or a .env file, use a config class, remove globals.

## Section 5 – CustomerImport::processCsv()

- **Plain English**: Reads a CSV file line by line and inserts or updates customer records in the database.
- **Pattern**: Procedural loop with copy-pasted code for insert and update.
- **Issues**: No input validation, no transaction (partial imports on failure), silent failure on bad rows.
- **Improvements**: Validate each row, wrap in a transaction, log rejected rows, extract insert/update into one method.
