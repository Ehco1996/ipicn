# ipicn

A tool to help determine whether ip is in China.

## explain the principle

ipinc use GeoDatabase: `[GeoIP2-CN](https://github.com/Hackl0us/GeoIP2-CN)` to find ip location.

It only provide one api to judge you input ip/domain is in China.

## Install

 `pip install ipicn`

Note that `ipicn` will download geo database from `https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb` if the current directory not contains this file.

if you want to update the latest database, just remove `Country.mmdb` and restart your program, or you can use `is_in_china(ip, update_database=True)`

## Example

``` python
from ipicn import is_in_china

is_in_china("www.baidu.com")
>> True

is_in_china("www.google.com")
>> False

# force update geo database
is_in_china(www.google.com, update_database=True)
>> False
```
