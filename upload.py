import sys

buffer = []
last_line = ''
for line in sys.stdin:
    buffer.append(line)
    last_line = line
print('Execution last line is: %s' % last_line)
report = ''.join(buffer)
print('report is:')
print(report)

