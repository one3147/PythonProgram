import os
output = os.popen('lsof -i:8000').read()


pids = []
lines = output.split('\n')
for line in lines:
    if 'CLOSE_WAIT' in line:
        parts = line.split()
        pids.append(parts[1])

for pid in pids:
    print(pid)
    os.system(f'kill -9 {pid}')
    

