# ipython_config.py

c = get_config()

# Allow all IP addresses to use the service and run it on port 80.
<<<<<<< HEAD
c.NotebookApp.ip = '127.0.0.1'
c.NotebookApp.port = 80

# Don't load the browser on startup.
c.NotebookApp.open_browser = False
=======
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 80

# Don't load the browser on startup.
c.NotebookApp.open_browser = True
>>>>>>> a5b362d47769b6b8fa18cad07b6b8b221adf3854
