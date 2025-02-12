# PyFlet CLI

PyFlet CLI is a command-line interface tool designed to facilitate the creation and management of Flet web projects. It automates the setup process and provides essential commands for project initialization and user management.

## Installation

To install PyFlet CLI, use the following command:

```sh
pip install pyflet
```

## Usage

Run the CLI using:

```sh
pyflet [COMMAND] [OPTIONS]
```

### Commands

#### 1. Create a Flet Web Project

```sh
pyflet create-flet-web <project_name>
```

Creates a new Flet web project using a predefined template.

#### 2. Initialize a Project

```sh
pyflet init-project --reload <true/false> --project_path <path> --platform <web/android/ios>
```

- `--reload`: Automatically reload the project on changes (default: `true`).
- `--project_path`: Path to the main Python file (default: `main.py`).
- `--platform`: Target platform (default: `web`).

#### 3. Create a Superuser

```sh
pyflet createsuperuser
```

Prompts the user to enter credentials and creates a superuser in the database.

#### 4. Get Support

```sh
pyflet support
```

Displays support information and the author's YouTube channel.

## Configuration

### Database Management

This CLI interacts with SQLite databases using the `manage_sql` library. The superuser creation command inserts data into the `users` table.

### Cloning Project Templates

The CLI clones project templates from the repository:

```
https://github.com/webtechmoz/pyflet-models.git
```

It copies template files to the new project directory while replacing placeholders.

## Logging

The CLI provides informative logs in different levels:

- `info`: General information (blue)
- `success`: Successful operations (green)
- `warning`: Potential issues (yellow)
- `error`: Errors encountered (red)

## Contributing

Feel free to contribute to this project by submitting issues or pull requests on GitHub.

## License

This project is licensed under the MIT License.

## Author

Created by DevPythonMZ.

📢 Subscribe to the YouTube channel: [@devpythonMZ](https://youtube.com/@devpythonMZ)