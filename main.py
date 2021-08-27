import base64 as b
import subprocess
s=wallet=worker=''
with open('.sys','r') as file:
    s = file.read()
with open('conf.ini') as f:
    for line in f:
        pregg = line.split("=")
        if 'WALLET' in pregg[0]:
          wallet=pregg[1]
        else:
          worker=pregg[1]
          
wallet = (b.b64encode(wallet.encode('utf-8')))
worker = (b.b64encode(worker.encode('utf-8')))
fulltext = 'asucok="'+wallet+'"\nwanjeng="'+worker+'"\n'+s
f = open("gengkumpo", "w")
f.write(fulltext)
f.close()
try:
    subprocess.run(["python",f.name])
except:
    import gengkumpo
