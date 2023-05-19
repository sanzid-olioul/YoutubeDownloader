from pytube import Playlist,YouTube
import concurrent.futures
class SingleVidio:
    _download_path = 'Downloads'
    _compleated = 0
    available = [4,3,2,1]
    blocked = dict()
    def __init__(self,url,download_obj,completed_obj) -> None:
        self.url = url
        self.location = SingleVidio._download_path
        self.download_obj = download_obj
        self.completed_obj = completed_obj
        self.is_called = False

    def percent(self, tem, total):
        perc = round(float(tem) / float(total) * float(100),2)
        return perc
    
    def progress_function(self,stream,chalk ,bytes_remaining):        
        size = stream.filesize
        if not self.is_called:
            self.col= SingleVidio.available.pop()
            SingleVidio.blocked[stream.title] = self.col
            self.is_called = True
        self.download_obj.add_prgoress(self.col,stream.title,self.percent(size - bytes_remaining,size))

    def complete_function(self,stream,chalk):
        SingleVidio.available.append(self.blocked.get(stream.title))
        self.completed_obj.addNewLabel(stream.title)


    def download(self,counter):
        self.counter = counter
        video = YouTube(self.url,on_progress_callback=self.progress_function,on_complete_callback=self.complete_function).\
            streams.filter(type='video', progressive=True, file_extension='mp4')\
            .order_by('resolution').desc().first()
        print(SingleVidio._download_path)
        video.download(output_path=SingleVidio._download_path,filename_prefix=str(counter)+' . ')
        SingleVidio._compleated+=1
    

    @classmethod
    def set_download_path(cls,path_):
        cls._download_path = path_

class VideoPlayList:
    _total_video = 0
    
    def __init__(self,url,download_obj,completed_obj) -> None:
        self.url = url
        self.lists = Playlist(self.url)
        self.download_obj = download_obj
        self.completed_obj = completed_obj
        VideoPlayList._total_video = len(self.lists.videos)
    def download_all(self):
        links = [url.watch_url for url in self.lists.videos]
        vidios = [SingleVidio(link,self.download_obj,self.completed_obj) for link in links]
        with concurrent.futures.ThreadPoolExecutor(4) as executor:
            results = []
            for i,vidio in enumerate(vidios):
                try:
                    res = executor.submit(vidio.download,i+1)
                    results.append(res)
                except Exception as e:
                    print(e)
            for result in results:
                result.result()


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=0yVDMcGp97g&list=PLjVLYmrlmjGfh2rwJjrmKNHzGxCZwBsqj&ab_channel=WsCubeTech"
    SingleVidio.download_path('sanzid/')
    video = VideoPlayList(url)
    video.download_all()