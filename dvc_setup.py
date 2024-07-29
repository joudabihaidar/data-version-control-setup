import os
import subprocess

def run_command(command):
    """
    This function executes a system command and print its output.
    """
    result=subprocess.run(command, shell=True, capture_output=True, text=True)
    # stdout: standard output
    # stderr: standard error
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result


def initialize_git_repo(repo_path):
    """Initialize a Git repository."""
    os.chdir(repo_path)
    run_command('git init')
    run_command('dvc init')
    run_command('git add .dvc .gitignore')
    run_command('git commit -m "Initialize DVC project"')

def configure_dvc_remote(repo_path, remote_name, drive_folder_id):
    """Configure DVC remote storage with Google Drive."""
    os.chdir(repo_path)
    run_command(f'dvc remote add -d {remote_name} gdrive://{drive_folder_id}')
    run_command('dvc remote modify --local {remote_name} gdrive_use_service_account true')

def track_and_push_data(repo_path, data_file):
    """Track a data file with DVC and push to remote storage."""
    os.chdir(repo_path)
    run_command(f'dvc add {data_file}')
    run_command(f'git add {data_file}.dvc .gitignore')
    run_command('git commit -m "Track data file with DVC"')
    run_command('dvc push')

def main():
    repo_path = r"C:\Users\Legion\Desktop\dvc_setup"
    data_file = 'data/data.csv'
    remote_name = 'myremote'
    drive_folder_id = '14OTN7AaJJlXYzOuRuEjeCAldEEds4ZWN'
    github_repo_url = 'https://github.com/joudabihaidar/data-version-control-setup.git'

    # Initializing a Git repository 
    initialize_git_repo(repo_path)

    # Configuring DVC remote storage with Google Drive
    configure_dvc_remote(repo_path, remote_name, drive_folder_id)

    # Track data file with DVC and push to remote storage
    track_and_push_data(repo_path, data_file)

    # Push changes to GitHub
    run_command(f'git remote add origin {github_repo_url}')
    run_command('git push -u origin master')

if __name__ == "__main__":
    main()
