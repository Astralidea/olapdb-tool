Doris Tools

A set of tools for Doris

dorisdump - dump doris table structure

# Setup

requirement python3

```
pip install argparse
pip install pymysql
```


# Usage

python dorisdump.py [--host HOST] [--port PORT] [--user USER]
                    [--password PASSWORD] [--database DATABASE]

example:
python dorisdump.py -h 127.0.0.1 -P 9030 -u root -d dtest > dump.sql
