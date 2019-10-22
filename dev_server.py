import os
os.environ['dev'] = '1'
from dash_mess import dev_server
server = app.server

if __name__ == '__main__':
    dev_server(debug=True)