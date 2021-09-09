# The lines up to and including sys.stderr should always come first
# Then any errors that occur later get reported to the console
# If you'd prefer to report errors to a file, you can do that instead here.
import sys
from Npp import *

# Set the stderr to the normal console as early as possible, in case of early errors
sys.stderr = console

# Define a class for writing to the console in red
class ConsoleError:
	def __init__(self):
		global console
		self._console = console;

	def write(self, text):
		self._console.writeError(text);

# Set the stderr to write errors in red
sys.stderr = ConsoleError()

# This imports the "normal" functions, including "help"
import site

sys.stdout = console

# In order to set the stdout to the current active document, uncomment the following line
# sys.stdout = editor
# So print "hello world", will insert "hello world" at the current cursor position


#import ctypes
#MessageBox = ctypes.windll.user32.MessageBoxW
#MessageBox(None, 'print Message', 'Pay Attention', 0)

#-------------------------------------->option1
def callback_BUFFERACTIVATED(args):
    if '.yx' in notepad.getBufferFilename(args['bufferID']):
        notepad.runMenuCommand('Language','Yoix')
	if '.jack' in notepad.getBufferFilename(args['bufferID']):
		notepad.runMenuCommand('Language','Jack')

notepad.clearCallbacks([NOTIFICATION.BUFFERACTIVATED ])
notepad.callback(callback_BUFFERACTIVATED, [NOTIFICATION.BUFFERACTIVATED ])

#-------------------------------------->option2

#
# from fnmatch import fnmatch
#
# def callback_BUFFERACTIVATED(args):
# 	_file = notepad.getBufferFilename(args['bufferID'])
# # if fnmatch(_file, '*\Notepad++\plugins\Con*\Python*\*\*.py'):
# 	if fnmatch(_file, r'*\Notepad++\plugins\PythonScript\scripts\*.py'):
# 		current_bufferID = str(args['bufferID'])
# 		if editor.getProperty(current_bufferID) != '1':
# 			editor.setProperty(current_bufferID, '1')
# 			notepad.runMenuCommand('Language','Yoix')
#
# notepad.clearCallbacks([NOTIFICATION.BUFFERACTIVATED ])
# notepad.callback(callback_BUFFERACTIVATED, [NOTIFICATION.BUFFERACTIVATED ])