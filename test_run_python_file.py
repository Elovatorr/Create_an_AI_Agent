# test_run_python_file.py
from functions.run_python_file import run_python_file

def main():
    # 1. should print the calculator's usage instructions
    print(run_python_file("calculator", "main.py"))

    # 2. should run the calculator with an argument ("3 + 5")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # 3. should run the calculator's tests successfully
    print(run_python_file("calculator", "tests.py"))

    # 4. should return an error because the file is outside the working directory
    print(run_python_file("calculator", "../main.py"))

    # 5. should return an error because the file does not exist
    print(run_python_file("calculator", "nonexistent.py"))

    # 6. should return an error because the file is not a Python file
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main()
