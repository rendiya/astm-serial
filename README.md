sampel communication with astm e1381 protocol.

ready on pip

```
pip install astm-serial
```

for documentation please visit http://astm-serial.readthedocs.io/

under construction

schema communication:
```
client > ENQ
server > ACK
client > DATA
server > ACK
client > EOT
```
NAK handling
```
client > ???
server > NAK
client > EOT
```