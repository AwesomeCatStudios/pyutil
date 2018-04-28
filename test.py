print("LAUCHED pyutil tester")
import pyutil
try:
    pyutil.core.core.web("","http://google.com")
except Exception as e:
    print("FAILED "+str(e))
