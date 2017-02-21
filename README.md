sampel communication with astm e1381 protocol.

ready on pip

```
pip install astm-serial
```

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