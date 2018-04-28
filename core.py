print("loaded core")
helpmsg='''
pyutil core
Methods
help()-show help
web(url)-open web browser
'''
import webbrowser
class core:
    def help(self):
        print(helpmsg)
    def web(self,url):
        webbrowser.open(url)
