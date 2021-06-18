# so-xml-parser (demo)

- Installing with `pipenv install` is recommended.

- Output is as follows (see [`config.yaml`](config.yaml) for the, er, config).

```
$ pipenv run ./parse.py && sqlite3 -table output.sqlite "SELECT * FROM badges;"


Processing /home/simon/tmp/so-xml-parser/badges.xml...
Processing document 1...
...1 document processed!
Writing tables to /home/simon/tmp/so-xml-parser/output.sqlite ...
Writing 7626 rows to `badges`...
+------+-------+------------------+-------------------------+-------+-----------+
|  id  | user  |       name       |          date           | class | tag-based |
+------+-------+------------------+-------------------------+-------+-----------+
| 1    | 1     | Autobiographer   | 2013-12-17T20:38:43.550 | 3     | False     |
| 2    | 3     | Autobiographer   | 2013-12-17T20:38:43.550 | 3     | False     |
| 3    | 4     | Autobiographer   | 2013-12-17T20:38:43.550 | 3     | False     |
| 4    | 13    | Autobiographer   | 2013-12-17T20:53:40.320 | 3     | False     |
| 5    | 8     | Autobiographer   | 2013-12-17T21:40:48.927 | 3     | False     |
| 6    | 23    | Autobiographer   | 2013-12-17T21:45:46.917 | 3     | False     |
| 7    | 41    | Autobiographer   | 2013-12-17T22:05:47.040 | 3     | False     |
| 8    | 38    | Supporter        | 2013-12-17T22:05:47.040 | 3     | False     |
| 9    | 41    | Supporter        | 2013-12-17T22:05:47.040 | 3     | False     |
| 10   | 8     | Teacher          | 2013-12-17T22:05:47.040 | 3     | False     |
| 11   | 6     | Autobiographer   | 2013-12-17T22:15:50.757 | 3     | False     |
| 12   | 44    | Autobiographer   | 2013-12-17T22:20:50.780 | 3     | False     |
| 13   | 39    | Autobiographer   | 2013-12-17T23:01:07.293 | 3     | False     |

...

```
