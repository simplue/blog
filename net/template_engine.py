import re
import ast

VAR_TOKEN_START = '{{'
VAR_TOKEN_END = '}}'
BLOCK_TOKEN_START = '{%'
BLOCK_TOKEN_END = '%}'
COMMENT_TOKEN_START = '{#'
COMMENT_TOKEN_END = '#}'

# re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})"
# TOK_REGEX = re.compile(r'(?s)({}.*?{}|{}.*?{}|{}.*?{})'.format(
#     VAR_TOKEN_START,
#     VAR_TOKEN_END,
#     BLOCK_TOKEN_START,
#     BLOCK_TOKEN_END,
#     COMMENT_TOKEN_START,
#     COMMENT_TOKEN_END))

TOK_REGEX = re.compile(
    fr'(?s)({VAR_TOKEN_START}.*?{VAR_TOKEN_END}|{BLOCK_TOKEN_START}.*?{BLOCK_TOKEN_END}|{COMMENT_TOKEN_START}.*?{COMMENT_TOKEN_END})')

SPACE_REGEX = re.compile(r'\s+')


def remove_all_blank(s):
    return re.sub(SPACE_REGEX, '', s)


def remove_all_blank_n_split(s, separator):
    return remove_all_blank(s).split(separator)


def join_n_remove_all_blank(l, separator):
    return remove_all_blank(separator.join((l)))


# 原理
#   https://www.jianshu.com/p/b5d4aa45e771
#   https://www.jianshu.com/p/d6551dfacd58
# 源码
#   https://github.com/aosabook/500lines/blob/master/template-engine/code/templite.py
#   http://code.activestate.com/recipes/496702/


class TempliteSyntaxError(ValueError):
    """Raised when a template has a syntax error."""
    pass


class CodeBuilder(object):
    """Build source code conveniently."""

    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def __str__(self):
        return ''.join(str(c) for c in self.code)

    def add_line(self, line):
        """Add a line of source to the code.

        Indentation and newline will be added for you, Do not provide them.

        """
        self.code.append(f'{" " * self.indent_level}{line}\n')

    def add_section(self):
        """Add a section, a sub-CodeBuilder."""
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    INDENT_STEP = 4  # PEP8 says so!

    def indent(self):
        """Increase the current indent for following lines."""
        self.indent_level += self.INDENT_STEP

    def dedent(self):
        """Decrease the current indent for following lines."""
        self.indent_level -= self.INDENT_STEP

    def get_globals(self):
        """Execute the code, and return a dict of globals it defines."""
        # A check that the caller really finished all the blocks they started.
        assert self.indent_level == 0
        # Get the Python source as a single string.
        python_source = str(self)
        # Execute the source, defining globals, and return them.
        global_namespace = {}
        exec(python_source, global_namespace)
        return global_namespace


class Templite(object):
    """A simple template renderer, for a nano-subset of Django syntax.

    Supported constructs are extended variable access::

        {{var.modifer.modifier|filter|filter}}

    loops::

        {% for var in list %}...{% endfor %}

    and ifs::

        {% if var %}...{% endif %}

    Comments are within curly-hash markers::

        {# This will be ignored #}

    Construct a Templite with the template text, then use `render` against a
    dictionary context to create a finished string::

        templite = Templite('''
            <h1>Hello {{name|upper}}!</h1>
            {% for topic in topics %}
                <p>You are interested in {{topic}}.</p>
            {% endif %}
            ''',
            {'upper': str.upper},
        )
        text = templite.render({
            'name': "Ned",
            'topics': ['Python', 'Geometry', 'Juggling'],
        })

    """

    def __init__(self, text, *contexts):
        """Construct a Templite with the given `text`.

        `contexts` are dictionaries of values to use for future renderings.
        These are good for filters and global values.

        """
        self.context = {}
        for context in contexts:
            self.context.update(context)

        self.all_vars = set()
        self.loop_vars = set()

        # We construct a function in source form, then compile it and hold onto
        # it, and execute it to render the template.
        code = CodeBuilder()

        code.add_line('def render_function(context, do_dots):')
        code.indent()
        vars_code = code.add_section()
        code.add_line('result = []')
        code.add_line('append_result = result.append')
        code.add_line('extend_result = result.extend')
        code.add_line('to_str = str')

        buffered = []

        def flush_output():
            """Force `buffered` to the code builder."""
            if len(buffered) == 1:
                code.add_line(f'append_result({buffered[0]})')
            elif len(buffered) > 1:
                code.add_line(f'extend_result([{", ".join(buffered)}])')
            del buffered[:]

        ops_stack = []

        # Split the text to form a list of tokens.
        tokens = re.split(TOK_REGEX, text)
        # print(tokens)
        for token in tokens:
            if token.startswith(COMMENT_TOKEN_START):
                # Comment: ignore it and move on.
                continue
            elif token.startswith(VAR_TOKEN_START):
                # An expression to evaluate.
                expr = self._expr_code(token[2:-2].strip())
                buffered.append(f'to_str({expr})')
            elif token.startswith(BLOCK_TOKEN_START):
                # Action tag: split into words and parse further.
                flush_output()
                words = token[2:-2].strip().split()
                if words[0] == 'if':
                    # An if statement: evaluate the expression to determine if.
                    if len(words) != 2:
                        self._syntax_error('Do not understand if', token)
                    ops_stack.append('if')
                    code.add_line('if %s:' % self._expr_code(words[1]))
                    code.indent()
                elif words[0] == 'for':
                    # A loop: iterate over expression result.
                    code.add_line(self._expr_code(token[2: -2].strip(), self.loop_vars) + ':')
                    ops_stack.append('for')
                    code.indent()
                elif words[0].startswith('end'):
                    # Endsomething.  Pop the ops stack.
                    if len(words) != 1:
                        self._syntax_error('Do not understand end', token)
                    end_what = words[0][3:]
                    if not ops_stack:
                        self._syntax_error('Too many ends', token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error('Mismatched end tag', end_what)
                    code.dedent()
                else:
                    self._syntax_error('Do not understand tag', words[0])
            else:
                # Literal content.  If it isn't empty, output it.
                if token:
                    buffered.append(repr(token))

        if ops_stack:
            self._syntax_error('Unmatched action tag', ops_stack[-1])

        flush_output()

        for var_name in self.all_vars - self.loop_vars:
            vars_code.add_line(f'c_{var_name} = context[{var_name.__repr__()}]')

        code.add_line('return "".join(result)')
        code.dedent()
        self._render_function = code.get_globals()['render_function']
        self.strr = str(code)

    def _expr_code(self, expr, var_sets=None):
        """Generate a Python expression for `expr`."""
        tokens = [i for i in re.split(
            r'([_a-zA-Z][_a-zA-Z0-9\.]*\(.*\)|\s+)', expr) if i and i.strip()]
        # tokens = [i for i in re.split(r'([_a-zA-Z\{\[][\'\"\:\,_a-zA-Z0-9]*\}*\]*\.\(.*\)|\s)', expr) if i and i.strip()]
        print(tokens)
        default_var_set = self.all_vars if var_sets is None else var_sets
        var_sets_separate_index = tokens.index('in') if tokens[0] == 'for' else 0
        if var_sets_separate_index:
            tokens[1: var_sets_separate_index] = \
                [join_n_remove_all_blank(tokens[1: var_sets_separate_index], separator='')]
            var_sets_separate_index = tokens.index('in')

        for index, token in enumerate(tokens[:]):
            r = self._variable(token, default_var_set if index < var_sets_separate_index else self.all_vars)
            tokens[index] = f'c_{token}' if r is None else str(r[1])

        return ' '.join(tokens)

    def _syntax_error(self, msg, thing):
        """Raise a syntax error using `msg`, and showing `thing`."""
        raise TempliteSyntaxError(f'{msg}: {thing.__repr__()}')

    def _variable(self, name, vars_set):
        """Track that `name` is used as a variable.

        Adds the name to `vars_set`, a set of variable names.

        Raises an syntax error if `name` is not a valid name.

        """

        func_match = re.match(r'([_a-zA-Z][\._a-zA-Z0-9]*)\((.*)\)', name)
        if func_match:
            func_name, func_vars = \
                func_match.group(1), remove_all_blank_n_split(func_match.group(2), separator=',')

            is_buildin_func = func_name in ['enumerate', 'isinstance', 'list', 'str', 'float', 'int', 'tuple']
            if not is_buildin_func:
                if '.' in func_name:
                    vars_set.add(func_name.split('.', 1)[0])
                else:
                    vars_set.add(func_name)

            if func_vars[0]:
                for _index, _func_var in enumerate(func_vars[:]):
                    r = self._variable(_func_var, vars_set)
                    func_vars[_index] = f'c_{_func_var}' if r is None else str(r[1])

            func_vars_str = ', '.join(func_vars)
            return 'eval', f'{(func_name if is_buildin_func else ("c_" + func_name))}({func_vars_str})'

        loop_vars_match = re.match(r'[_a-zA-Z][_a-zA-Z0-9]*[\s]*,', name)
        if loop_vars_match:
            loop_vars = remove_all_blank_n_split(name, ',')
            for _index, _func_var in enumerate(loop_vars[:]):
                r = self._variable(_func_var, vars_set)
                loop_vars[_index] = f'c_{_func_var}' if r is None else str(r[1])
            return 'eval', ', '.join(loop_vars)

        if not re.match(r'[_a-zA-Z][_a-zA-Z0-9]*$', name) \
            or name in ['if', 'else', 'elif', 'for',
                        'False', 'None', 'True',
                        'and', 'in', 'is', 'not', 'or',
                        '==', '!=', '>', '>=', '<', '<=']:
            return 'eval', name

        vars_set.add(name)
        return

    def render(self, context=None):
        """Render this template by applying it to `context`.

        `context` is a dictionary of values to use in this rendering.

        """
        # Make the complete context we'll use.
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context, self._do_dots)

    def _do_dots(self, value, *dots):
        """Evaluate dotted expressions at runtime."""
        for dot in dots:
            try:
                value = getattr(value, dot)
            except AttributeError:
                value = value[dot]
            if callable(value):
                value = value()
        return value
