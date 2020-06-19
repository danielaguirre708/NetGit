
from typing import Dict
import aiohttp
import datetime
import logging

# %%
CONFIG = {'end_points': {'gists': {'type_response': list,
                                   'per_page': 3},
                         'events': {'type_response': Dict,
                                    'per_page': 5},
                         }
          }

# %%
BASE_URL = 'https://api.github.com/users/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Huawey_mate_book_pro; Intel Corei7 )'}


async def get_req(user_name, endp, pool):
    time = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    params = {'per_page': CONFIG['end_points'][endp]['per_page']}
    # for user_name in user_list:
    url = f'{BASE_URL}{user_name}/{endp}'
    print(f'Get last {params["per_page"]} {endp} for {user_name}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status == 200:
                if CONFIG['end_points'][endp]['type_response'] == Dict:
                    pool[user_name][endp] = {i['id']+'_'+i['type']: i for i in await resp.json()}
                elif CONFIG['end_points'][endp]['type_response'] == list:
                    pool[user_name][endp] = await resp.json()
            else:
                pool[user_name][endp] = f'Something works wrong please verify log file'
                event = {'Response_place': f'get_{endp}',
                         'Status': f'{resp.status}',
                         'message': f'{resp.json}'}
                logging.info(f'{time}:{event}')


