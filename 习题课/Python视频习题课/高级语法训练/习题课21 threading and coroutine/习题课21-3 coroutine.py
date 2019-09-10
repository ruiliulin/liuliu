# 用协程的方式完成播放

movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "大话西游.mp4"]
music_list = ['周杰伦.mp3', '五月天.mp3']
movie_format = ["mp4", "avi"]
music_format = ["mp3"]

import asyncio
import time

# async await

# @asyncio.coroutine
async def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("Now playing movie named: %s" % i)
            await asyncio.sleep(5)
        elif i.split(".")[1] in music_format:
            print("Now playing music named: %s" % i)
            await asyncio.sleep(3)
        else:
            print("NO SUPPORTED")

loop = asyncio.get_event_loop()
task = [play(movie_list), play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()

