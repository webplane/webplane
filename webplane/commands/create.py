import shutil
from appframe import Command
from pathlib import Path
from eprint import eprint


class CreateCommand(Command):
    """
    Create an application using a template

    create
        {app-directory : path to the directory containing the application}
        {template-name? : template to use as the base for the application}
        {--force : overwrite directory if it already exists}
    """

    def handle(self):
        app_directory = self.argument("app-directory")
        force = self.option("force")
        if Path(app_directory).exists():
            if force:
                shutil.rmtree(app_directory)
            else:
                eprint.error(
                    "{} already exists, if you want to overwrite it add {}",
                    app_directory,
                    "--force",
                )
                exit(1)
        starter_app_dir = Path(Path(__file__).parent, "..", "starter_app_template")
        shutil.copytree(starter_app_dir, app_directory)
