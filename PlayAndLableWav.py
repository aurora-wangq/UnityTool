import os
import wave
import pyaudio
import shutil
def play_wav(filename):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(1024)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(1024)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("[INFO]Stream Closed!\n")

def getfile(path: str):
    fileName = os.listdir(path)
    fileDic = []
    for i in fileName:
        if (i[-1] == 'v' or i[-1] == 'V') and (i[-2] == 'a' or i[-2] == 'A') and (i[-3] == 'w' or i[-3] == 'W') and i[-4] == '.': 
            fileDic.append({"name":i,"path":path + '\\' + i})
    return fileDic
path = input("[INFO]Input files path:\n")
try:
    path = path.replace('"','')
except:
    input("[Error]at: path = path.replace() ")
try:
    wavs = getfile(path)
except:
    input("[Error]at: wavs = getfile(path) , your path is right?")
if len(wavs) <= 0:
    input("There is no wavs?")
for wav in wavs:
    try: 
        print(f"[INFO]Now Playing {wav['name']}\n")
        play_wav(wav["path"])
    except:
        input("Look like that there some files not with .wav")
    while 1:
        a = input("[INFO]Press 'N' to play next audio, Press 'T' to lable\n")
        if a == 'N' or a == 'n':
            break
        if a == 'T' or a == 't':
            b = input("[INFO]Input tag:\n")
            if not os.path.exists(path + '\\' + b):
                os.makedirs(path + '\\' + b)
            tagPath = path + '\\' + b + '\\' + wav['name']
            shutil.copy(wav['path'], tagPath)
            break
        else:
            print("[INFO]Please input 'N' or 'T'\n")
input("[INFO]Finished, Push any key to close")