from flask import flask, josniy, Flask


def onko_alkuluku(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
app = Flask(__name__)
@app.route('/alkuluku/<int:n>', methods = ['GET'])

def alkuluku(n):
    tulos = onko_alkuluku(n)
    return jsonify({"Number": n, "isprime": tulos})


if __name__ == '__main__':
    app.run(debug=True)




