@albertfast ➜ /workspaces/DjangoDemo (main) $ git remote -v
origin  https://github.com/albertfast/DjangoDemo (fetch)
origin  https://github.com/albertfast/DjangoDemo (push)
upstream        https://github.com/CTI-CodeDay/DjangoDemo.git (fetch)
upstream        https://github.com/CTI-CodeDay/DjangoDemo.git (push)
@albertfast ➜ /workspaces/DjangoDemo (main) $ git branch asahiner
@albertfast ➜ /workspaces/DjangoDemo (main) $ git checkout asahiner
Switched to branch 'asahiner'
@albertfast ➜ /workspaces/DjangoDemo (asahiner) $ git branch -m asahiner_django_tutorial
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ virtualenv --python=/usr/bin/python3.8 .
created virtual environment CPython3.8.10.final.0-64 in 1163ms
  creator CPython3Posix(dest=/workspaces/DjangoDemo, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/codespace/.local/share/virtualenv)
    added seed packages: pip==24.3.1, setuptools==75.3.0, wheel==0.45.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ python version
python: can't open file '/workspaces/DjangoDemo/version': [Errno 2] No such file or directory
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ python --version
Python 3.12.1
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ python -m pip install Django
Collecting Django
  Downloading Django-5.1.4-py3-none-any.whl.metadata (4.2 kB)
Collecting asgiref<4,>=3.8.1 (from Django)
  Downloading asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from Django)
  Downloading sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Downloading Django-5.1.4-py3-none-any.whl (8.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.3/8.3 MB 46.5 MB/s eta 0:00:00
Downloading asgiref-3.8.1-py3-none-any.whl (23 kB)
Downloading sqlparse-0.5.3-py3-none-any.whl (44 kB)
Installing collected packages: sqlparse, asgiref, Django
  WARNING: The script sqlformat is installed in '/usr/local/python/3.12.1/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script django-admin is installed in '/usr/local/python/3.12.1/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Django-5.1.4 asgiref-3.8.1 sqlparse-0.5.3
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip delete django
ERROR: unknown command "delete"
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ python -m pip delete django
ERROR: unknown command "delete"
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip install django==2.1.7
Collecting django==2.1.7
  Downloading Django-2.1.7-py3-none-any.whl.metadata (3.5 kB)
Requirement already satisfied: pytz in /home/codespace/.local/lib/python3.12/site-packages (from django==2.1.7) (2024.2)
Downloading Django-2.1.7-py3-none-any.whl (7.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 47.7 MB/s eta 0:00:00
Installing collected packages: django
  Attempting uninstall: django
    Found existing installation: Django 5.1.4
    Uninstalling Django-5.1.4:
      Successfully uninstalled Django-5.1.4
Successfully installed django-2.1.7
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip freeze

@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ deactivate
DeprecationWarning: 'source deactivate' is deprecated. Use 'conda deactivate'.
@albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ source bin/activate
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip freeze
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ git remote -v
origin  https://github.com/albertfast/DjangoDemo (fetch)
origin  https://github.com/albertfast/DjangoDemo (push)
upstream        https://github.com/CTI-CodeDay/DjangoDemo.git (fetch)
upstream        https://github.com/CTI-CodeDay/DjangoDemo.git (push)
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ git status
On branch asahiner_django_tutorial
nothing to commit, working tree clean
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip freeze
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ activate
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip freeze
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ virtualenv --python=/usr/bin/python3.8 .
created virtual environment CPython3.8.10.final.0-64 in 383ms
  creator CPython3Posix(dest=/workspaces/DjangoDemo, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/codespace/.local/share/virtualenv)
    added seed packages: pip==24.3.1, setuptools==75.3.0, wheel==0.45.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ pip freeze
(DjangoDemo) @albertfast ➜ /workspaces/DjangoDemo (asahiner_django_tutorial) $ ==> suanda django virtual env de actif mi?

title: "Dell XPS 13", description: "Intel Core i7 11th Gen\nIntel Iris Xe Graphics\n512 GB SSD 16GB RAM", price: 1250.99, summary: "Perfect for professionals!"