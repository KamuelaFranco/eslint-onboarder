import os
import sys

def log(text):
    try:
        if sys.argv[1] == '--verbose' or sys.argv[1] == '-v':
            print(text)
    except IndexError:
        pass


def traverse_files_and_append_warning_text(warning_text, eslint_ignored, working_dir):
    log(f'Now in {working_dir}')
    files = [item for item in os.listdir(working_dir) \
        if os.path.isfile(f'{working_dir}/{item}')]
    for file in files:
        if file in eslint_ignored:
            files.remove(file)
            log(f'{file} ignored')
    log(f'List of traversable files: {files}')
    for file in files:
        if file.endswith('.js'):
            log(f'Prepending warning text to {file}')
            file_path = f'{working_dir}/{file}'
            file_contents = open(file_path, 'r').read()
            open(file_path, 'w').write(warning_text + file_contents)

    directories = [item for item in os.listdir(working_dir) if os.path.isdir(item)]
    for directory in directories:
        if directory in eslint_ignored:
            directories.remove(directory)
            log(f'{directory}/ ignored')
    log(f'List of traversable directories: {directories}')
    for directory in directories:
        log(f'{directory}/ found and being traversed')
        traverse_files_and_append_warning_text(
            warning_text=warning_text,
            eslint_ignored=eslint_ignored,
            working_dir=f'{working_dir}/{directory}'
        )


if __name__ == '__main__':
    warning_text = '''/* eslint-disable */
// TODO: Remove previous line and work through linting issues at next edit.

'''

    try:
        ignore_list = open('.eslintignore', 'r').read().split('\n')
        eslint_ignored = list(filter(None, ignore_list))
        log(f'Found .eslintignore, ignoring {eslint_ignored}')
    except FileNotFoundError:
        eslint_ignored = ['node_modules', '.git', '.idea']
        log('Did not find .eslintignore, using default of \'node_modules\'')

    traverse_files_and_append_warning_text(
        warning_text=warning_text,
        eslint_ignored=eslint_ignored,
        working_dir='.'
    )
