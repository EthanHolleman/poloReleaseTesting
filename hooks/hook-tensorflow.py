# https://stackoverflow.com/questions/60384288/pyinstaller-modulenotfounderror

from PyInstaller.utils.hooks import collect_all


def hook(hook_api):

    print('\n'*10)
    print('RUNNING HOOK')
    print('\n'*5)

    packages = [
        'tensorflow',
        'tensorflow_core',
        'astor'
    ]
    
    for package in packages:
        datas, binaries, hiddenimports = collect_all(package)
        hook_api.add_datas(datas)
        hook_api.add_binaries(binaries)
        hook_api.add_imports(*hiddenimports)