# Introduction and Installation

Webplane is an open source HTTP application server for Python, it integrates some of the best Python tecnhologies like the [CherryPy] web server and the [Jinja] templating engine in order to provide a rapid web application development experience.


[CherryPy]: https://cherrypy.org/
[Jinja]: https://jinja.palletsprojects.com/


## Developer Features
- Automatic web routing based on the application directory structure
- Automatic rendering of composed web templates (Thanks to Jinja)
- Automatic web to functions arguments mapping (Thanks to CherryPy)
- Automatic deployments from Github (using GitHub actions)
- Runs on Linux, Mac and Windows

## Production Features
- HTTPS listener configuration
- Client SSL Authentication
- Deployment tools for: [CloudFoundry]; [Docker]; [Kubernetes]

[CloudFoundry]: https://www.cloudfoundry.org/
[Docker]: https://www.docker.com/
[Kubernetes]: https://kubernetes.io/

## Requirements

A Linux, MacOS or Windows system with Python 3.6+, if you are new to Python you probably should read the [Python For Beginners] guide.

[Python For Beginners]: https://www.python.org/about/gettingstarted/

## Installation

Webplane is avaiable from the official Python Package Index, it can be installed from the terminal with:
```sh
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

