
"""
WSGI config for proyecto3 project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Configurar PyMySQL como reemplazo de MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto3.settings")

application = get_wsgi_application()
