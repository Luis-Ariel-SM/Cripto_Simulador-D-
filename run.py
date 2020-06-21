from flask import Flask


app = Flask(__name__)

@app.route('/')
def Tabla_movimientos ():
    return 'Hello Flask es la p'
    

if __name__ == '__main__':
    app.run()