"""Shim de PyMySQL.

En producción (cPanel) la base de datos es MySQL y no hay compilador para
``mysqlclient``. PyMySQL se hace pasar por ``MySQLdb`` para que el backend
``django.db.backends.mysql`` funcione sin cambios.
"""
try:
    import pymysql

    pymysql.install_as_MySQLdb()
except ImportError:  # En local con SQLite no es necesario.
    pass
