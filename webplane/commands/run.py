from appframe import Command, Application
from eprint import eprint
from webplane.version import version
from pathlib import Path


FEATURES = ["lib", "boot", "web"]


class StartCommand(Command):
    """
    Start an application

    run
        {app-directory : path to the directory containing the application}
    """

    def handle(self):
        app_directory = Path(self.argument("app-directory"))
        eprint.info("Starting Webplance application server {}", version)
        app = Application(app_directory)
        app.run()
