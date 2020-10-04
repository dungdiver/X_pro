# X_pro
Web app for X_pro database

# flask migrate
<!-- Thay dòng này vào file env.py -->
db_url_escaped = current_app.config.get('SQLALCHEMY_DATABASE_URI').replace('%', '%%')
config.set_main_option('sqlalchemy.url', db_url_escaped)