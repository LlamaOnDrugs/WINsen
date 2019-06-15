# Quantis Network Sentinel

All masternodes must run Sentinel.

Will update instructions soon.

1. Download [quansentinel.exe]
2. Create a sentinel.conf file in the same directory that you downloaded trcsentinel.exe with this inside:
quantisnet_conf=C:\Users\USERNAME\AppData\Roaming\QuantisNetCore\quantisnet.conf

Change the username part to your username on your computer.

3. Go into %appdata% QuantisNetCore

Open quantisnet.conf and make sure it has at least:

```rpcuser=someuser
rpcpassword=somepass
server=1
rpcport=13332
rpcconnect=127.0.0.1
```

Restart QuantisNet-QT and wait for it to sync.

Run quansentinel

Press 1.


# Building

Install pyinstaller `pip install pyinstaller`

Generate output EXE/ELF: `pyinstaller --onefile --paths=lib/ main.py`
