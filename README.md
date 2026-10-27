# Lab 5: Static Code Analysis — Sports Tournament Scoreboard

**Source file:** `tournament_scoreboard.py`

## About the Project

This Python program manages a sports tournament scoreboard. It registers teams, records match results, calculates points and goal differences, ranks teams, checks the top two positions, and simulates a coin toss.

The lab demonstrates how static analysis tools can identify code-quality and security issues and how those issues can be addressed.

## Setup and Execution

Install the required tools:

```bash
python -m pip install pylint bandit flake8
```

Run the scoreboard:

```bash
python tournament_scoreboard.py
```

The demonstration creates four teams, records four matches, prints the league table, checks whether City Rovers is in the top two, and displays the number of matches played.

## Static Analysis

The project was analyzed using:

- **Pylint** — code quality, naming, documentation, and maintainability.
- **Bandit** — potentially insecure Python operations.
- **Flake8** — style and formatting violations.

### Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 4.75/10 | 10.00/10 |
| Bandit | 4 findings, including 1 high-severity finding | 3 low-severity findings |
| Flake8 | 4 reported violations | 0 reported violations |

### Fixes Applied

1. Added module and function docstrings.
2. Changed function and argument names to `snake_case`.
3. Replaced the mutable default argument with `None`.
4. Simplified match-result logic and the top-two check.
5. Removed the unused hardcoded referee password.
6. Replaced `random.choice()` with `secrets.choice()`.
7. Replaced `tempfile.mktemp()` with `tempfile.mkstemp()`.
8. Replaced `os.system()` with `subprocess.run()` using an argument list.
9. Corrected whitespace and formatting issues.

### Remaining Security Findings

Bandit reports three low-severity findings related to subprocess usage:

- **B404:** Subprocess module import.
- **B607:** Partial executable path used for SCP.
- **B603:** Subprocess execution requires security review.

The publishing helper avoids shell execution, but its executable path and external command execution still warrant review. Publishing to an actual remote server has not been tested.

## Reports and Documentation

### Original analysis reports

- `pylint_before.txt`
- `bandit_before.txt`
- `flake8_before.txt`

### Final analysis reports

- `pylint_after.txt`
- `bandit_after.txt`
- `flake8_after.txt`

### Additional deliverables

- `issues.md` — documented issues, their types, and fixes.
- `reflection.md` — lessons learned from static analysis.

## Conclusion

The updated scoreboard retains its demonstration functionality while improving code readability, consistency, and security practices. The results show that static analysis can help identify issues early, but tool output should be combined with functional testing and manual security review.
