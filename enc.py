import sys, os, marshal, ast, random, builtins, string
from ast import *
def rb():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))

def rb2():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=10))

def encunicode():
    return [chr(x) for x in random.sample(range(0x2160, 0x217F), 16)]

meo = encunicode()

checkvs = r'''
with open(__file__, "r", encoding="utf-8") as f:
    data = f.read()

expected = f"""if str(__import__('sys').version[0:4]) != '{str(eval("__import__('sys').version[0:4]"))}':
    print('You need to Install Python {str(eval("__import__('sys').version[0:4]"))}')
    __import__("sys").exit()"""

if expected not in data:
    raise __builtins__['Version']
'''

antihookvip = checkvs+"""
class __ngan_hook_builtins__:
    def __init__(self):
        try:
            self.p = builtins.print
            self.e = builtins.exec
            self.v = builtins.eval
        except:
            self.p = self.e = self.v = None

    def check(self):
        try:
            if self.p and builtins.print != self.p:
                raise fn
            if self.e and builtins.exec != self.e:
                raise fn
            if self.v and builtins.eval != self.v:
                raise fn
        except SystemExit:raise fn
        except:pass
__rt = __ngan_hook_builtins__()
"""

checkcuoi = """
with open(__file__, "r", encoding="utf-8") as f:
    data = ''.join(f.read().split())

if (
    f"exceptExceptionase:print(e)" not in data
):
    raise e

if (
    f"exceptKeyboardInterrupt:pass" not in data
):
        raise Crackconcak
"""

anti = antihookvip+checkcuoi+"""
if str(__import__('sys').exit) != '<built-in function exit>':
    raise fn
if str(print) != '<built-in function print>':
    raise fn
if str(exec) != '<built-in function exec>':
    raise fn
if str(input) != '<built-in function input>':
    raise fn
if str(len) != '<built-in function len>':
    raise fn
if str(__import__('marshal').loads) != '<built-in function loads>':
    raise fn
a = __import__('sys')
b = __import__('builtins')
t = __import__('types')
i = __import__('inspect')
if a.modules.get('builtins') is not b: raise fn
if not isinstance(b.exec, t.BuiltinFunctionType): raise fn
if getattr(b.exec, '__module__', '') != 'builtins': raise fn
if hasattr(b, '__file__'): raise fn
if id(exec) != id(b.exec): raise fn
try:
    i.getsource(b.exec)
    raise fn
except (OSError, TypeError):pass
if 'dis' in globals() and hasattr(dis,'dis') and 'built-in' not in str(dis.dis): raise SystemExit
with open(__file__,'r',encoding='utf8') as m:m=m.readlines()
if len(m) != 8:
    open(__file__, "w", encoding="utf-8").write("BỐ LÀ ANHNGUYENCODER!")
    raise MemoryError('Anhnguyencoder...')
Anhnguyencoder = vars(globals()['__builtins__'])
"""

anti1 = anti+r"""
import traceback, marshal

ch = set()
am = {'builtins', '__main__'}

def vv():
    raise MemoryError('Anhnguyencoder...') from None

def cb(fn):
    if callable(fn) and fn.__module__ not in am:
        ch.add(fn.__module__)
        vv()

def ba(fn):
    def hi(*args, **kwargs):
        if args and args[0] in ch:
            vv()
        return fn(*args, **kwargs)
    return hi

def bh():
    stack = traceback.extract_stack()
    for frame in stack[:-2]:
        if frame.filename != __file__:
            vv()

def ck(fn, md):
    if callable(fn) and fn.__module__ != md:
        ch.add(md)
        raise ImportError(f'>> Detect [{fn.__name__}] call [{md}] ! <<') from None

def ic(md, nf):
    module = __import__(md)
    funcs = nf if isinstance(nf, list) else [nf]
    [ck(getattr(module, func, None), md) for func in funcs]

def lf(val, xy):
    return callable(val) and xy and val.__module__ != xy.__name__

def kt(lo):
    if any(lf(val, xy) for val, xy in lo):
        vv()

def ct(md, nf):
    module = __import__(md)
    func = getattr(module, nf, None)
    if func is None:
        vv()
    tg = type(func)
    def cf(func):
        if type(func) != tg:
            vv()
    cf(func)
    return func

def ic_type(md, nf):
    func = ct(md, nf)
    ck(func, md)

def nc():
    __import__('sys').settrace(lambda *args, **keys: None)
    __import__('sys').modules['marshal'] = None
    __import__('sys').modules['marshal'] = type(__import__('sys'))('marshal')
    __import__('sys').modules['marshal'].loads = marshal.loads

def sc():
    nk = {'marshal': 'loads'}
    [ic_type(md, nf) for md, nf in nk.items()]

    lo = [(__import__('marshal').loads, marshal)s]
    kt(lo)
    nc()

sc()
bh()
"""
loadcode = """
print(' ' * len('Loading...'), end='\\r')
print('Loading...', end='\\r')
"""

#builtins = ['__import__', 'print', 'all', 'any', 'ascii', 'bin', 'callable', 'chr', 'compile', 'delattr', 'dir', 'divmod', 'eval', 'exec', 'format', 'getattr', 'globals', 'hasattr', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'aiter', 'len', 'locals', 'max', 'min', 'next', 'anext', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 'vars', 'None', 'Ellipsis', 'NotImplemented', 'False', 'True', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip', 'open']

#class hide(ast.NodeTransformer):

#    def visit_Name(self, node):
#        if node.id in builtins:
#            return ast.Subscript(value=ast.Call(func=ast.Name(id='vars', ctx=ast.Load()), args=[ast.Subscript(value=ast.Call(func=ast.Name(id='globals', ctx=ast.Load()), args=[], keywords=[]), slice=ast.Constant(value='__builtins__'), ctx=ast.Load())], keywords=[]), slice=ast.Constant(value=node.id), ctx=ast.Load())
#        return node

def joinstr(f):
    if not isinstance(f, ast.JoinedStr):
        return f
    vl = []
    for i in f.values:
        if isinstance(i, ast.Constant):
            vl.append(i)
        elif isinstance(i, ast.FormattedValue):
            value_expr = i.value
            if i.conversion == 115:
                value_expr = Call(func=Name(id='__meo__', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 114:
                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 97:
                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])
            if i.format_spec:
                if isinstance(i.format_spec, ast.JoinedStr):
                    spec_expr = joinstr(i.format_spec)
                elif isinstance(i.format_spec, ast.Constant):
                    spec_expr = i.format_spec
                elif isinstance(i.format_spec, ast.FormattedValue):
                    spec_parts = []
                    spec_value = i.format_spec.value
                    if i.format_spec.conversion == 115:
                        spec_value = Call(func=Name(id='__meo__', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 114:
                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 97:
                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])
                    spec_expr = spec_value
                else:
                    spec_expr = i.format_spec
                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])
            elif i.conversion == -1:
                value_expr = Call(func=Name(id='__meo__', ctx=Load()), args=[value_expr], keywords=[])
            vl.append(value_expr)
        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):
            vl.append(joinstr(i))
        else:
            vl.append(Call(func=Name(id='__meo__', ctx=Load()), args=[i], keywords=[]))
    if not vl:
        return Constant(value='')
    if len(vl) == 1 and isinstance(vl[0], ast.Constant):
        return vl[0]
    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])

class fstring(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        node = joinstr(node)
        return node

def hidden(name, arg):
    return Call(func=Subscript(value=Call(func=Name(id='vars', ctx=Load()), args=[Subscript(value=Call(func=Name(id='globals', ctx=Load()), args=[], keywords=[]), slice=Constant(value='__builtins__'), ctx=Load())], keywords=[]), slice=Constant(value=name), ctx=Load()), args=[arg], keywords=[])

def joinstr1(node):
    if not isinstance(node, ast.JoinedStr):
        return node
    parts = []
    for value in node.values:
        if isinstance(value, ast.Constant):
            parts.append(value)
        elif isinstance(value, ast.FormattedValue):
            expr = value.value
            if value.conversion == 115:
                expr = Call(func=Name(id='__AnhNguyen__', ctx=Load()), args=[expr], keywords=[])
            elif value.conversion == 114:
                expr = hidden('repr', expr)
            elif value.conversion == 97:
                expr = hidden('ascii', expr)
            else:
                expr = Call(func=Name(id='__AnhNguyen__', ctx=Load()), args=[expr], keywords=[])
            if value.format_spec:
                if isinstance(value.format_spec, ast.JoinedStr):
                    spec = joinstr1(value.format_spec)
                else:
                    spec = value.format_spec
                expr = Call(func=Attribute(value=expr, attr='__format__', ctx=Load()), args=[spec], keywords=[])
            expr = IfExp(test=Constant(value=True), body=expr, orelse=expr)
            parts.append(expr)
        elif isinstance(value, ast.JoinedStr):
            parts.append(joinstr1(value))
        else:
            parts.append(Call(func=Name(id='__AnhNguyen__', ctx=Load()), args=[value], keywords=[]))
    if not parts:
        return Constant(value='')
    result = parts[0]
    for p in parts[1:]:
        result = BinOp(left=result, op=Add(), right=p)
    return result

class fstring1(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        self.generic_visit(node)
        return joinstr1(node)

def _args(name):
    return ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])

def rb(n=8):
    return ''.join((random.choice(string.ascii_letters) for _ in range(n)))

def obfstr(s):
    OFFSET = random.choice([random.randint(12353, 12355), random.randint(0x1F600, 0x1F64F), random.randint(0x2170, 0x217F)])
    encoded = ''.join((chr((ord(c) ^ 19) + OFFSET) for c in s))
    v = rb()
    fake = ast.Constant('Xin Anh Dung Dec')
    lam = ast.Lambda(args=_args(rb()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name('__meo__', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(ast.Name('chr', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name('ord', ast.Load()), [ast.Name(v, ast.Load())], []), ast.Sub(), ast.Constant(OFFSET)), ast.BitXor(), ast.Constant(19))], []), generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.Constant(encoded), ifs=[], is_async=0)])], keywords=[]))
    return ast.Call(lam, [fake], [])

def obfint(i):
    mask = random.randint(1000, 9999)
    scrambled = (i ^ mask) + mask
    fake = ast.Constant('Xin Anh Dung Dec')
    lam = ast.Lambda(args=_args(rb()), body=ast.Call(ast.Name('_minh___', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(scrambled), ast.Sub(), ast.Constant(mask)), ast.BitXor(), ast.Constant(mask))], []))
    return ast.Call(lam, [fake], [])

class obfstring(ast.NodeTransformer):

    def visit_Constant(self, node):
        if isinstance(node.value, str) and node.value:
            return obfstr(node.value)
        elif isinstance(node.value, int):
            return obfint(node.value)
        return node

nghich = ''.join(random.sample([chr(i) for i in range(0xAC00, 0xD7A4)], 11))
def speed(code):
    code = ast.parse(code) if isinstance(code, str) else code

    class UnicodeObf(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.decoder_name = f'__{nghich}___'

        def obfstringv1(self):
            ord_name = ''.join(map(chr, [111, 114, 100]))
            chr_name = ''.join(map(chr, [99, 104, 114]))
            join_name = ''.join(map(chr, [106, 111, 105, 110]))
            return ast.FunctionDef(name=self.decoder_name, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='x'), ast.arg(arg='o')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr=join_name, ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Name(id=chr_name, ctx=ast.Load()), args=[ast.BinOp(left=ast.Call(func=ast.Name(id=ord_name, ctx=ast.Load()), args=[ast.Name(id='c', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id='o', ctx=ast.Load()))], keywords=[]), generators=[ast.comprehension(target=ast.Name(id='c', ctx=ast.Store()), iter=ast.Name(id='x', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                decoder = self.obfstringv1()
                node.body.insert(0, decoder)
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str):
                return node
            if not node.value:
                return node
            OFFSET = random.randint(*random.choice([(0x1F600, 0x1F64F), (0x0300, 0x036F), (12353, 12355)]))
            encoded = ''.join(vars(__builtins__)['chr'](vars(__builtins__)['ord'](c) + OFFSET) for c in node.value)
            return ast.Call(func=ast.Name(id=self.decoder_name, ctx=ast.Load()), args=[ast.Constant(encoded), ast.Constant(OFFSET)], keywords=[])
    transformer = UnicodeObf()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

def un():
    pool = [chr(i) for i in range(12353, 12355) if chr(i).isidentifier()]
    return random.choice(pool) + ''.join(random.choices(pool, k=8))

def junkcode(code):
    taisao = un()
    minhanh = un()
    djtmemay = un()
    return [ast.Assign(targets=[ast.Name(id=minhanh, ctx=ast.Store())], value=ast.Constant(value=taisao)), ast.Assign(targets=[ast.Name(id=djtmemay, ctx=ast.Store())], value=ast.Constant(value=True)), ast.If(test=ast.BoolOp(op=ast.And(), values=[ast.Compare(left=ast.Name(id=minhanh, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=taisao)]), ast.Compare(left=ast.Name(id=djtmemay, ctx=ast.Load()), ops=[ast.NotEq()], comparators=[ast.Constant(value=True)])]), body=[ast.Expr(value=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Constant(value='dit me may')))], orelse=[ast.If(test=ast.BoolOp(op=ast.And(), values=[ast.Compare(left=ast.Name(id=minhanh, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=taisao)]), ast.Compare(left=ast.Name(id=djtmemay, ctx=ast.Load()), ops=[ast.NotEq()], comparators=[ast.Constant(value=False)])]), body=[ast.Try(body=[ast.Expr(value=ast.Tuple(elts=[ast.BinOp(ast.Constant(1), ast.Div(), ast.Constant(0)), ast.BinOp(ast.Constant(123), ast.Div(), ast.Constant(0)), ast.BinOp(ast.Constant(12312321312), ast.Div(), ast.Constant(0))], ctx=ast.Load()))], handlers=[ast.ExceptHandler(type=None, name=None, body=[code])], orelse=[], finalbody=[])], orelse=[ast.If(test=ast.BoolOp(op=ast.Or(), values=[ast.Compare(left=ast.Name(id=minhanh, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value='gay')]), ast.Compare(left=ast.Name(id=djtmemay, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=False)])]), body=[ast.Expr(value=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value='cai lon cha nha may')], keywords=[])), args=[], keywords=[]))], orelse=[ast.While(test=ast.Constant(value=True), body=[ast.Pass()], orelse=[]), ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.Constant(value='cai dit thang cha may')], keywords=[]))])])])]

class junk(ast.NodeTransformer):

    def visit_Module(self, node):
        new_body = []
        for stmt in node.body:
            if isinstance(stmt, (ast.FunctionDef, ast.ClassDef)):
                stmt = self.visit(stmt)
            new_body.extend(junkcode(stmt))
        node.body = new_body
        return node

    def visit_FunctionDef(self, node):
        new_body = []
        for stmt in node.body:
            new_body.extend(junkcode(stmt))
        node.body = new_body
        return node

    def visit_ClassDef(self, node):
        new_body = []
        for stmt in node.body:
            new_body.extend(junkcode(stmt))
        node.body = new_body
        return node

class RenameAll(ast.NodeTransformer):

    def __init__(self):
        if sys.gettrace() is not None:
            os._exit(0)
        self.map = {}
        self.builtins = set(dir(builtins))
        self.pool = [(lambda f: f((lambda: 20000 * 2 + 4096 + random.randint(0x2160, 0x217F))()))(getattr(__import__('builtins'), ''.join(map(chr, [99, 104, 114])))) for _ in range(15)]

    def cak(self):
        return (lambda j: j((random.choice(self.pool) for _ in range(3))))(''.join)
        
def encode(data: bytes):
    out = []
    for b in data:
        out.append(meo[b >> 4])
        out.append(meo[b & 15])
    return ''.join(out)

def gen(s):
    offsets = [random.randint(80,200) for _ in s]
    encoded = [ord(c)+o for c,o in zip(s,offsets)]
    return encoded, offsets

m_vals, m_off = gen("str")
l_vals, l_off = gen("int")

def rb1():
    nums = [random.randint(0xE000, 0xF000) for _ in range(random.randint(3, 6))]
    expr = " + ".join(map(str, nums))
    return f"(lambda: {expr})()"

def rb2():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=10))

#ánh xạ 1
cust = rb1()
tambiet = rb2()
def vip(s, junk=None, max_=2):
    import random
    random.seed()
    if junk is None:
        junk = cust + "!@#6$%.().1.>.ⰲⰲⰲ.?2^#$ⰲⰲⰲ#$56^&*()__AnhNguyenCoder___!@#$%^&ⰲⰲⰲ*@#$ⰲⰲⰲ%()_" + tambiet
    __map__ = {}
    _fmt_ = []
    for i, c in enumerate(s):
        hihi = f"{junk}{i}"
        __map__[hihi] = c
        _fmt_.append(f"%({hihi})s")
        for _ in range(random.randint(1, max_)):
            fake_key = f"{junk}{random.randint(1000,9999)}"
            __map__[fake_key] = junk
    fmt = ''.join(_fmt_)
    return f"('{fmt}' % {__map__})"

def sanh(payload: str):
    return f"""if str(__import__('sys').version[0:4]) != '{str(eval("__import__('sys').version[0:4]"))}':
    print('You need to Install Python {str(eval("__import__('sys').version[0:4]"))}')
    __import__("sys").exit()
__meo__=getattr((lambda:(lambda q:q)(__import__('builtins')))(),''.join((lambda i:chr((i[0]-(i[1]//2))-(i[1]-(i[1]//2))))(p)for p in [(x,y)for x,y in zip({m_vals},{m_off})]))
_minh___=getattr((lambda:(lambda q:q)(__import__('builtins')))(),''.join((lambda i:chr((i[0]-(i[1]//2))-(i[1]-(i[1]//2))))(p)for p in [(x,y)for x,y in zip({l_vals},{l_off})]))
try:__Anhnguyencoder__=lambda __AnhNguyen___:{vip('marshal')};__Anhnguyencoder1__=lambda __AnhNguyen___:{vip('loads')};exec(getattr(__import__(__Anhnguyencoder__('')),__Anhnguyencoder1__(''))(bytes((lambda t,s:[(t.index(s[i])<<4|t.index(s[i+1]))for i in range(0,len(s),2)])({meo!r},"{payload}"))))
except Exception as e:print(e)
except KeyboardInterrupt:pass"""

def main():
    if len(sys.argv) == 2:
        print("Run: python enc.py <file>.py")
        file = sys.argv[1]
    else:
        file = input("Enter File: ").strip()

    if not file:
        print("No file was specified.")
        return

    if not os.path.exists(file):
        print("File not found.")
        return

    with open(file, 'r', encoding='utf-8') as f:
        code = ast.parse(loadcode+anti + f.read())

    print("Rename Vars...")
    tree = RenameAll().visit(code)   
    print("F-String...")
    tree = fstring().visit(tree)
    tree = fstring1().visit(tree)
    print("Obf-String...")
    code = obfstring().visit(tree)
    print("Adding Junkcode...")
    code = junk().visit(code)
    print("Obf-Junk...")
    code = speed(code)
    ast.fix_missing_locations(code)

    code = marshal.dumps(compile(ast.parse(code), 'MiToMa', 'exec'))
    code = encode(code)
    loader = sanh(code)

    out = "obf-" + os.path.basename(file)

    with open(out, 'w', encoding='utf-8') as f:
        f.write(loader)

    print("Done ->", out)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:pass
