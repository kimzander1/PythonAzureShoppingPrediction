# ipython_config.py

c = get_config()

# Allow all IP addresses to use the service and run it on port 80.

c.NotebookApp.ip = '127.0.0.1'
c.NotebookApp.port = 80

# Don't load the browser on startup.
c.NotebookApp.open_browser = True

