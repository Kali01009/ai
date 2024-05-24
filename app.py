from flask import Flask, render_template, request
import pandas as pd
# Import other required libraries

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        revenue_category_input = request.form['revenue_category']
        year_input = int(request.form['year'])
        
        # Your existing code to make predictions goes here
        # ...

        return render_template('result.html', predicted_value=inverse_scaled_value[0][0], accuracy=accuracy)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)