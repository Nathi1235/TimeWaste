# TimeWaste
TimeWaste is an esoteric programming language.

It is based on Python3 and was created to ... well, waste your time.

Basically it is like standard Python3 but certain keywords can only be executed at certain times.

## Timetable:
|  Keyword  |      Time     |
|-----------|---------------|
|   while   | 00:00 - 01:00 |
|    for    | 01:00 - 02:00 |
|   print   | 02:00 - 03:00 |
|   input   | 03:00 - 04:00 |
|     if    | 04:00 - 05:00 |
|   import  | 05:00 - 06:00 |

## Usage
Windows:
```python .\TimeWaste_Interpreter.py .\testprogram.tW```

Linux:
```python3 .\TimeWaste_Interpreter.py .\testprogram.tW```

## Example Programs
### Hello World:
```
print("Hello World!")
```
It looks exactly like in Python, but the Output will only appear if the current time is between 2am and 3am.
If not, the program will wait until 2am.

### Cat Program:
```
text = input()
print(text)
```
This program will at least take 23 hours to complete.

<br>
<br>

> *Special Thanks to Luca Bombardelli and Sandro Fender, they helped a lot with the inspiration for the project.*
