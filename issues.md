\# Static Code Analysis — Tournament Scoreboard



\## Issues identified and fixes



| Tool | Original issue | Fix applied |

|---|---|---|

| Pylint | Missing module and function docstrings | Added documentation strings |

| Pylint | Function and argument names did not follow snake\_case | Renamed functions and arguments |

| Pylint | Mutable default argument `players=\[]` | Changed to `players=None` and initialized inside the function |

| Pylint | Unnecessary `elif` after `return` | Replaced with a separate `if` |

| Pylint | Repeated comparisons in the top-two check | Used membership checking on the top-two list |

| Bandit | Hardcoded referee password | Removed the unused hardcoded password |

| Bandit | Standard pseudo-random generator used for the coin toss | Replaced `random.choice` with `secrets.choice` |

| Bandit | Insecure `tempfile.mktemp()` | Replaced with `tempfile.mkstemp()` and closed the file descriptor |

| Bandit | Shell command constructed using `os.system()` | Replaced with `subprocess.run()` and an argument list |

| Flake8 | Whitespace and blank-line violations | Corrected formatting and spacing |



\## Remaining Bandit findings



After the changes, Bandit reported three low-severity findings related to the SCP subprocess operation:



\- \*\*B404:\*\* Importing the subprocess module.

\- \*\*B607:\*\* Using a partial executable path.

\- \*\*B603:\*\* Calling a subprocess without enabling a shell.



The publishing function uses an argument list and does not invoke a shell, reducing shell-injection risk. However, the executable path and external command execution should still be reviewed before deployment. These findings have not been suppressed.



\## Validation



\- Pylint: 10.00/10.

\- Flake8: No reported violations.

\- Bandit: No high- or medium-severity findings; three low-severity findings remain.

\- Program execution: Successfully displayed the scoreboard and recorded four matches.



The remote publishing function was not tested against an actual server.



