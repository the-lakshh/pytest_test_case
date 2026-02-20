def add(a, b):
    return a - b


def multiply(a, b):
    return a + b


def divide(a, b):
    return a * b

#==================================================================
# [AI-AGENT FIX REQUIRED — NO API KEY / AI FIX FAILED]
# ────────────────────────────────────────────────────────────────
#   Bug Type   : LOGIC
#   File       : calculator.py
#   Line       : 13
#   Error      : Assertion failed: assert divide(10, 2) == 5.0 (source function: divide)
# ────────────────────────────────────────────────────────────────
#   INSTRUCTION:
#   Fix the logic error at line 13. Review the failing assertion
#   and ensure the correct output is produced. Error: Assertion
#   failed: assert divide(10, 2) == 5.0 (source function:
#   divide)
# ────────────────────────────────────────────────────────────────
#   CODE CONTEXT:
#          8 | 
#          9 | def divide(a, b):
#         10 |     return a * b
# ────────────────────────────────────────────────────────────────
#   TEST OUTPUT (tail):
#   [notice] To update, run: pip install --upgrade pip
#   WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
#   [notice] A new release of pip is available: 25.0.1 -> 26.0.1
#   [notice] To update, run: pip install --upgrade pip
#==================================================================
