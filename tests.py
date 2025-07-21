from functions.write_file import write_file


tests = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")
]

for test in tests:
    #dir = "current" if test[1] == "." else test[1]
    #print(f"Result for '{dir}' directory:")
    print(write_file(*test))
