from functions.get_files_info import get_files_info


tests = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
]

for test in tests:
    dir = "current" if test[1] == "." else test[1]
    print(f"Result for '{dir}' directory:")
    print(get_files_info(*test))
