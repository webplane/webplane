# ProcessorKit App Layout

## Adding CLI Commands
The primary interface for any processkit application is the command line interface, the commands that an pkit app should handle must be provided in the ***commands/*** directory, they will be implicitely imported when the main the application is invoked. Such modules must provide classes based on `cleo.Command`.

## Adding Processing Features
When a pkit application is started, any modules on the ***start/*** directory will be imported, they must provide an activate(*args, kwargs**) function which will be invoked.

any commands available for a pkit application
Command line interface is invoked, any modules on the  ***commands/*** directory will be implicitely imported, 
The processorkit module provides 

## Adding processing features
When a processorkit application is started, any modules on the ***start/*** directory will be imported, they must provide an  `activate()` function will be executed.

