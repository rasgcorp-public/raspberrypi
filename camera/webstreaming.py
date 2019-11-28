import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

PAGE = """\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""


class StreamingOutput(object)
 def __init__(self):
    self.frame = None
    self.buffer = io.BytesIO()
    self.condition = Condition()

  def write(self, buf):
    if buf.startswith(b'\xff\xd8'):
      self.buffer.truncate()
      with self.condition:
        self.frame = self.buffer.getValue()
        self.condition.notify_all()
      self.buffer.seek(0)
    return self.buffer.write(buf)

#class StreamingHandler

