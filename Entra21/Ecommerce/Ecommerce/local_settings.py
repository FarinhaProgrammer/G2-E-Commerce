SECRET_KEY = 'django-insecure-s)cf1c(3ss*^1fxfpq#83=l(m*z-zhrq^_on(c1#8-ypca81mf'


DbSqLite = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

DbMySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DbE21G2',
        'USER': 'dbe21g2',
        'PASSWORD': 'b2349kluMenaUfazmuTtocalor2.*',
        'HOST': 'dbsolapp01.sol.app.br',
        'PORT': '3306',
        'OPTIONS':  {
            'ssl': {'ca': 'C:/ssl/server-ca.pem',
            'cert': 'C:/ssl/client-cert.pem',
            'key': 'C:/ssl/client-key.pem'
            }
        }
    }
}

#DATABASES = DbSqLite 
DATABASES = DbMySQL




