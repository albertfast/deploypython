from pathlib import Path
dir_path = Path('D:\Desktop\lambdaPythonProject')
file_path = dir_path / "mydocument.txt"
with open(file_path, "w") as f:
    f.write("Text in specific directory")

with open("mydocument.txt", "a") as f:
    f.write("\nThis text is appended")
    
with open(file_path, "w") as f:
    f.write(" 'w' mode Text in specific directory")

'''
lines = ["Line 1", "Line 2", "Line 3"]
with open("mydocument.txt", 'w') as f:
    f.writelines(line + '\n' for line in lines)
'''



