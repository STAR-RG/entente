import esprima
import json
from esprima import nodes # https://github.com/Kronuz/esprima-python

def parse_and_rewrite(code_string):
    visitor = RewriteVisitor()
    ast = esprima.parseScript(code_string, delegate=visitor)
    visitor.visit(ast) # side-effects on the ast
    return ast

class RewriteVisitor(esprima.NodeVisitor):
    def transform_Literal(self, node, metadata):
        if type(node.value) is unicode:
            return nodes.Literal('Alo!', "Alo")
        elif type(node.value) is str:
            return nodes.Literal('Alo!', "Alo")
        elif type(node.value) is int:
            return nodes.Literal(99, "99")  
        else:
            return node

if __name__ == "__main__":
    ast = parse_and_rewrite('const answer = "Hello"')
    ## to read the tree (with types)
    print(json.dumps(ast.toDict(), indent=2))
    ## to read the code
    ## ????
