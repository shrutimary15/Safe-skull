from flask import Flask, request, render_template
import os

import inflect

from src.pipeline.predict_pipeline import PredictPipeline
application = Flask(__name__)

app = application

# Route for a detectHelmet page


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_helmet():
    if request.method == 'GET':
        print('Page Rendered')
        return render_template('detectHelmet.html')
    else:
        print('Image Request Made')
        image = request.files['file']
        print(type(image))
        os.makedirs('Uploads', exist_ok=True)
        image_path = os.path.join('Uploads', 'Data.png')
        image.save(image_path)

        result_img_path,noHelmetValue=PredictPipeline.predict_pipeline(image_path=image_path)
        num_text_engine=inflect.engine()
        noHelmetValue=num_text_engine.number_to_words(noHelmetValue)

        print('Image received')
        return render_template('results.html', image_path=result_img_path,nohelmet_value=noHelmetValue)

@app.route('/results')
def resultspage():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
