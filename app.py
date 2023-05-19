from flask import Flask,request,render_template


application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_helmet():
    if request.method=='GET':
        return render_template('home.html')
    else:
        if 'file' in request.files:
            image=request.files['file']
            return 'Image uploaded successfully!'
        else:
            return 'Image did not upload'
        
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)  