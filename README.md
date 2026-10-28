## 🔐 Anhnguyencoder Python Obfuscator

Advanced AST + Marshal + Unicode Hybrid Obfuscation
Author: Anhnguyencoder

## 📌 Introduction

Anhnguyencoder Obfuscator is an advanced Python protection tool that combines multiple obfuscation and anti-analysis techniques, including:

AST Transformation

Marshal bytecode encoding

Multi-range Unicode encoding

Builtins hiding

Anti-hook protection

Anti-tamper verification

Control flow obfuscation

Junk code injection

Its primary goal is to make source code extremely difficult to read, decompile, dump, or analyze through static and dynamic methods.

## ⚙️ Core Features

# 1️⃣ AST Transformation Engine

The obfuscator uses ast.NodeTransformer to:

Hide all built-in function calls

Convert f-strings into runtime .join() constructions

Obfuscate:

String constants

Integer constants

Inject dynamically generated Unicode-named decoder functions

# 2️⃣ String Obfuscation Layer

Strings are encoded using the following formula:

encoded_char = chr((ord(c) ^ 19) + OFFSET)

Where:

OFFSET is randomly selected from multiple Unicode ranges:

Emoji range (0x1F600–0x1F64F)

Combining marks (0x0300–0x036F)

Japanese ranges

Roman numeral blocks

A decoder function is dynamically injected into the module.

The original string is only reconstructed at runtime.

# 3️⃣ Integer Obfuscation

Integers are scrambled using:

scrambled = (i ^ mask) + mask

They are restored at runtime via dynamically generated lambda functions.

# 4️⃣ Builtins Hiding

Instead of calling builtins directly:

print("Hello")

They are transformed into indirect lookups:

vars(globals()['__builtins__'])['print']

Additionally:

print, eval, and exec are removed from globals()

Runtime integrity checks verify original builtins

If builtins are hooked or modified → execution stops

# 5️⃣ Anti-Hook Protection

The class:

__ngan_hook_builtins__

Verifies integrity of:

builtins.print

builtins.exec

builtins.eval

If any of these are altered, the program terminates immediately.

# 6️⃣ Anti-Tamper System

The obfuscated output performs several integrity checks:

Python version must match the encoding environment

File content must not be modified

File length must remain unchanged

exit, print, exec, input, len must not be overridden

marshal.loads must remain intact

The dis module must not be hooked

If tampering is detected:

raise MemoryError('Anhnguyencoder...')
# 7️⃣ Junk Code Injection

The obfuscator injects:

Fake conditional branches

Useless lambda expressions

Infinite loops

Deliberate division-by-zero blocks inside try/except

Illogical boolean conditions

Purpose:

Break control flow graph reconstruction

Crash naive decompilers

Increase static analysis complexity

# 8️⃣ Marshal Encoding Layer

Pipeline:

Original Source
→ AST Transform
→ Compile
→ marshal.dumps
→ Custom Unicode Encoding (16-character map)
→ Runtime Loader
→ Unicode Decode
→ marshal.loads
→ exec

The original source code never appears in plain text.

##🔁 Control Flow Overview
main()

    │
    
    ├── Parse AST
    
    │
    
    ├── fstring() transformation
    
    │
    
    ├── hide() builtins transformation
    
    │
    
    ├── obfstring() (string + integer obfuscation)
    
    │
    
    ├── speed() (Unicode string encoding v2)
    
    │
    
    ├── junk() inject control flow distortion
    
    │
    
    ├── compile()
    
    │
    
    ├── marshal.dumps()
    
    │
    
    ├── encode() → Unicode mapping
    
    │
    
    └── sanh() → Build runtime loader
    
            │
            
            ├── Version check
            
            ├── Anti-hook verification
            
            ├── Anti-tamper validation
            
            ├── Unicode decode
            
            ├── marshal.loads
            
            └── exec
## 🛡️ Protection Layers Summary
Layer	Purpose
AST Layer	Structural transformation
String Layer	XOR + OFFSET + Unicode encoding
Integer Layer	Mask-based scrambling
Builtins Hiding	Indirect runtime lookup
Anti-Hook	Builtins integrity verification
Anti-Tamper	File & environment validation
Junk Code	Control flow distortion
Marshal Encoding	Bytecode-level protection
##🚀 Usage
python enc.py target.py

Output -> obf-<file>.py

## 📁 Output Characteristics

The generated file:

Does not contain original source code

Does not contain original strings

Does not contain original integers

Does not call builtins directly

Will not execute in a mismatched Python version

Will terminate if tampered with

## 👤 Author

Anhnguyencoder

Specialization:

Python Obfuscation

AST manipulation

Marshal encoding

Unicode polymorphism

Anti-hook and anti-debug protection

Control flow distortion

Each encoding run produces a completely different output due to heavy randomization.

## 🔥 Key Strengths

Fully randomized Unicode function names

Random OFFSET per string

Random mask per integer

Random junk injection

Random Unicode mapping tables

Every obfuscation process produces a unique result.

## ⚠️ Requirements

Python version must match the encoding environment

Do not modify the output file

Do not hook builtins

Avoid debugging tools that override runtime functions

## 📜 Disclaimer

This tool is intended for:

Source code protection

Reverse engineering resistance

Research and educational purposes

The author is not responsible for misuse.

## ☎️ Contact
- t.me/ctevclwar
- https://www.facebook.com/anhnguyencoder.izumkonata
