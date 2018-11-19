import os
import time
import shutil
from sys import platform
if platform == "linux" or platform == "linux2":
    print(platform)
    import getpass
    usernameLinux = getpass.getuser()
    # linux
elif platform == "darwin":
    print(platform)
    import os
    homedir = os.environ['HOME']

    #do mac things
    # OS X
elif platform == "win32":
    # Windows
    print(platform)
    import getpass
    import fnmatch
    import platform
    usernameWin = getpass.getuser()
    desktop = os.path.expanduser("~\Desktop")
    chimeFolder = os.path.expanduser("~\Chime")
    os.chdir(desktop)
    currentTime = (time.strftime("%H-%M-%S"))
    currentDate = (time.strftime("%m_%d_%Y"))
    chimeDesktop = (desktop + '\\' + usernameWin + '_' + currentDate + '_' + currentTime)
    os.mkdir(chimeDesktop)
    # creates folder on Desktop with username, date, and time
    shutil.copy2(chimeFolder + "\\ChimePluginDebug.txt.0", chimeDesktop + "\\ChimePluginDebug.txt.0")
    # copies log file to Chime folder on Desktop
    f= open(chimeDesktop + "\\systemInfo.txt", "a+")
    f.write(platform.platform())

    f.write()
