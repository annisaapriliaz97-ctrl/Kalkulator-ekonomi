from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Mengambil data dari input user
        marketing_cost = float(request.form.get('cost', 0))
        new_customers = float(request.form.get('customers', 0))
        avg_purchase = float(request.form.get('purchase', 0))
        retention_rate = float(request.form.get('retention', 0)) / 100

        # Rumus Ekonomi Digital Sederhana
        # 1. CAC (Customer Acquisition Cost)
        cac = marketing_cost / new_customers if new_customers > 0 else 0
        
        # 2. LTV (Lifetime Value) - Rumus simpel: Rata-rata belanja / (1 - retention rate)
        ltv = avg_purchase / (1 - retention_rate) if retention_rate < 1 else avg_purchase
        
        # 3. Rasio LTV/CAC (Idealnya > 3x dalam startup)
        ratio = ltv / cac if cac > 0 else 0

        return render_template('index.html', 
                               cac=round(cac, 2), 
                               ltv=round(ltv, 2), 
                               ratio=round(ratio, 2),
                               submitted=True)
    except Exception as e:
        return "Terjadi kesalahan input: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
