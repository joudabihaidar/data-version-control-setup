import os
import subprocess

def run_command(command):
    result=subprocess.run(command, shell=True, capture_output=True, text=True)
    # stdout: standard output
    # stderr: standard error
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

def initialize_dvc_git_repo(repo_path):
    os.chdir(repo_path)
    run_command('git init')
    run_command('dvc init')
    run_command('git add .dvc .gitignore')
    run_command('git commit -m "Initialize DVC project"')

def add_remote(github_repo_url):
    run_command(f'git remote add origin {github_repo_url}')
    run_command('git push -u origin master')

def configure_dvc_remote(repo_path, remote_name, drive_folder_id):
    # Configure DVC remote storage with Google Drive.
    os.chdir(repo_path)
    run_command(f'dvc remote add -d {remote_name} gdrive://{drive_folder_id}')
    run_command('git add .dvc/config')
    run_command('git commit -m "Configure DVC remote storage"')
    #run_command('dvc remote modify --local {remote_name} gdrive_use_service_account true')

def add_and_track_data(repo_path, data_file):
    # Adding for the first time a data file with DVC and pushing to remote storage.
    os.chdir(repo_path)
    run_command(f'dvc add {data_file}')
    run_command(f'git add {data_file}.dvc .gitignore')
    run_command('git commit -m "Track data file with DVC"')
    run_command('dvc push')

def change_and_version_data(repo_path, data_file):
    # tracking changes and updates in the data
    os.chdir(repo_path)
    run_command(f'dvc add {data_file}')
    run_command(f'git add {data_file}.dvc')
    run_command('git commit -m "Update data file"')
    run_command('dvc push')

def main():
    repo_path = r"C:\Users\Legion\Desktop\dvc_setup"
    data_file = 'data/data.csv'
    remote_name = 'myremote'
    drive_folder_id = '14OTN7AaJJlXYzOuRuEjeCAldEEds4ZWN'
    github_repo_url = 'https://github.com/joudabihaidar/data-version-control-setup.git'

    # # Initializing a Git and DVC repository 
    # initialize_dvc_git_repo(repo_path)

    # # adding a remote GitHub repository URL to the local Git repository
    # add_remote(github_repo_url)

    # # Configuring DVC remote storage with Google Drive
    # configure_dvc_remote(repo_path, remote_name, drive_folder_id)

    # # Track data file with DVC and push to remote storage
    # add_and_track_data(repo_path, data_file)

    # Push changes to GitHub
    change_and_version_data(repo_path,data_file)


if __name__ == "__main__":
    main()
