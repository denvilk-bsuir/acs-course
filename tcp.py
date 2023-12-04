# import os
import subprocess
# import datetime
import requests
import re

# cat dump.txt| grep "\[P.\]" | grep "IP 10.8.0.10" | awk ' { print $5 }'  FS=' ' | tail
# sudo tcpdump -tttt -i utun11 'src 10.8.0.10 and (dst port 80 or 443)'
run_cmd = ['sudo', 'tcpdump', '-tttt', '-i', 'utun11', 'src 10.8.0.10 and (dst port 80 or 443)']
# print(' '.join(run_cmd))

# dt = datetime.datetime.now()
# TIME = 60 #sec
# new = dt
# delta = 0
with open('dump.txt', "w+") as f:
    with subprocess.Popen(run_cmd, stdout=subprocess.PIPE) as proc:
        while (line := proc.stdout.readline()):
            # print(line.decode(), end="", file=f)
            ma = re.match(r'^(?P<time>.*)\sIP\s(?P<src>.*)\s>\s(?P<dst>.*):\s(Flags\s\[P\.]|quic)', line.decode())
            if (not ma):
                continue
            requests.post("http://localhost:8000/v1/api/", json={"destination": ma.group("dst"),"created_at": ma.group("time")})


