print()
print("----Coded by SyphonArch----")
with open('calc.obj', 'rb') as f:
    contents = f.read()

print("Successfully read calc.obj")

code = ''
for i in range(0, len(contents), 2):
    hexstr = "x{:02x}{:02x}".format(contents[i], contents[i + 1])
    assert len(hexstr) == 5
    code += '.FILL ' + hexstr + '\n'

code = code.replace('.FILL', '.ORIG', 1)
code += '.END'

print("Successfully generated code.")
with open('fill-calc.asm', 'w') as f:
    f.write(code)

print("fill-calc.asm written to disk.")
print("---------------------------\n")
