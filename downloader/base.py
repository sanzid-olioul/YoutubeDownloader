from pytube import Playlist,YouTube
import concurrent.futures
class SingleVidio:
    _download_path = 'Download'
    _compleated = 0
    def __init__(self,url) -> None:
        self.url = url
        self.location = SingleVidio._download_path
    def percent(self, tem, total):
        perc = round(float(tem) / float(total) * float(100),2)
        return perc
    def progress_function(self,stream,chalk ,bytes_remaining):        
        size = stream.filesize
        print(stream.title,self.percent(size-bytes_remaining,size))
       

    def download(self,counter):
        
        video = YouTube(self.url,on_progress_callback=self.progress_function).\
            streams.filter(type='video', progressive=True, file_extension='mp4')\
            .order_by('resolution').desc().first()
        print(self.location)
        video.download(output_path=self.location,filename_prefix=str(counter)+' . ')
    

    @classmethod
    def set_download_path(cls,path_):
        cls._download_path = path_

class VideoPlayList:
    _total_video = 0
    
    def __init__(self,url) -> None:
        self.url = url
        print(url)
        self.lists = Playlist(self.url)
        VideoPlayList._total_video = len(self.lists.videos)
    def download_all(self):
        links = [url.watch_url for url in self.lists.videos]
        vidios = [SingleVidio(link) for link in links]
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