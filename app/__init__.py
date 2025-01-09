from flask import Flask

# 初始化 Flask 應用
def create_app():
    app = Flask(__name__)

    # 註冊 Blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
