import esprima


def validate(file_path):
    with open(file_path) as source:
        contents = '\n'.join(source.readlines())
        # TODO see if enabling tolerant mode (parser will continue after encountering errors) is useful
        # for now, just return the error as a string
        try:
            ast = esprima.parseScript(contents)  # , options={'tolerant': True}
        except esprima.Error as e:
            return str(e)

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
