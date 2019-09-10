# 类的方式去完成
# 多进程 multiprocession去完成

import threading
import time
import multiprocessing

movie_list = ["斗破苍穹.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "大话西游.mp4"]
music_list = ['周杰伦.mp3', '五月天.mp3']
movie_format = ["mp4", "avi"]
music_format = ["mp3"]


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("正在播放的电影是: %s" % i)
            time.sleep(5)
        elif i.split(".")[1] in music_format:
            print("正在收听的音乐是：%s" % i)
            time.sleep(3)
        else:
            print("当前没有可播放的格式")

# 定义类
class LlrThread(threading.Thread):

    def __init__(self, ps):
        super().__init__()
        self.ps = ps

    def run(self):
        play(self.ps)

# 类方法主线程如下：
# if __name__ == '__main__':
#     L1 = LlrThread(movie_list)
#     L2 = LlrThread(music_list)
#     L1.start()
#     L2.start()

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=play, args=(movie_list, ))
    t2 = multiprocessing.Process(target=play, args=(music_list, ))

    t1.start()
    t2.start()

