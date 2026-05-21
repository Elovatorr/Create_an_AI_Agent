from functions.get_files_info import get_files_info
print("result for current directory")
print(get_files_info("calculator", "."))
print("result for pkg directory")
print(get_files_info("calculator", "pkg"))
print("result for /bin directory")
print(get_files_info("calculator", "/bin"))
print("result for ../ directory")
print(get_files_info("calculator", "../"))