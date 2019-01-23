import subprocess
import select 
packet = '' 
in_packet = False
result = subprocess.Popen(['minimodem', '--rx', '4800'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True : 
    readers, _, _ = select.select([result.stdout, result.stderr],[],[])
    if in_packet:
        if result.stdout in readers:
            data = result.stdout.read(1) 
            if not data: 
                break 
            packet += data.decode('ISO-8859-1') 
            continue 
    if result.stderr in readers:
        line = result.stderr.readline()
        if not line: 
            break
        if line.startswith(b'### CARRIER '):
            in_packet = True
            packet = ''
        elif line.startswith(b'### NOCARRIER '):
            in_packet = False
            print (packet)
                
