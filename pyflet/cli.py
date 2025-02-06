import typer
import os
import subprocess
from datetime import datetime
from time import sleep

app = typer.Typer()

@app.command(name='create_flet_web', help='Add new flet web project')
def create(project_name: str):
    log_message(
        message=f'📂 Criando o projecto {project_name}',
    )
    os.makedirs(name=project_name, exist_ok=True)

    log_message(
        message=f'📂 Criando os directorios principais do {project_name}',
    )
    dirname_list = os.listdir('models')

    for dir in dirname_list:
        if os.path.isdir(os.path.join('models', dir)):
            log_message(
                message=f'📂 Criando o directorio {dir}',
            )
            os.makedirs(os.path.join(project_name, dir), exist_ok=True)

            if dir == 'assets':
                log_message(
                    message=f'🎁 Criando a imagem principal',
                )
                create_image(
                    image_name='flet.png',
                    dir=dir,
                    project_name=project_name
                )
            
            else:
                for file_path in os.listdir(os.path.join('models', dir)):
                    if '__init__.py' not in file_path:
                        log_message(
                            message=f'🔗 Criando o ficheiro {file_path}',
                        )
                        create_file(
                            file_name=file_path,
                            dir=os.path.join('models', dir),
                            project_name=os.path.join(project_name, dir)
                        )
        
        else:
            if '__init__.py' not in file_path:
                log_message(
                    message=f'🔗 Criando o ficheiro {dir}',
                )
                create_file(
                    file_name=dir,
                    dir='models',
                    project_name=project_name
                )
    
    log_message(
        message=f'✅ Projecto {project_name} criado com sucesso',
        level='sucess'
    )

@app.command(name='init_project', help='Initialize your project')
def init_project(reload: bool = True, project_path: str = 'main.py', platform: str = 'web'):
    command = f"flet -r {project_path} --{platform}" if reload else f"flet {project_path} --{platform}"

    try:
        log_message(
            message=f'✨ Projecto iniciado com sucesso',
            level='sucess'
        )
        subprocess.run(command, shell=True, check=True)
    
    except subprocess.CalledProcessError as e:
        log_message(
            message=f'❌ Erro ao executar o projecto',
            level='error'
        )

@app.command(name='support', help='For help & support, read the notes')
def support():
    message = 'CLI created by DevPythonMZ\nSubscribe on your youtube channel with https://youtube.com/@devpythonMZ \nThank you'
    typer.echo(
        message=message
    )


def create_file(file_name: str, dir: str, project_name: str):
    with open(f'{os.path.join(dir, file_name)}', 'r') as model_file:
        with open(f'{os.path.join(project_name, file_name)}', 'w') as file:
            file.write(
                model_file.read()
                if 'main.py' not in file_name
                else model_file.read().replace('project title', project_name.replace('_', ' ').strip().capitalize())
            )

def create_image(image_name: str, dir: str, project_name: str):
    with open('models/assets/flet_image.txt', 'rb') as file:
        with open(f'{os.path.join(project_name, dir, image_name)}', 'wb') as pic:
            pic.write(file.read())

def log_message(message: str, level: str = 'info'):
    # Exibir as messagens durante a execução do CLI
    time = datetime.now().strftime('%H:%M:%S')

    colors = {
        'info': typer.colors.BRIGHT_BLUE,
        'sucess': typer.colors.GREEN,
        'warning': typer.colors.YELLOW,
        'error': typer.colors.RED
    }

    typer.echo(
        typer.style(
            text=f'[{time}] {message}',
            fg=colors.get(level, typer.colors.WHITE)
        )
    )

    sleep(0.5)

if __name__ == '__main__':
    app()