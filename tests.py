from functions.run_python import run_python_file


tests = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py")
]

for test in tests:
    #dir = "current" if test[1] == "." else test[1]
    #print(f"Result for '{dir}' directory:")
    print(run_python_file(*test))
