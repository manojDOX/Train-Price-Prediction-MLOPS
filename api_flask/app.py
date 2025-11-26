from flask import Flask
from flask import request, jsonify
app = Flask(__name__)
import os
from joblib import load, dump
from predict_operation import predict_price




@app.route('/',methods=['GET','POST'])
def predict():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Train Ticket Price Prediction</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #141e30, #243b55);
        }

        .container {
            background: #ffffff;
            width: 100%;
            max-width: 650px;
            padding: 24px 28px 30px;
            border-radius: 18px;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.25);
        }

        h2 {
            margin: 0 0 4px;
            font-size: 24px;
            text-align: center;
            color: #111827;
        }

        .subtitle {
            margin: 0 0 18px;
            font-size: 13px;
            text-align: center;
            color: #6b7280;
        }

        form {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px 18px;
        }

        .full-width {
            grid-column: 1 / 3;
        }

        label {
            display: block;
            margin-bottom: 4px;
            font-size: 13px;
            font-weight: 600;
            color: #374151;
        }

        input[type="datetime-local"],
        input[type="number"],
        select {
            width: 100%;
            padding: 8px 10px;
            border-radius: 8px;
            border: 1px solid #d1d5db;
            font-size: 13px;
            outline: none;
            transition: border 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
            background: #f9fafb;
        }

        input[type="datetime-local"]:focus,
        input[type="number"]:focus,
        select:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.18);
            background: #ffffff;
        }

        input[type="number"]::-webkit-outer-spin-button,
        input[type="number"]::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }

        input[type="number"] {
            -moz-appearance: textfield;
        }

        .hint {
            margin-top: 2px;
            font-size: 11px;
            color: #9ca3af;
        }

        .button-row {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-top: 6px;
        }

        input[type="submit"],
        .secondary-btn {
            border: none;
            border-radius: 999px;
            padding: 9px 18px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.12s ease, box-shadow 0.12s ease, background 0.12s ease, color 0.12s ease;
        }

        .secondary-btn {
            background: #e5e7eb;
            color: #374151;
        }

        .secondary-btn:hover {
            background: #d1d5db;
            transform: translateY(-1px);
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12);
        }

        input[type="submit"] {
            background: #2563eb;
            color: white;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.45);
        }

        input[type="submit"]:hover {
            background: #1d4ed8;
            transform: translateY(-1px);
            box-shadow: 0 10px 24px rgba(37, 99, 235, 0.55);
        }

        input[type="submit"]:active,
        .secondary-btn:active {
            transform: translateY(0);
            box-shadow: none;
        }

        @media (max-width: 640px) {
            body {
                padding: 16px;
                align-items: flex-start;
            }

            .container {
                margin-top: 26px;
                padding: 18px 16px 22px;
            }

            form {
                grid-template-columns: 1fr;
            }

            .full-width {
                grid-column: 1 / 2;
            }

            .button-row {
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Train Ticket Price Prediction</h2>
        <p class="subtitle">Fill the journey details below and get an estimated ticket price.</p>

        <form action="/predict" method="POST">
            <!-- Booking date & time -->
            <div class="full-width">
                <label for="insert_date">Booking Date & Time (insert_date)</label>
                <input type="datetime-local" id="insert_date" name="insert_date" required>
                <div class="hint">Auto-filled with current date & time – you can adjust if needed.</div>
            </div>

            <!-- Origin -->
            <div>
                <label for="origin">Origin</label>
                <select id="origin" name="origin" required>
                    <option value="">Select origin</option>
                    <option value="PONFERRADA">PONFERRADA</option>
                    <option value="MADRID">MADRID</option>
                    <option value="SEVILLA">SEVILLA</option>
                    <option value="VALENCIA">VALENCIA</option>
                    <option value="BARCELONA">BARCELONA</option>
                </select>
            </div>

            <!-- Destination -->
            <div>
                <label for="destination">Destination</label>
                <select id="destination" name="destination" required>
                    <option value="">Select destination</option>
                    <option value="MADRID">MADRID</option>
                    <option value="VALENCIA">VALENCIA</option>
                    <option value="BARCELONA">BARCELONA</option>
                    <option value="PONFERRADA">PONFERRADA</option>
                    <option value="SEVILLA">SEVILLA</option>
                </select>
            </div>

            <!-- Train departure -->
            <div>
                <label for="start_date">Departure (start_date)</label>
                <input type="datetime-local" id="start_date" name="start_date" required>
                <div class="hint">Select the train’s departure date & time.</div>
            </div>

            <!-- Train arrival -->
            <div>
                <label for="end_date">Arrival (end_date)</label>
                <input type="datetime-local" id="end_date" name="end_date" required>
                <div class="hint">Select the train’s arrival date & time.</div>
            </div>

            <!-- Train type -->
            <div class="full-width">
                <label for="train_type">Train Type</label>
                <select id="train_type" name="train_type" required>
                    <option value="">Select train type</option>
                    <option value="MD-AVE">MD-AVE</option>
                    <option value="MD-LD">MD-LD</option>
                    <option value="ALVIA">ALVIA</option>
                    <option value="REGIONAL">REGIONAL</option>
                    <option value="AVE">AVE</option>
                    <option value="INTERCITY">INTERCITY</option>
                    <option value="AVE-MD">AVE-MD</option>
                    <option value="AVE-LD">AVE-LD</option>
                    <option value="R. EXPRES">R. EXPRES</option>
                    <option value="AVE-TGV">AVE-TGV</option>
                    <option value="AV City">AV City</option>
                    <option value="MD">MD</option>
                    <option value="LD-MD">LD-MD</option>
                    <option value="LD">LD</option>
                    <option value="LD-AVE">LD-AVE</option>
                    <option value="TRENHOTEL">TRENHOTEL</option>
                </select>
            </div>

            <!-- Train class -->
            <div>
                <label for="train_class">Train Class</label>
                <select id="train_class" name="train_class" required>
                    <option value="">Select class</option>
                    <option value="Turista">Turista</option>
                    <option value="Preferente">Preferente</option>
                    <option value="Turista Plus">Turista Plus</option>
                    <option value="Turista con enlace">Turista con enlace</option>
                    <option value="Cama Turista">Cama Turista</option>
                </select>
            </div>

            <!-- Fare -->
            <div class="full-width">
                <label for="fare">Fare Type</label>
                <select id="fare" name="fare" required>
                    <option value="">Select fare</option>
                    <option value="Promo">Promo</option>
                    <option value="Adulto ida">Adulto ida</option>
                    <option value="Flexible">Flexible</option>
                    <option value="Promo +">Promo +</option>
                    <option value="Mesa">Mesa</option>
                </select>
            </div>

            <!-- Buttons -->
            <div class="full-width button-row">
                <button type="reset" class="secondary-btn">Clear</button>
                <input type="submit" value="Predict">
            </div>
        </form>
    </div>

    <script>
        // Auto-fill insert_date with current local date & time
        (function () {
            const now = new Date();
            const tzOffsetMs = now.getTimezoneOffset() * 60000;
            const localISOTime = new Date(now.getTime() - tzOffsetMs)
                                    .toISOString()
                                    .slice(0, 16); // "YYYY-MM-DDTHH:MM"
            const insertDateInput = document.getElementById('insert_date');
            if (insertDateInput) {
                insertDateInput.value = localISOTime;
            }
        })();
    </script>
</body>
</html>
"""

@app.route('/predict', methods=['POST'])
def index():
    if request.method == 'POST':

        # ----- Get input data from the form -----
        insert_date = request.form.get('insert_date')
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        train_type = request.form.get('train_type')
        # price = float(request.form.get('price'))
        train_class = request.form.get('train_class')
        fare = request.form.get('fare')

        # ----- Prepare data dictionary (to pass into model/pipeline) -----
        data = {
            'insert_date': insert_date,
            'origin': origin,
            'destination': destination,
            'start_date': start_date,
            'end_date': end_date,
            'train_type': train_type,
            'train_class': train_class,
            'fare': fare
        }

        # ----- Load model and preprocessing objects -----
        model_path = os.path.join(os.path.dirname(__file__),'..', 'artifacts', 'models', 'lgbm_regressor_hyper_model.joblib')
        label_encoders_path = os.path.join(os.path.dirname(__file__),'..', 'artifacts', 'transformers', 'label_encoders.joblib')
        
        loaded_model = load(model_path)
        loaded_encoders = load(label_encoders_path)

        # ----- Call your model inference logic -----
        try:
            # Predict ticket price using model
            prediction = predict_price(data, loaded_model, loaded_encoders)

            return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Prediction Result</title>
                <style>
                    * {{
                        box-sizing: border-box;
                        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                    }}

                    body {{
                        margin: 0;
                        padding: 0;
                        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                        min-height: 100vh;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        color: white;
                    }}

                    .result-container {{
                        background: rgba(255, 255, 255, 0.1);
                        padding: 32px 40px;
                        border-radius: 18px;
                        backdrop-filter: blur(10px);
                        box-shadow: 0 18px 40px rgba(0, 0, 0, 0.25);
                        text-align: center;
                        max-width: 480px;
                        width: 90%;
                    }}

                    h2 {{
                        margin: 0 0 6px;
                        font-size: 26px;
                        font-weight: 600;
                    }}

                    h3 {{
                        margin: 18px 0 20px;
                        font-size: 38px;
                        font-weight: 700;
                        color: #ffdd57;
                    }}

                    .btn {{
                        display: inline-block;
                        padding: 10px 22px;
                        margin-top: 4px;
                        background: #2563eb;
                        color: white;
                        border-radius: 12px;
                        font-weight: 600;
                        font-size: 14px;
                        text-decoration: none;
                        transition: 0.2s;
                    }}

                    .btn:hover {{
                        background: #1d4ed8;
                        transform: translateY(-2px);
                        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.55);
                    }}
                </style>
            </head>
            <body>
                <div class="result-container">
                    <h2>Predicted Ticket Price</h2>
                    <h3>{prediction:.2f} €</h3>
                    <a href="/" class="btn">🔙 Predict Another Fare</a>
                </div>
            </body>
            </html>
            """


            # return jsonify({
            #     'status': 'success',
            #     'prediction': float(prediction)
            # })

        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            })

if __name__ == "__main__":
    # debug=True so you can see errors in the terminal
    app.run(host="0.0.0.0", port=5000, debug=True)
