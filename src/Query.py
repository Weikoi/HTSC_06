class Query(object):
    def __init__(self, table_name, input_str):
        self.table_name = table_name
        self.input_str = input_str
        self.ast = []

    def to_ast(self):
        left_index = []
        i = 0
        while i < len(self.input_str):
            if self.input_str[i] == "(":
                left_index.append(i)
                i = i + 1
            elif self.input_str[i] == ")":
                self.ast.append(self.input_str[left_index[-1]:i + 1])
                self.input_str = self.input_str.replace(self.input_str[left_index[-1]:i + 1], "")
                i = left_index[-1]
                left_index.pop(-1)
            else:
                i = i + 1

    @staticmethod
    def transfer(relation):
        if relation == "==":
            return "="
        elif relation == "!=":
            return "<>"
        elif relation == "<":
            return "<"
        elif relation == ">":
            return ">"
        elif relation == ">=":
            return ">="
        elif relation == "<=":
            return "<="
        elif relation == "contains":
            return "like"

    def to_sql(self):

        init_str = ""
        logic_list = ["(and)", "(or)"]
        relation_list = ["==", "!=", "<", ">", "<=", ">=", "contains"]
        not_logic = "(not)"

        temp_list = []
        for i in self.ast:
            if i in logic_list:
                if len(temp_list) == 2:
                    init_str = init_str + "(" + temp_list[0] + i[1:-1] + temp_list[-1] + ")"
                    temp_list = []
                elif len(temp_list) == 1:
                    init_str = "(" + init_str + i[1:-1] + temp_list[-1] + ")"
            elif i == not_logic:
                init_str = "(" + i[1:-1] + init_str + ")"
            else:
                temp_list.append(i)
        return_str = "SELECT * FROM " + str(self.table_name) + " WHERE " + init_str
        print(return_str)
        return return_str
