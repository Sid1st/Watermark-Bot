# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 28908582))
	API_HASH = os.environ.get("API_HASH", "0d79d297bb8f56caed2c8f08bfc17289")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002219645512"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002151777689")
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 5052476013))
	CAPTION = "By @MoviesXonee"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Watermark_Bot")
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://subhamgupta992sg:UXRT66yXTlP7MTJt@cluster0.bza4jw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/MoviesXonee).__

Desgined by @MoviesXonee
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
