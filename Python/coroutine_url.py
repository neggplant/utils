#!/usr/local/envs/bin/python
# -*- encoding:utf-8 -*-
# 使用协程获取接口数据

import time
import aiohttp
import asyncio
print(time.strftime("%S"))
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        # print(html)
        return html

async def main():
    a_list = [asyncio.create_task(get_html('http://127.0.0.1:7777/')), asyncio.create_task(get_html('http://127.0.0.1:7777/'))]
    # await asyncio.sleep(0.0001)
    # print("run_async",a)
    done, pending = await asyncio.wait(a_list)
    for i in done:
        print(i.result())


asyncio.run(main())

print(time.strftime("%S"))
