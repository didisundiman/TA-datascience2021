from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('modelRFR.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    #return render_template('index.html', insurance_cost=0)
    return render_template('index.html', kinerja_umkm=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    #age, sex, smoker = [x for x in request.form.values()]
    kpl_value, tph_value, am_value = [x for x in request.form.values()]

    data = []

    # data.append(int(age))
    # if sex == 'Laki-laki':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if smoker == 'Ya':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    data.append(int(kpl_value))
        data.extend(int(tph_value))
        data.extend(int(am_value))

    prediction = model.predict([data])
    output = round(prediction[0], 2)

    #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)
    return render_template('index.html', kinerja_umkm=output, kpl_value=kpl_value, tph_value=tph_value, am_value=am_value)


if __name__ == '__main__':
    app.run(debug=True)