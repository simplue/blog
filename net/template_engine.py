import re
import ast

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'
BLOCK_TOKEN_START = '{%'
BLOCK_TOKEN_END = '%}'

TOK_REGEX = re.compile(r"(%s.*?%s|%s.*?%s)" % (
    VAR_TOKEN_START,
    VAR_TOKEN_END,
    BLOCK_TOKEN_START,
    BLOCK_TOKEN_END
))

# 原理
#   https://www.jianshu.com/p/b5d4aa45e771
#   https://www.jianshu.com/p/d6551dfacd58
# 源码
#   https://github.com/aosabook/500lines/blob/master/template-engine/code/templite.py
content = """Hello, {{name}}!
{% if role == "admin" %}
<a href="/dashboard">Dashboard</a>
{% end %}"""

def generate_content(exec_text, context):
    print(f'exec_text: `{exec_text}` {context}')

    r = eval(exec_text, context)
    print(r, '=========')

    # r = ast.literal_eval("'xx' if False else 'FOO'")
    # print(r, '=========')

    return r


def convert_tpl(content, context=None):
    tmp_str = []
    splited_content_list = TOK_REGEX.split(content)
    for line in splited_content_list:
        if not line.startswith(('{{', '}}', '{%', '%}')):
            tmp_str.append(line)
            continue

        _match = re.match(r'{{\s*([\w\'\"\s]+)\s*}}', line)
        if _match:
            _match_content = _match.group(1)
            tmp_str.append(generate_content(_match_content, context))
        else:
            tmp_str.append(line)

    return ''.join(tmp_str)

x = convert_tpl(content, context={'name': 'Ho'})
print(x)
# OUTPUT =>
# ['Hello, ',
#  '{{name}}',
#  '\n',
#  '{% if role == "admin" %}',
#  '\n<a href="/dashboard">Dashboard</a>\n',
#  '{% end %}',
#  '']
