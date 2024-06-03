import sqlite3
from flask import Flask, render_template, request

# Исправление csrf уязвимости
# ────────────────────────────────────────╮
from flask_wtf.csrf import CSRFProtect  # │
# │
csrf = CSRFProtect()                    # │
app = Flask(__name__)                   # │
csrf.init_app(app)                      # │
# ────────────────────────────────────────╯


app = Flask(__name__)


# Исправление debug уязвимости
# ───────────────────────────╮
app.debug = False          # │
# ───────────────────────────╯


def vulnerable_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    success_login = cursor.fetchone()
    if success_login:
        query_token = f"SELECT flag FROM token"
        cursor.execute(query_token)
        result = cursor.fetchone()
        conn.close()
        return result, 200


@app.route('/', methods=['GET', 'POST'])
def vulnerable_login_form():
    if request.method == 'POST':
        login = request.form.get('name')
        password = request.form.get('password')
        result = vulnerable_login(login, password)
    # Добавлен код результата во избежинии узявимости небезопасных http методов
        return render_template('profile.html', result=result), 200
    return render_template('vulnerable.html'), 200


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")  # debug был изменён с True на False
    # во избежании debug уязвимости
