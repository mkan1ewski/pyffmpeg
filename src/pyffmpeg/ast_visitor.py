from pycparser.pycparser import c_ast


class FilterVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.filter_names = []
        self.filter_options = []
        self.filter_inputs = []
        self.filter_outputs = []

    def visit_Decl(self, node):
        """Traverses AST to find filter informations."""
        # matching AVClass definition to get filter names
        if isinstance(node.type, c_ast.TypeDecl):
            if isinstance(node.type.type, c_ast.IdentifierType):
                typename = node.type.type.names[0]
                if typename == "AVClass":
                    if node.init and isinstance(node.init, c_ast.InitList):
                        self.filter_names.append(
                            (node.init.exprs[0].expr.value.strip('"'))
                        )

        # matching AVOption definition to get filter options
        if isinstance(node.type, c_ast.ArrayDecl):
            if isinstance(node.type.type, c_ast.TypeDecl):
                if isinstance(node.type.type.type, c_ast.IdentifierType):
                    typename = node.type.type.type.names[0]
                    if typename == "AVOption":
                        if isinstance(node.init, c_ast.InitList):
                            options = node.init.exprs[:-1]
                            options_dict = {}
                            for option in options:
                                if isinstance(option, c_ast.InitList):
                                    if isinstance(
                                        option.exprs[0], c_ast.Constant
                                    ) and isinstance(option.exprs[1], c_ast.Constant):
                                        name = option.exprs[0].value.strip('"')
                                        description = option.exprs[1].value.strip('"')
                                        options_dict[name] = description
                                    self.filter_options.append(options_dict)

        # matching AVFilterPad definition to get inputs and outputs info
        if (
            node.name
            and "inputs" in node.name
            and isinstance(node.init, c_ast.InitList)
        ):
            self.filter_inputs.append(len(node.init.exprs))

        if (
            node.name
            and "outputs" in node.name
            and isinstance(node.init, c_ast.InitList)
        ):
            self.filter_outputs.append(len(node.init.exprs))
