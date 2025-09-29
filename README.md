# Zone DNS autoupdater
## Usage
> Don't forget to fill your .env with your data and put PROD to true

```
pip install -r requirements.txt
python3 main.py
```

## Sample crontab
Here's a sample crontab i use:
```
0 * * * * python3 /path/to/project/main.py
```
