from flask import Flask # type: ignore
from calculator import SimpleCalculator

app = Flask(__name__)
calc = SimpleCalculator()

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Простой калькулятор</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            .container { max-width: 400px; margin: 0 auto; }
            .form-group { margin-bottom: 15px; }
            input, select { padding: 8px; width: 100px; margin: 0 5px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
            .result { margin-top: 20px; padding: 15px; background: #f8f9fa; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Простой калькулятор</h1>
            <div class="form-group">
                <input type="number" id="num1" value="10">
                <select id="operation">
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">×</option>
                    <option value="/">÷</option>
                    <option value="**">^</option>
                </select>
                <input type="number" id="num2" value="5">
            </div>
            <button onclick="calculate()">Посчитать</button>
            <div id="result" class="result" style="display: none;"></div>
        </div>

        <script>
            function calculate() {
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const operation = document.getElementById('operation').value;
                
                let result;
                switch(operation) {
                    case '+': result = num1 + num2; break;
                    case '-': result = num1 - num2; break;
                    case '*': result = num1 * num2; break;
                    case '/': 
                        if (num2 === 0) {
                            result = "Ошибка: на ноль делить нельзя!";
                        } else {
                            result = num1 / num2;
                        }
                        break;
                    case '**': result = Math.pow(num1, num2); break;
                }
                
                document.getElementById('result').innerHTML = `
                    <h3>Результат:</h3>
                    <p>${num1} ${operation} ${num2} = <strong>${result}</strong></p>
                `;
                document.getElementById('result').style.display = 'block';
            }
        </script>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)