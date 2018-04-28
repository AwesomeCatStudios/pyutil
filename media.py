#Media.py
#Play media
try:
    import pafy
except:
    pafy="disabled"
#
#
def fetch(url):
    obj=pafy.new(url)
    a=obj.audiostreams
    print("Download")
    a[2].download(filepath="c:\\Data\\")
    





    from subprocess import Popen, PIPE

    pipes = dict(stdin=PIPE, stdout=PIPE, stderr=PIPE)
    mplayer = Popen(["mplayer", "c:\\Data\\"+obj.title+".m4a"], **pipes)

    # to control u can use Popen.communicate
    mplayer.communicate(input=b">")
    sys.stdout.flush()
