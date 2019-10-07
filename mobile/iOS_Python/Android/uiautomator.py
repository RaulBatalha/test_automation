from uiautomator2 as device
import time
startApp = time.time()
connectDevic = device'('192.0.0.1')
    def setUp()
     start_activity = "adb shell am start - "

     am start -a android.intent.action.MAIN -n com.android.browser/.BrowserActivity
