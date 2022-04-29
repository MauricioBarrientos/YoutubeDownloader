import youtube_dl


def run():
    video_url = input("ingresa la url del video: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False)
    filename = f"{video_info['title']}.mp3"
    option = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with youtube_dl.YoutubeDL(option) as ydl:
        ydl.download([video_info['webpage_url']])

    print("descarga completa... ---> {}".format(filename))


if __name__ == '__main__':
    run()