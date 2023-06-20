from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def homepage(): 
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_price(): 
    if request.method == 'GET': 
        print('get')
        return render_template('index.html')

    else : 
        data = CustomData(
            CRIM = float(request.form.get("CRIM")), 
            ZN = float(request.form.get("ZN")), 
            INDUS = float(request.form.get("INDUS")), 
            CHAS = float(request.form.get("CHAS")), 
            NOX = float(request.form.get("NOX")), 
            RM = float(request.form.get("RM")), 
            AGE = float(request.form.get("AGE")), 
            DIS = float(request.form.get("DIS")), 
            #RAD = float(request.form.get('RAD')), 
            #TAX = float(request.form.get('TAX)), 
            PTRATIO = float(request.form.get("PTRATIO")), 
            B = float(request.form.get("B")), 
            LSTAT = float(request.form.get("LSTAT"))
        )


        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        results = round(pred[0], 2)
        return render_template('index.html', final_results = results)



if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True)