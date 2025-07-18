from functions.get_file_content import get_file_content


tests = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
    ("calculator", "lorem.txt")
]

for test in tests:
    #dir = "current" if test[1] == "." else test[1]
    #print(f"Result for '{dir}' directory:")
    print(get_file_content(*test))
