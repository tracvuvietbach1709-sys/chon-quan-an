from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# -------------------------------------------------------------
# TRANG 1: Hello bà nha !!
# -------------------------------------------------------------
PAGE_1_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Bà Nha</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            height: 100vh; display: flex; justify-content: center; align-items: center;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #feada6 100%);
            font-family: 'Playfair Display', serif; cursor: pointer; user-select: none;
            overflow: hidden; position: relative; transition: opacity 0.7s ease;
        }
        .flower {
            position: absolute; bottom: -60px; font-size: 22px;
            animation: floatUp 8s linear infinite; pointer-events: none; opacity: 0.7;
        }
        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); opacity: 0.8; }
            50% { opacity: 0.5; }
            100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
        }
        .card {
            background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px);
            padding: 55px 75px; border-radius: 35px;
            box-shadow: 0 20px 50px rgba(255, 154, 158, 0.3), inset 0 0 20px rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.7); text-align: center;
            animation: floatCard 4.5s ease-in-out infinite; z-index: 10; max-width: 90%;
        }
        h1 { color: #d63384; font-family: 'Dancing Script', cursive; font-size: 4rem; font-weight: 700; margin-bottom: 12px; }
        p.subtitle { font-size: 1.15rem; color: #6c757d; font-style: italic; }
        p.hint { margin-top: 28px; font-size: 0.8rem; color: #b0b0b0; font-family: system-ui, sans-serif; text-transform: uppercase; letter-spacing: 3px; animation: pulseHint 2.5s infinite; }
        @keyframes floatCard { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        @keyframes pulseHint { 0%, 100% { opacity: 0.3; } 50% { opacity: 0.8; } }
    </style>
</head>
<body onclick="goToNextPage()">
    <div class="flower" style="left: 12%; animation-delay: 0s;">🌹</div>
    <div class="flower" style="left: 28%; animation-delay: 2.2s; font-size: 26px;">🌸</div>
    <div class="flower" style="left: 55%; animation-delay: 1s;">🌹</div>
    <div class="flower" style="left: 78%; animation-delay: 3.5s; font-size: 25px;">🌷</div>
    <div class="flower" style="left: 88%; animation-delay: 1.5s;">🌹</div>
    <div class="card">
        <h1>Hello bà nha !! 🌹</h1>
        <p class="subtitle">"Một lời chào nhỏ cho một ngày ngọt ngào..."</p>
        <p class="hint">✦ Chạm nhẹ vào bất kỳ đâu để tiếp tục ✦</p>
    </div>
    <script>
        function goToNextPage() {
            document.body.style.opacity = '0';
            setTimeout(() => { window.location.href = '/next'; }, 600);
        }
    </script>
</body>
</html>
"""

# -------------------------------------------------------------
# TRANG 2: Thứ 3 mình đi đâu ăn ta?
# -------------------------------------------------------------
PAGE_2_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thứ 3 ăn gì</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            height: 100vh; display: flex; justify-content: center; align-items: center;
            background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
            font-family: 'Playfair Display', serif; cursor: pointer; user-select: none;
            overflow: hidden; position: relative; animation: fadeIn 0.9s ease-in; transition: opacity 0.6s ease;
        }
        @keyframes fadeIn { from { opacity: 0; transform: scale(0.98); } to { opacity: 1; transform: scale(1); } }
        .flower { position: absolute; bottom: -60px; font-size: 22px; animation: floatUp 8s linear infinite; pointer-events: none; opacity: 0.7; }
        @keyframes floatUp { 0% { transform: translateY(0) rotate(0deg); opacity: 0.7; } 100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; } }
        .card {
            background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(12px);
            padding: 60px 80px; border-radius: 35px; box-shadow: 0 20px 50px rgba(43, 88, 118, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.8); text-align: center; max-width: 90%;
            animation: softPulse 5s ease-in-out infinite;
        }
        @keyframes softPulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.01); } }
        h1 { color: #2b5876; font-size: 2.9rem; font-weight: 600; margin-bottom: 15px; }
        p.quote { font-family: 'Dancing Script', cursive; font-size: 2.3rem; color: #4e73df; margin-top: 12px; }
        .decoration { font-size: 2.5rem; margin-bottom: 12px; }
    </style>
</head>
<body onclick="goToOptionsPage()">
    <div class="flower" style="left: 15%; animation-delay: 0s;">🌹</div>
    <div class="flower" style="left: 45%; animation-delay: 2.5s; font-size: 26px;">🌸</div>
    <div class="flower" style="left: 80%; animation-delay: 1.2s;">🌹</div>
    <div class="card">
        <div class="decoration">🌹</div>
        <h1>Thứ 3 mình đi đâu ăn ta?</h1>
        <p class="quote">~ Hôm đó ăn gì cũng được, miễn là đi cùng nhau ~</p>
    </div>
    <script>
        function goToOptionsPage() {
            document.body.style.opacity = '0';
            setTimeout(() => { window.location.href = '/places'; }, 600);
        }
    </script>
</body>
</html>
"""

# -------------------------------------------------------------
# TRANG 3: Các lựa chọn quán ăn
# -------------------------------------------------------------
PAGE_3_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gợi ý món ăn</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            height: 100vh; display: flex; justify-content: center; align-items: center;
            background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
            font-family: 'Playfair Display', serif; overflow: hidden; position: relative;
            animation: fadeIn 0.9s ease-in; transition: opacity 0.6s ease;
        }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
        .flower { position: absolute; bottom: -60px; font-size: 22px; animation: floatUp 8s linear infinite; pointer-events: none; opacity: 0.7; }
        @keyframes floatUp { 0% { transform: translateY(0) rotate(0deg); opacity: 0.7; } 100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; } }
        .card {
            background: rgba(255, 255, 255, 0.93); backdrop-filter: blur(12px);
            padding: 50px 60px; border-radius: 35px; box-shadow: 0 20px 50px rgba(43, 88, 118, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.8); text-align: center; max-width: 90%; width: 460px;
        }
        h2 { color: #2b5876; font-size: 2.2rem; margin-bottom: 25px; font-weight: 600; }
        .places-list { display: flex; flex-direction: column; gap: 16px; }
        .place-item {
            background: rgba(255, 255, 255, 0.95); padding: 18px 24px; border-radius: 18px; font-size: 1.2rem;
            color: #2b5876; font-weight: 600; box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            border: 2px solid #e2edf8; transition: all 0.3s ease; display: flex;
            align-items: center; justify-content: center; gap: 12px; cursor: pointer;
        }
        .place-item:hover { transform: translateY(-4px); border-color: #76a9fc; background: #ffffff; box-shadow: 0 10px 25px rgba(118, 169, 252, 0.25); }
        .place-item.selected { background: #2b5876 !important; color: white !important; border-color: #2b5876 !important; transform: scale(1.02); }
    </style>
</head>
<body>
    <div class="flower" style="left: 10%; animation-delay: 0s;">🌹</div>
    <div class="flower" style="left: 75%; animation-delay: 2s; font-size: 26px;">🌸</div>
    <div class="card">
        <h2>Gợi ý cho bà nè 🌹</h2>
        <div class="places-list">
            <div class="place-item" onclick="selectPlace('Thai Market', this)">🍲 Thai Market</div>
            <div class="place-item" onclick="selectPlace('The Pizza Company', this)">🍕 The Pizza Company</div>
            <div class="place-item" onclick="selectPlace('Udon & Ramen', this)">🍜 Udon & Ramen</div>
        </div>
    </div>
    <script>
        function selectPlace(placeName, element) {
            element.classList.add('selected');
            setTimeout(() => {
                document.body.style.opacity = '0';
                setTimeout(() => { window.location.href = '/done?choice=' + encodeURIComponent(placeName); }, 500);
            }, 350);
        }
    </script>
</body>
</html>
"""

# -------------------------------------------------------------
# TRANG 4: Xác nhận + Ghi file & In Log Render
# -------------------------------------------------------------
@app.route('/done')
def done_page():
    chosen_place = request.args.get('choice', 'Chưa chọn gì cả')
    
    # Ghi file tạm thời trên server
    try:
        with open("ket_qua.txt", "w", encoding="utf-8") as f:
            f.write(f"Crush da chon quan: {chosen_place}")
    except Exception as e:
        print("Lỗi ghi file:", e)

    # In ra tab Logs trên Render
    print("\n==========================================")
    print(f"CRUSH DA CHON QUAN: {chosen_place}")
    print("==========================================\n", flush=True)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Xác nhận</title>
        <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Playfair+Display:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
                height: 100vh; display: flex; justify-content: center; align-items: center;
                background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
                font-family: 'Playfair Display', serif; overflow: hidden; position: relative; animation: fadeIn 0.9s ease-in;
            }}
            @keyframes fadeIn {{ from {{ opacity: 0; transform: scale(0.96); }} to {{ opacity: 1; transform: scale(1); }} }}
            .flower {{ position: absolute; bottom: -60px; font-size: 22px; animation: floatUp 8s linear infinite; pointer-events: none; opacity: 0.7; }}
            @keyframes floatUp {{ 0% {{ transform: translateY(0) rotate(0deg); opacity: 0.7; }} 100% {{ transform: translateY(-110vh) rotate(360deg); opacity: 0; }} }}
            .card {{
                background: rgba(255, 255, 255, 0.93); backdrop-filter: blur(12px);
                padding: 60px 80px; border-radius: 35px; box-shadow: 0 20px 50px rgba(43, 88, 118, 0.18);
                border: 1px solid rgba(255, 255, 255, 0.8); text-align: center; max-width: 90%;
            }}
            h1 {{ color: #2b5876; font-family: 'Dancing Script', cursive; font-size: 3.5rem; font-weight: 700; margin-bottom: 12px; }}
            p {{ color: #4e73df; font-size: 1.25rem; font-weight: 600; margin-top: 12px; font-style: italic; }}
            .decoration {{ font-size: 2.5rem; margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        <div class="flower" style="left: 20%; animation-delay: 0s;">🌹</div>
        <div class="flower" style="left: 70%; animation-delay: 1.8s; font-size: 26px;">🌸</div>
        <div class="card">
            <div class="decoration">✨🌹✨</div>
            <h1>Oki bà nha !!!</h1>
            <p>(Đã chốt kèo: {chosen_place})</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

# -------------------------------------------------------------
# TRANG XEM KẾT QUẢ BÍ MẬT (Chỉ dành riêng cho bạn)
# Link truy cập: https://chon-quan-an-1.onrender.com/secret-result
# -------------------------------------------------------------
@app.route('/secret-result')
def show_result():
    try:
        with open("ket_qua.txt", "r", encoding="utf-8") as f:
            content = f.read()
        return f"""
        <div style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h2 style="color: #2b5876;">🎉 Kết quả lựa chọn từ Crush:</h2>
            <p style="font-size: 24px; color: #d63384; font-weight: bold; margin-top: 20px;">{content}</p>
        </div>
        """
    except Exception as e:
        return """
        <div style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
            <h3 style="color: #6c757d;">Chưa có kết quả nào được ghi nhận!</h3>
        </div>
        """

# -------------------------------------------------------------
# ROUTING MAIN & PORT BINDING CHO RENDER
# -------------------------------------------------------------
@app.route('/')
def index():
    return render_template_string(PAGE_1_HTML)

@app.route('/next')
def next_page():
    return render_template_string(PAGE_2_HTML)

@app.route('/places')
def places_page():
    return render_template_string(PAGE_3_HTML)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)