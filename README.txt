------------------------------Youtube Video/Audio Downloader(automation script)---------------------------------------------------

A)Purpose of this app:
-Afew years back ago,I remember I used to install YTDownloader to download songs from youtube.
-So now,I wanted to know I thought of integrating on my own.
-Thus the idea popped up to build a youtube dowloader automation app.
-It will download the Video or audio depending upon the user's choice.

B)Python Module used in this:

-I have used 'pytube'  module for this automation.It doesnot comes built-in.we can need to download it.
-The main class used from pytube module is 'YouTube' class.
-pytube is a very serious, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube Videos.
-Various methods of these classes can be used using this module.



C)Working/internal implementation of this application:
-The 'pytube' module is first installed in the project using Settings/Interpreter/pip option or
 pip install pytube

-After installing the module,we need to import 'YouTube' class which is used for downloading Youtube videos

-Here the user needs to enter the URL of the video one wishes to download.

-Along with the URL,the script will ask for choice-Audio or Video.

-According to the choice,the respective method,download_video(link) or download_audio(link) is  called .



C)notification() method:

-notification() method has few parameters:
 notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False)

toast (bool) – simple Android message instead of full notification

D)Issue faced while developing this mini project:

-Issue 1
  while checking for the choice entered ,when I used identity operator to compare the choice and required i.p,I was
  getting a syntax warning "do u mean == or !="
  After google search,I came to know that from Python 3.8,identity operator(is and is not) is for comparing whether two objects
  are same or not and == is for equality comparison.


E)Exception where it would fail:

-Where the URL is incorrect.Still not added any eexception to deal with such cases.


Note-For more details:
    https://www.studytonight.com/post/pytube-to-download-youtube-videos-with-python

