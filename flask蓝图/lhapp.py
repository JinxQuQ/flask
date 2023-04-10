from flask import Flask
import lhnews
import lhproducts

app = Flask(__name__)

app.register_blueprint(lhproducts.blueprint)
app.register_blueprint(lhnews.blueprint)

app.run(debug=True,port=80)
