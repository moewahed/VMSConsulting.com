# VMSConsulting.com

Django - Python Web Development Project
> Using Python 3.8 and Django 2.2

## Environment

- Version Controll
    - Git-Flow
- CI & CD
    - Docker Used for Redis as Cache and Message broker
    install for:
      - MAC > https://docs.docker.com/docker-for-mac/install/
      - Windows > https://docs.docker.com/docker-for-windows/install/
      - Linux > https://docs.docker.com/engine/install/
- IDE
    - IntelliJ
- Back-end
    - Back-end Language : Python 3.8
    - Back-end Framework : Django 2.2
- Front-end
    - Front-end : HTML, CSS (BOOTSTRAP), JavaScirpt (JQuery) --->(Basics)
    
# Run Redis on Docker
After Installing the right installation for your OS you need to open Terminal on MAC/Linux or PowerShell on Windows, and then run the below code:

> docker run --name=redis-devel --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest

Docker will take care of downloading the latest version of Redis and the run it.
If Environment stops or you did restart the machine you can easily run it again from the Docker Software, by opening it and then press on the (PLAY BUTTON :P), and that's it

# More
You can Change the Email Config in setting.py with your Gmail, Yahoo, Hotmail, or what ever you want, in this project the SMTP service we used is Google
```
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' # We decaler Gmail SMTP as the HOST email, or search in Google for "smtp django (Yehoo!, HotMail, etc)"
EMAIL_PORT = 587 # Port of Gmail SMTP, or search in Google for "smtp django (Yehoo!, HotMail, etc) port"
EMAIL_HOST_USER = 'email@gmail.com' # Your Email
EMAIL_HOST_PASSWORD = 'password' # Not the Actual Password, you can set a third-party app password using Gmail follow the link 
                                 # https://support.google.com/mail/answer/185833?hl=en

```


If you wish to run the server without the chat app you can do some stuff, and then you good to go:

- Comments Settings APPS:
    Go to setting.py and comment out the below lines
    ```
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    ....
    \# Created APPs
    'addon',
    'account',
    'chat', ---> this one
    'idea',

    \# Third-Party APPs
    'rest_framework',
    'rest_framework.authtoken',
    'django_countries',
    \# 'redis', ---> this one
    \# 'django_redis', ---> this one
    \# 'channels', ---> this one
    ```

- Also I recommend to comment the Channel Layers Config in setting.py
```
# Redis Config
# CHANNEL_LAYERS = {
#    'default': {
#        'BACKEND': 'channels_redis.core.RedisChannelLayer',
#        'CONFIG': {
#            "hosts": [('127.0.0.1', 6379)],
#            # "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')]
#        },
#    },
#}
```
