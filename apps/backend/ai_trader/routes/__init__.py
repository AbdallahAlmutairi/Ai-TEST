from . import stocks, auth, predict, chat, alerts, learn, admin, payments


def register_blueprints(app):
    app.register_blueprint(auth.bp)
    app.register_blueprint(stocks.bp)
    app.register_blueprint(predict.bp)
    app.register_blueprint(chat.bp)
    app.register_blueprint(alerts.bp)
    app.register_blueprint(learn.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(payments.bp)
