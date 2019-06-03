import warnings
warnings.filterwarnings("ignore")

from flask import Flask, redirect, url_for, request,render_template
import res_exp as restest
app = Flask(__name__)



@app.route('/')
def index():
   return render_template('simple_chat.html')
   
@app.route('/success/<name>')
def success(name):
   return 'here is your most matching answer :        %s' % name
   
   
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
	  #print(user)
      resuser = restest.response(user)
      return resuser; #redirect(url_for('success',name = resuser))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
	  
@app.route('/spell',methods = ['POST', 'GET'])
def spell():
   if request.method == 'POST':
      user = request.form['nm']
	  #print(user)
      resuser = 'test'
      return resuser; #redirect(url_for('success',name = resuser))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run('0.0.0.0',8084)