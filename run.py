from pickle import FALSE
from application import application
from application.controllers.user import bp_app as user_mod
from application.controllers.user_wallet import bp_app as wallet_mod
from application.controllers.transaction import bp_app as transaction_mod
from application.controllers.currency import bp_app as currency_mod
from application.controllers.notification import bp_app as notification_mod

application.register_blueprint(user_mod)
application.register_blueprint(wallet_mod)
application.register_blueprint(transaction_mod)
application.register_blueprint(currency_mod)
application.register_blueprint(notification_mod)
application.run(port=9000, host="0.0.0.0", debug=FALSE)