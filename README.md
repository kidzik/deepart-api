# deepart-api

## Install requirements

```bash
pip install -r requirements.txt
```

## Update settings.py

In `settings.py` specify your login, password, and paths to content and style files
```bash
DEEPART_LOGIN="login"
DEEPART_PASSWORD="password"
DEEPART_CONTENT="content.jpg"
DEEPART_STYLE="style.jpg"
```

## Uplooad content and style

To upload content and style run the `submit scritpt`
```bash
python submit.py
```
It should return the ID of a new image
```bash
{"id":4520139}
Images submitted succesfully
```

## Get results
Check the status by running
```bash
python getresult.py 4520139
```
At first you will get `processing` status like this
```json
{"status":"processing","result":""}
```
but at some point it will turn to `done` and will return a url of the result
```json
{"status":"done","result":"https://deepart-io.s3.amazonaws.com/results/d7ca10ed2b14b1a1-4520139.png"}
```
