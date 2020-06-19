# %%
from aiohttp import web
import asyncio
import datetime
from gitapp import get_req
import logging
from io import StringIO
import csv
from shared.db_util import db_conn
import pandas as pd


# %%
async def index(request):
    return web.Response(text='Im up S4N!')


# %%

async def get_users(request):
    time = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    try:
        users = await request.json()
        if type(users) == list and len(users) > 0:
            # print(f'{users} and type {type(users)}')
            pool = {usr: {} for usr in users}
            for i in users:
                begin_time = datetime.datetime.now()
                await asyncio.gather(get_req(i, 'gists', pool), get_req(i, 'events', pool))
                print(datetime.datetime.now() - begin_time)
            event = {'Response_place': 'get_users',
                     'Response_type': 'Valid_request'}
            logging.info(f'{time}:{event}')
            conn = db_conn()
            sio = StringIO()
            df = pd.DataFrame({'user_git': [u for u in users],
                               'gists': [pool[g]['gists'] for g in users],
                               'events': [pool[e]['events'] for e in users]})
            sio.write(df.to_csv(index=None, header=None, sep=';', encoding='utf8',
                                quoting=csv.QUOTE_NONE))
            sio.seek(0)  # Be sure to reset the position to the start of the stream
            with conn.cursor() as cursor:
                cursor.copy_from(sio, "s4n_github", columns=df.columns, sep=';')
                conn.commit()
            return web.json_response(pool)
        else:
            event = {'Response_place': 'get_users',
                     'Response_type': ' Invalid_request'}
            logging.error(f'{time}:{event}')
            return web.json_response({'response': """request is not a list type
                                                     or length is not valid"""})

    except Exception as exc:
        event = {'Exception_place': 'get_users',
                 'exception_type': type(exc).__name__,
                 'exception_args': exc.args}
        time = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        logging.error(f'{time}:{event}')
        raise exc


# %%



"""
data = ['danielaguirre708', 'fabpot',
        'andrew',
        'taylorotwell',
        'egoist',
        'HugoGiraudel']
import json
import requests
data_json = json.dumps(data)

res=requests.post(url='http://127.0.0.1:8080/get_users',data=data_json)

"""

