import time
import subprocess
import select

FILENAME = "test_log.log"

 f = subprocess.Popen(['tail', '-F', FILENAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 p = select.poll() ### select.poll is not supported in BSD???
 p.register(f.stdout) .register is part of .poll...

 while True:
    if p.poll(1):
        print f.stdout.readline()
    time.sleep(1)
