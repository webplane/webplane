# Introduction and Installation

!!! Important
    This documentation is on the initial phase of development, breaking changes are likely to be introduced until the v1.0 release.

Webplane is an open source HTTP application server for Python with a focus on rapid web application development and deployment. It leverages some of the best tecnhologies like the [CherryPy] web server and the [Jinja] templating engine.


[CherryPy]: https://cherrypy.org/
[Jinja]: https://jinja.palletsprojects.com/


## Developer Features

- [x] Automatic web routing based on the application directory structure
- [x] Automatic rendering of composed web templates (Thanks to Jinja)
- [x] Automatic web to functions arguments mapping (Thanks to CherryPy)
- [x] Automatic deployments from Github (using GitHub actions)
- [x] Runs on Linux, Mac and Windows

## Production Features
- [x] HTTPS listener configuration
- [x] Client SSL Authentication
- [x] Deployment tools for: [CloudFoundry]; [Docker]; [Kubernetes]

[CloudFoundry]: https://www.cloudfoundry.org/
[Docker]: https://www.docker.com/
[Kubernetes]: https://kubernetes.io/

## Requirements

A Linux, MacOS or Windows system with Python 3.6+

!!! Information
    if you are new to Python you can get started by reading the [Python For Beginners] guide.

[Python For Beginners]: https://www.python.org/about/gettingstarted/

## Installation

Webplane is avaiable from the official Python Package Index (PIP), you can install it from the terminal:
```bash
pip install webplane
```

You can ensure webplane and craft installed correctly by running:
```sh
webplane
```
You should see a list of commands like `create` and `run` .

## Creating your first application
```sh
webplane create «application_directory»
```
The create command will create a webplane starter application at the specified directory.

