round(Zahl, Nachkommastellen)
rundet auf! 

time.time() 
returns time since the epoch (1970) in seconds


class time.struct_time
The type of the time value sequence returned by gmtime(), localtime(), and strptime(). It is an object with a named tuple interface: values can be accessed by index and by attribute name. The following values are present:

Index
Attribute
Values
0
tm_year
(for example, 1993)

1
tm_mon
range [1, 12]

2
tm_mday
range [1, 31]
3
tm_hour
range [0, 23]

4
tm_min
range [0, 59]

5
tm_sec
range [0, 61]; see Note (2) in strftime()

6
tm_wday
range [0, 6]; Monday is 0

7
tm_yday
range [1, 366]

8
tm_isdst
0, 1 or -1; see below

N/A
tm_zone
abbreviation of timezone name

N/A
tm_gmtoff
offset east of UTC in seconds