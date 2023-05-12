import random

def generate_expression(operators, max_num, with_brackets=False, with_decimal=False):
    """
    生成一个四则运算表达式
    :param operators: 运算符列表
    :param max_num: 最大数
    :param with_brackets: 是否包含括号
    :param with_decimal: 是否包含小数
    :return: 表达式字符串
    """
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    operator = random.choice(operators)
    if with_decimal:
        num1 = round(random.uniform(1, max_num), 2)
        num2 = round(random.uniform(1, max_num), 2)
    if with_brackets and random.random() < 0.5:
        return f"({num1} {operator} {num2})"
    else:
        return f"{num1} {operator} {num2}"
def generate_questions(num, operators, max_num, with_brackets=False, with_decimal=False):
    """
    生成指定数量的四则运算题目
    :param num: 题目数量
    :param operators: 运算符列表
    :param max_num: 最大数
    :param with_brackets: 是否包含括号
    :param with_decimal: 是否包含小数
    :return: 题目列表
    """
    questions = []
    for i in range(num):
        expression = generate_expression(operators, max_num, with_brackets, with_decimal)
        while eval(expression) < 0:  # 避免出现负数
            expression = generate_expression(operators, max_num, with_brackets, with_decimal)
        questions.append(f"{i+1}. {expression} = ")
    return questions
def output_questions(questions, output_method):
    """
    输出题目
    :param questions: 题目列表
    :param output_method: 输出方式
    """
    if output_method == "console":
        for question in questions:
            print(question)
    elif output_method == "file":
        with open("questions.txt", "w") as f:
            for question in questions:
                f.write(question + "\n")
    elif output_method == "printer":
        # 打印机输出
        pass
    else:
        print("不支持的输出方式")
if __name__ == "__main__":
    operators = ["+", "-", "*", "/"]
    max_num = 100
    num = 10
    with_brackets = True
    with_decimal = False
    output_method = "console"
    questions = generate_questions(num, operators, max_num, with_brackets, with_decimal)
    output_questions(questions, output_method)

