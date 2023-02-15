c.NotebookApp.certfile = '/tmp/certs/mycert.pem'
c.NotebookApp.keyfile = '/tmp/certs/mykey.key'

c.NotebookApp.password  = 'ECRYPTED_PASSWORD'

c.NotebookApp.open_browser = False

c.NotebookApp.notebook_dir = '/home/jovyan/src/notebooks'
c.NotebookApp.port = 1443
c.NotebookApp.allow_remote_access = True
c.ServerApp.allow_root = True
c.NotebookApp.ip = '0.0.0.0'
