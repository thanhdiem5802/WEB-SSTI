import random
from flask import Flask, render_template_string, render_template, request
import os
os.system("whoami")
os.system("ls")
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Follow your dream'
nicknames = ['%s']

    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            p = request.values.get('nickname')
            if p != None:
                if 'VNPT' in p:
                    return 'ước lại đi'
            if 'FSORF' in p:
                    return 'congratulation' 

            id = random.randint(0, len(nicknames) - 1)
            
            return render_template_string(nicknames[id] % p)

        except Exception as e:
            print(e)
            return 'Exception'
			
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
