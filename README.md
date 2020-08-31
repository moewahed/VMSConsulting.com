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
