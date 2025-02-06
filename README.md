# PYFLET CLI

A simple command-line interface (CLI) tool for generating and managing web projects using Flet.

## Features
- Create new Flet web projects with a predefined structure.
- Initialize and start Flet projects with optional configurations.
- Get support and helpful resources.

## Installation

To install the CLI via pip:

```bash
pip install pyflet
```

## Create a New Flet Web Project

You can create a new Flet web project like this:

```bash
pyflet create_flet_web <project_name>
```

This command creates a project with the required directories and files.

## Initialize a Project

You can initialize and start a project with the following command:

```bash
pyflet init_project [--reload] [--project_path <path>] [--platform <platform>]
```

- `--reload`: (Optional) Starts the project with automatic reloading.
- `--project_path`: (Optional) Defines the path of the project's main file (default: `main.py`).
- `--platform`: (Optional) Specifies the target platform (`web` by default).

## Support & Help

If you need support or further information, run:

```bash
pyflet support
```

This will display support details and a link to the YouTube channel `DevPythonMZ`.

## Example Usage

```bash
pyflet create_flet_web my_project
cd my_project
pyflet init_project
```

This will create a new project and start the application automatically.

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute.

## License
This project is licensed under the MIT License.