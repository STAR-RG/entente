import esprima
import json
from esprima import nodes # https://github.com/Kronuz/esprima-python

class SillyVisitor(esprima.NodeVisitor):
    def transform_Literal(self, node, metadata):
        if type(node.value) is unicode:
            return nodes.Literal('Alo!', "Alo")
        elif type(node.value) is str:
            return nodes.Literal('Alo!', "Alo")
        elif type(node.value) is int:
            return nodes.Literal(99, "99")  
        else:
            return node

def parse_and_rename():
    program = 'const answer = "Hello"'
    visitor = SillyVisitor()
    ast = esprima.parseScript(program, delegate=visitor)
    visitor.visit(ast)
    print(json.dumps(ast.toDict(), indent=2))

if __name__ == "__main__":
    parse_and_rename()