from pytubefix import YouTube


def verify(url):
    yt = YouTube(url)
    print(yt.title)
    while True:
        confirm = input('[y/n]: ').lower().strip()
        if (confirm == 'y'):
            return download_video(yt)
        elif (confirm == 'n'):
            return main()

def download_video(yt):

    while True:
        formato = input('Formato de output (mp3/mp4): ').lower().strip()

        if (formato == 'mp3'):
            audio = yt.streams.get_audio_only()
            audio.download('./audios')
            break
        elif (formato == 'mp4'):
            video = yt.streams.get_highest_resolution()
            video.download('./videos')
            break

def main():
    video = input('Digite a url do video: ')
    verify(video)
    print('Baixado com sucesso!')

main()
