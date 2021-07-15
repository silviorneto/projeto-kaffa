from flask import Flask


def init_app(app: Flask) -> None:
    # import das bps e registro das blueprints abaixo
    from .login_view import bp as bp_login
    from .user_view import bp as bp_user
    from .account_view import bp as bp_account
    from .waiter_view import bp as bp_waiter
    from .payment_method_view import bp as bp_payment_method
    from .cashier_view import bp as bp_cashier
    from .provider_view import bp as bp_provider
    from .manager_view import bp as bp_manager
    from .table_view import bp as bp_table
    from .operator_view import bp as bp_operator
    from .product_view import bp as bp_product
    from .account_product_view import bp as bp_account_product
    # from .stock_product_view import bp as bp_stock_product
    from .provider_product_view import bp as bp_provider_product
    from .operator_cashier_view import bp as bp_operator_cashier
    from .purchase_order_views import bp as bp_purchase_order
    from .product_purchase_order import bp as bp_product_purchase_order

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_account)
    app.register_blueprint(bp_waiter)
    app.register_blueprint(bp_payment_method)
    app.register_blueprint(bp_cashier)
    app.register_blueprint(bp_provider)
    app.register_blueprint(bp_manager)
    app.register_blueprint(bp_table)
    app.register_blueprint(bp_operator)
    app.register_blueprint(bp_product)
    app.register_blueprint(bp_account_product)
    # app.register_blueprint(bp_stock_product)
    app.register_blueprint(bp_provider_product)
    app.register_blueprint(bp_operator_cashier)
    app.register_blueprint(bp_purchase_order)
    app.register_blueprint(bp_product_purchase_order)
