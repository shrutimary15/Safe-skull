from flask import Flask,request,render_template
import os

from src.pipeline.predict_pipeline import PredictPipeline
application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_helmet():
    if request.method=='GET':
        print('Page Rendered')
        return render_template('home.html')
    else:
                print('Image Request Made')
                image=request.files['file']
                print(type(image))
                os.makedirs('Uploads',exist_ok=True)
                image_path=os.path.join('Uploads','Data.png')
                image.save(image_path)

                PredictPipeline.predict_pipeline(image_path)

                print('Image received')
                return 'Image uploaded successfully!'
            
        
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)  