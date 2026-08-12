

OlapDb Tools

A set of Tools For OlapDb

olapdump - dump mysql/starrocks/doris table structure

# Setup

requirement python3

```
pip install argparse
pip install pymysql
```


# Usage

python olapdump.py [-h HOST] [-P PORT] [-u USER]
                    [-p PASSWORD] [-d DATABASE]

example:
python olapdump.py -h 127.0.0.1 -P 9030 -u root -d dtest > dump.sql
