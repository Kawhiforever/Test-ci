from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello(): 
    return "Deployed to Rocky Linux 9.7 via CI/CD Pipeline!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
