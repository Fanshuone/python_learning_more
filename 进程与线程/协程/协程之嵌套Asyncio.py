# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import asyncio

async def print_sum(x,y):
    result = await  compute(x,y) # 等待下一个协程帮我计算
    print("%s+%s=%s"%(x,y,result))

async def compute(x,y):
    print("开始计算x：%s和y: %s"%(x,y))
    await asyncio.sleep(0)
    return y+x


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(10,20))
loop.close()