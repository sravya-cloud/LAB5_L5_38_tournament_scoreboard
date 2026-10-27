\# Reflection — Static Code Analysis



Working on the Tournament Scoreboard helped me understand how static analysis tools identify code-quality and security problems.



Pylint highlighted issues such as missing docstrings, inconsistent naming conventions, and the use of a mutable default argument. Fixing these issues improved the readability and maintainability of the program. The Pylint score increased from 4.75/10 to 10.00/10.



Bandit identified a hardcoded password, an insecure temporary-file function, a pseudo-random generator, and a shell command that could introduce command-injection risks. I removed the unused password, used `secrets.choice`, replaced the temporary-file function, and changed the publishing code to use `subprocess.run()` with separate arguments.



Bandit still reports three low-severity findings associated with subprocess usage. This demonstrates that changing code to reduce security risk does not necessarily eliminate every static-analysis warning. The remaining findings should be reviewed rather than ignored.



Flake8 reported four formatting violations in the original code. Correcting them resulted in no reported Flake8 violations.



Overall, this exercise showed me that static analysis is useful for finding defects early, improving code consistency, and identifying potentially unsafe operations. It also taught me that passing a static-analysis tool does not replace functional testing or a security review.



