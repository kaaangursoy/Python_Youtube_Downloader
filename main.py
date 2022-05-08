from time import sleep
from pytube import YouTube
from pytube.cli import on_progress
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
import tempfile


yt = YouTube(input("Url giriniz: "), on_progress_callback=on_progress)
os.system('cls||clear')
print('\n', "Başlık: ", yt.title, '\n',
      "---------------------------------------------", '\n',
      "Açıklama: ", yt.description[:75], '\n',
      "---------------------------------------------", '\n',
      "İzlenme sayısı: ", yt.views, '\n',
      "---------------------------------------------", '\n',
      "Anahtar Kelimeler :", yt.keywords[:75], '\n',
      )
onay = input("Bu videoyu indirmek istediğine emin misin? (Y/N): ").upper()
while onay == "":
    onay = input("Bu videoyu indirmek istediğine emin misin? (Y/N): ").upper()
else:
    while True:
        if onay == "Y":
            os.system('cls||clear')
            print("Çözünürlükler: ")
            for i in yt.streams.filter(adaptive=True, mime_type="video/webm"):
                if i.resolution != None:
                    print(str(i.resolution))
                else:
                    pass
            reso = None
            print("Çözünürlük seçin: ")
            reso = input()
            if "p" in reso:
                pass
            elif "P" in reso:
                reso.lower()
                continue
            else:
                reso = reso + "p"
            print("Ses Kaliteleri:")
            for i in yt.streams.filter(adaptive=True, mime_type='audio/webm'):
                if i.abr != None:
                    print(str(i.abr))
                else:
                    pass
            kbps = None
            print("Ses kalitesi seçin:")
            kbps = input()
            if "kbps" in kbps:
                pass
            elif "KBPS" in kbps or "KBps" in kbps or "KBPs" in kbps:
                kbps.lower()
                continue
            else:
                kbps = kbps + "kbps"
            print("Ses Kaliteleri:")
            for i in yt.streams.filter(adaptive=True, mime_type='audio/webm'):
                if i.abr != None:
                    print(str(i.abr))
                else:
                    pass
            os.system('cls||clear')
            print(f' çözünürlük : {reso}', '\n', f'Ses Kalitesi: {kbps}')
            isim = input("Kayıt edilecek dosyanın ismini giriniz: ")
            with tempfile.TemporaryDirectory() as tempdirname:
                yt.streams.filter(
                    res=reso, mime_type='video/webm').first().download(filename="video.webm", output_path=f"{tempdirname}")
                yt.streams.filter(
                    abr=kbps, mime_type='audio/webm').first().download(filename="audio.webm", output_path=f"{tempdirname}")
                videoclip = VideoFileClip(f"{tempdirname}/video.webm")
                audioclip = AudioFileClip(f"{tempdirname}/audio.webm")
                new_audioclip = CompositeAudioClip([audioclip])
                videoclip.audio = new_audioclip
                videoclip.write_videofile(f"{isim}"+".mp4")
            break
        elif onay == "N":
            print("Güle Güle")
            break
        else:
            onay = input("Hatalı bir tuşa bastınız: ").upper()
