import typer
import os
import subprocess
from datetime import datetime
from time import sleep
import tempfile
from manage_sql import SQLITE

app = typer.Typer()

@app.command(name='create-flet-web', help='Add new flet web project')
def create(project_name: str):
    with tempfile.TemporaryDirectory() as temp_path:
        try:
            log_message(
                message=f'🔗 Clonando o projecto modelo {project_name}',
            )
            clone_project_model(parent_path=temp_path)
            model_files = os.listdir(temp_path)

            log_message(
                message=f'📂 Criado o diretorio do projeto {project_name}',
            )
            project_path = create_path(child_path=project_name)

            for model_file in model_files:
                if os.path.isdir(os.path.join(temp_path, model_file)):

                    sub_path = os.path.join(temp_path, model_file)

                    if '.git' not in model_file:
                        log_message(
                            message=f'📂 Criando o directorio {model_file}',
                        )
                        new_path = create_path(child_path=model_file, parent_path=project_path)

                        for sub_file in os.listdir(sub_path):
                            create_file(
                                file=sub_file,
                                old_path=sub_path,
                                new_path=new_path,
                                project_name=project_name
                            )
                
                else:
                    create_file(
                        file=model_file,
                        old_path=temp_path,
                        new_path=project_path,
                        project_name=project_name
                    )
            
            log_message(
                message=f'✅ Projecto {project_name} criado com sucesso',
                level='sucess'
            )
        
        except Exception as e:
            log_message(
                message=f'❌ Erro ao criar o projecto\n {e}',
                level='error'
            )

@app.command(name='init-project', help='Initialize your project')
def init_project(reload: bool = True, project_path: str = 'main.py', platform: str = 'web'):
    valid_platforms = ['web', 'android', 'ios']
    if platform not in valid_platforms:
        log_message(
            message=f"❌ Opção inválida para 'platform'. As opções válidas são: {', '.join(valid_platforms)}.",
            level='error'
        )
        return
    
    command = f"flet -r {project_path} --{platform}" if reload else f"flet {project_path} --{platform}"
    
    try:
        log_message(
            message=f'✨ Tentando iniciar o projecto',
            level='warning'
        )
        subprocess.run(command, shell=True, check=True)
    
    except subprocess.CalledProcessError as e:
        log_message(
            message=f'❌ Erro ao executar o projecto',
            level='error'
        )

@app.command(name='createsuperuser', help='Create the superuser for your project')
def creater_user():
    username = verifiy_input(text='Please, enter the username')
    email = verifiy_input(text='Please, enter the email')

    while True:
        password = verifiy_input(text='Please, enter the password')
        confirm_password = verifiy_input(text='Please, enter again the password')

        if password == confirm_password:
            insert_user(
                username=username,
                email=email,
                usertype='superuser',
                status=True,
                password=password
            )
            break
        
        else:
            log_message(message='The password that you enter is different, enter again\n', level='warning')

def insert_user(
    username: str,
    email: str,
    usertype: str,
    status: str,
    password: str
):
    try:
        db = SQLITE(database='database')
        db.insert_data(
            tablename='users',
            insert_query=[
                db.ColumnData(
                    column='username',
                    value=username
                ),
                db.ColumnData(
                    column='email',
                    value=email
                ),
                db.ColumnData(
                    column='usertype',
                    value=usertype
                ),
                db.ColumnData(
                    column='password',
                    value=db.encrypt_value(value=password)
                ),
                db.ColumnData(
                    column='status',
                    value=status
                )
            ]
        )

        log_message(message='User created sucessfull')
    
    except Exception as e:
        log_message(message='We get error when we try to save on database', level='error')

@app.command(name='support', help='For help & support, read the notes')
def support():
    message = 'CLI created by DevPythonMZ\nSubscribe on your youtube channel with https://youtube.com/@devpythonMZ \nThank you'
    typer.echo(
        message=message
    )

def verifiy_input(text: str = None):
    while True:
        input_user = input(f'{text}: ').strip()

        if input_user:
            return input_user
        
        log_message(message='Wrong enter, please enter again!', level='warning')

def clone_project_model(parent_path: str):
    try:
        git_url = 'https://github.com/webtechmoz/pyflet-models.git'
        subprocess.run(['git', 'clone', git_url, parent_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    except subprocess.CalledProcessError as e:
        print(f'Ocorreu um erro grave: {e}')

def create_path(child_path: str, parent_path: str = None):
    if parent_path:
        os.makedirs(os.path.join(parent_path, child_path), exist_ok=True)

        return os.path.join(parent_path, child_path)
    
    else:
        os.makedirs(child_path, exist_ok=True)

        return child_path

def create_file(file: str, old_path: str, new_path: str, project_name: str):
    if not file.endswith('.txt'):
        log_message(
            message=f'🔗 Criando o ficheiro {file}',
        )
        with open(os.path.join(old_path, file), 'r') as model_file:
            with open(os.path.join(new_path, file), 'w') as new_file:
                new_file.write(model_file.read().replace(
                        'project title',
                        project_name.replace('_', ' ').strip().capitalize()
                    )
                )
    
    else:
        log_message(
            message=f'🎁 Criando a imagem principal',
        )
        with open(os.path.join(old_path, file), 'rb') as model_file:
            with open(os.path.join(new_path, file.replace('_image.txt', '.png')), 'wb') as new_file:
                new_file.write(model_file.read())

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