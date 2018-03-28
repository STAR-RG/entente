import esprima


def validate(file_path):
    '''
        Returns None if file is valid and returns an error message otherwise.
        A file is valid if 
         (1) it contains only unicode text
         (2) it is parseable (i.e., it is structurally well-formed)
         (3) it does not contain engine-specific functions
    '''
    with open(file_path) as source:
        
        try:
            contents = '\n'.join(source.readlines())
        except UnicodeDecodeError as e: # fuzzer can add really crazy characters
            return str(e)
        
        # TODO see if enabling tolerant mode (parser will continue after encountering errors) is useful
        # for now, just return the error as a string
        try:
            ast = esprima.parseScript(contents)  # , options={'tolerant': True}
        except esprima.Error as e:
            return str(e)
        except RecursionError as e:
            return str(e)

        # user-defined validators
        validators = [v for k, v in globals().items() if k.startswith("check_")]
        for v in validators:
            result = v(ast)
            if result:
                return result
                
    return None


def check_nonstandard_methods(ast):
    visitor = MethodCollectorVisitor()
    visitor.visit(ast)

    if "drainMicrotasks" in visitor.calls and "drainMicrotasks" not in visitor.declarations:
        return "drainMicroTasks is non-standard!"
    return None


class MethodCollectorVisitor(esprima.NodeVisitor):
    def __init__(self):
        self.declarations = set()
        self.calls = set()

    # noinspection PyPep8Naming
    def visit_FunctionDeclaration(self, node):
        # TODO consider modules (or whatever js uses to organize code)
        self.declarations.add(node.id.name)
        self.generic_visit(node)  # always put this at the end to continue the traversal

    # noinspection PyPep8Naming
    def visit_CallExpression(self, node):
        self.calls.add(node.callee.name)
        self.generic_visit(node)
