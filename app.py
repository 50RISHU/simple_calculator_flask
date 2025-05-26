from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    result = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        op = request.form.get('operator')

        if op == 'add':
            result = num1 + num2
        elif op == 'sub':
            result = num1 - num2
        elif op == 'mul':
            result = num1 * num2
        elif op == 'div':
            result = num1 / num2
        else:
            result = "Somthing Went Wrong!"    

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True) 