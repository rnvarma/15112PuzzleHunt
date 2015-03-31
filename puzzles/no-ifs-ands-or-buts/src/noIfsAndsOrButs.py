import sys
import ast

class WhatsWrong(Exception):
    pass

filename = sys.argv[1]
theirProgram = open(filename, "r").read()
root = ast.parse(theirProgram)
for node in ast.walk(root):
    if isinstance(node, ast.If):
        raise WhatsWrong("If only I knew...")
    elif isinstance(node, ast.And):
        raise WhatsWrong("And it's so frustrating!")
exec(theirProgram)
