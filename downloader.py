from pytubefix import YouTube
import os

def ensure_dirs():
    os.makedirs('./audios', exist_ok=True)
    os.makedirs('./videos', exist_ok=True)

def verify(url):
    try:
        yt = YouTube(url)
        print(yt.title)
    except Exception as e:
        print(f"Erro ao acessar o vídeo: {e}")
        main()
    while True:
        confirm = input('[y/n]: ').lower().strip()
        if (confirm == 'y'):
            return download_video(yt)
        elif (confirm == 'n'):
            return main()

def download_video(yt):

    while True:
        formato = input('Formato de output (mp3/mp4): ').lower().strip()
        
        ensure_dirs()
        if (formato == 'mp3'):
            audio = yt.streams.get_audio_only()
            audio.download('./audios')
            break
        elif (formato == 'mp4'):
            video = yt.streams.get_highest_resolution()
            video.download('./videos')
            break
        else:
            print("Formato inválido. Digite novamente.")
            continue

def main():
    video = input('Digite a url do video: ')
    verify(video)
    print('Baixado com sucesso!')
if (__name__ == "__main__"):
    main()
