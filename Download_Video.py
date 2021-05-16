from pytube import YouTube
SAVE_PATH = "E:/Down"  # to_do

def download_audio(link):
    yt=YouTube(link)
    try:
       stream=yt.streams.last()
       stream.download(SAVE_PATH)
    except:
        print("Audio could not be downloaded .Please try again")
    else:
        print("Audio is sucessfully downloaded")





def download_video(link):
    yt = YouTube(link)
    try:
       #streams give a Stream Query object after running yt.streams().And with this object we can perform different operations
       #first() will retuen the highest quality stream avaialbe for a given video
       #last() will return the audio stream becaus that is of lowest quality which is availbe
       stream=yt.streams.first()
       stream.download(SAVE_PATH)
    except:
        print("Video could not be downloaded due to some error.Please Try again")
    else:
        print("Your video is downloaded sucessfully")




link = str(input("Enter the link of YouTube video You wish to download"))
choice=str(input("Do You want a audio verison or a video to be download?\
                 Press A for Audio and\
                 Press V for Video "))
if (choice =='A' or  choice =='a'):
    download_audio(link)
elif (choice == 'V' or choice == 'v'):
    download_video(link)
else:
    print("Please enter option either 'A' or 'V'")
