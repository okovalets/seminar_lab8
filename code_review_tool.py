# code_review_tool.py

import re
import sys

def check_line_length(file_path, max_length=80):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        long_lines = [i+1 for i, line in enumerate(lines) if len(line) > max_length]
        return long_lines

def check_missing_comments(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        code_lines = [line for line in lines if not line.strip().startswith("#")]
        comment_lines = [line for line in lines if line.strip().startswith("#")]
        return len(comment_lines) < len(code_lines) * 0.1

def check_variable_names(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
        variables = re.findall(r'\b([a-zA-Z]{1,2})\s*=', code)
        return variables

if __name__ == "__main__":
    path = sys.argv[1]
    print(f"Long lines: {check_line_length(path)}")
    print("Too few comments!" if check_missing_comments(path) else "Comments are OK.")
    print(f"Suspicious variable names: {check_variable_names(path)}")