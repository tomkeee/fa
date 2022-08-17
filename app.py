from flask import Flask
from main import GroupAPI,DataCRUD

app = Flask(__name__)
app.add_url_rule('/', view_func=GroupAPI.as_view('show_users'))
app.add_url_rule('/<id>', view_func=DataCRUD.as_view('show_users_crud'))

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


def create_app():
   return app