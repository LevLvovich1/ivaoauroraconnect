# IvaoAuroraConnect Library #
https://pypi.org/project/ivaoauroraconnect/
## What is this? ##
Allows to get data from IVAO Aurora started on user`s computer

## Quick Guide ##

----------


### Using ###

1.import this library

```python
import ivaoauroraconnect
```

2.create a connection to Aurora 
```python
aurora = ivaoauroraconnect.Connection()
```
3.use the commands. 
```python
print(aurora.conn())
```
4.close the connection.
```python
aurora.close()
```
**OR use context manager**
```python
with ivaoauroraconnect.Connection() as aurora
```
Using the context manager does not require closing the connection.


We have commands, provided by ivao. To use these commands, use the method with the same name in lowercase in your code.

#### Examples

default
```python
import ivaoauroraconnect


aurora = ivaoauroraconnect.Connection()

for cs in aurora.tr():
	print(cs)
	
aurora.close()
```

with context manager
```python
import ivaoauroraconnect


with ivaoauroraconnect.Connection() as aurora:
	for cs in aurora.tr():
		print(cs)
```

### Commands list

| Command             | Action                                                    | Arguments                                                                                                                                                                                                  |
| ------------------- | --------------------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR                  | Returns traffic in range                                  |                                                                                                                                                                                                            |
| FP                  | Returns FPLN                                              | `cs`                                                                                                                                                                                                       |
| FP_S                | Returns FPLN for selected acft                            |                                                                                                                                                                                                            |
| SELTFC              | Returns selected traffic callsign                         |                                                                                                                                                                                                            |
| TRPOS               | Returns traffic position                                  | `cs`                                                                                                                                                                                                       |
| TRPOS_S             | Return selected traffic position                          |                                                                                                                                                                                                            |
| TRAS                | Assume traffic                                            | `cs`                                                                                                                                                                                                       |
| TRAS_S              | Assume selected acft                                      |                                                                                                                                                                                                            |
| TRRE                | Release traffic                                           | `cs`                                                                                                                                                                                                       |
| TRRE_S              | Release selected acft                                     |                                                                                                                                                                                                            |
| ZTR                 | Zoom traffic                                              | `cs`                                                                                                                                                                                                       |
| ZTR_S               | Zoom selected traffic                                     |                                                                                                                                                                                                            |
| ZSTR                | Select and zoom traffic                                   | `cs`                                                                                                                                                                                                       |
| LBWP                | Set waypoint to acft strips                               | `cs` `wp`                                                                                                                                                                                                  |
| LBWP_S              | Set waypoint to selected acft strips                      | `wp`                                                                                                                                                                                                       |
| LBALT               | Set altitude to acft strips                               | `cs` `alt`                                                                                                                                                                                                 |
| LBALT_S             | Set altitude to selected acft strips                      | `alt`                                                                                                                                                                                                      |
| LBSPD               | Set speed to acft strips                                  | `cs` `spd`                                                                                                                                                                                                 |
| LBSPD_S             | Set speed to selected acft strips                         | `spd`                                                                                                                                                                                                      |
| LBSQK               | Set squawk to acft strips                                 | `cs` `sqk`                                                                                                                                                                                                 |
| LBSQK_S             | Set squawk to selected acft strips                        | `sqk`                                                                                                                                                                                                      |
| TRSQK               | Returns generated SQK ==NOT PROVIDED==                    | `cs`                                                                                                                                                                                                       |
| TRSQK_S             | TReturns generated SQK for selected acft ==NOT PROVIDED== |                                                                                                                                                                                                            |
| ATC                 | Returns ATC in range                                      |                                                                                                                                                                                                            |
| ATCT                | Returns ATC in transfer list                              |                                                                                                                                                                                                            |
| ATCTA               | Add ATC to transfer list                                  | `atc`                                                                                                                                                                                                      |
| ATCTR               | Remove ATC from ransfer list                              | `atc`                                                                                                                                                                                                      |
| MSGFR               | Send message to primary frequency                         | `cs` `text`                                                                                                                                                                                                |
| MSGPM               | Send PM                                                   | `cs` `text`                                                                                                                                                                                                |
| TRPATHL             | Returns ETO for FIXs in route                             |                                                                                                                                                                                                            |
| METAR               | Returns METAR                                             | `icao`                                                                                                                                                                                                     |
| BAY                 | Open Baylist                                              |                                                                                                                                                                                                            |
| ATIS                | Returns ATIS                                              |                                                                                                                                                                                                            |
| CTRL                | Returns controlled airports                               |                                                                                                                                                                                                            |
| CTRLRWY             | Returns controlled airports and RWYs                      |                                                                                                                                                                                                            |
| CONN                | Returns user callsign                                     |                                                                                                                                                                                                            |
| CTO                 | Zoom to navaid                                            | `navaid`                                                                                                                                                                                                   |
| ZTO                 | Zoom to *???*                                             | `zoom`                                                                                                                                                                                                     |
| LBGTE               | Set gate for acft                                         | `cs` `gate`                                                                                                                                                                                                |
| LBGTE_S             | Set gate for selected acft                                | `gate`                                                                                                                                                                                                     |
| INTERCOMCALL        | Make intercom call                                        | `cs`                                                                                                                                                                                                       |
| INTERCOMANSWER      | Answer incoming intercom call                             |                                                                                                                                                                                                            |
| INTERCOMREJECT      | Reject incoming intercom call                             |                                                                                                                                                                                                            |
| INTERCOMPHONESTATUS | Returns intercom status                                   | PHONE_RECEIVING<br>PHONE_PERFORMING<br>PHONE_ONGOING<br>PHONE_RESET                                                                                                                                        |
| INTERCOMCALLSTATUS  | Returns incoming call status                              | status:<br>CALL_RESULT_OUT_OK<br>CALL_RESULT_IN_OK<br>CALL_RESULT_IN_MISSED<br>CALL_RESULT_OUT_FAIL<br>CALL_NIL<br>reject_reason:<br>CALL_CALLEE_NOT_CONNECTED<br>CALL_CALLEE_REJECT<br>CALL_SERVER_REJECT |
