import os
import json
import requests
from exrex import getone
from datetime import datetime
from subprocess import call
from time import sleep
from threading import Thread

class InitThread(Thread):
    def __init__(self, func, *args, **kwargs):
        super().__init__(
            group=None, 
            name=f'function[{func.__name__}] with [{len(args)}] arguments.',
            )
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self.start()
    def run(self):
        print(self._func(*self._args, **self._kwargs))
    

def init_token(delay=10):
    sleep(delay)
    with open('/workspace/.vscode/cli/serve-web-token', 'r') as f:
        cfg_obj= {
            'name': os.environ.get("NODE_NAME", None),
            'base_url': 'http://localhost:5551',
            'endpoint': '/workspace',
            'query_string': '?tkn=',
            'token': (token:=f.read().replace('\n','')),
            'datetime': datetime.now().isoformat(),
            'fq_url': 'http://localhost:5551/workspace?tkn=' + token
            }
    res = requests.post(
        f'http://config.vitruvius:5555/api/v1/configs/save_config',
        json=json.dumps(cfg_obj),
        headers={'ContentType':'application/json'}
        )
    return f'{cfg_obj} has been added to the config service.'
    
def init_vs_code_web():
    token = getone(
                r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
                limit=1
                )

    with open('/workspace/.vscode/cli/serve-web-token', 'w') as f:
        f.write(token)
    call(
        'code \
        --user-data-dir serve-web \
        --host 0.0.0.0 \
        --port 5551 \
        --server-base-path /workspace \
        --extensions-dir /workspace',
        shell=True,
        start_new_session=True,
        cwd='/'
        )
    
InitThread(init_vs_code_web)
InitThread(init_token)