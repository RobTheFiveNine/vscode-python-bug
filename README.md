## Environment data

- VS Code version: 1.42.1
- Extension version (available under the Extensions sidebar): 2020.2.64397
- OS and version: Ubuntu 18.04
- Python version (& distribution if applicable, e.g. Anaconda): 3.6.7
- Type of virtual environment used (N/A | venv | virtualenv | conda | ...): venv
- Relevant/affected Python packages and their versions: N/A
- Relevant/affected Python-related VS Code extensions and their versions: N/A
- Jedi or Language Server? (i.e. what is `"python.jediEnabled"` set to; more info #3977): `false`
- Value of the `python.languageServer` setting: `Microsoft`

## Expected behaviour

When launching vscode, the tests from the `tests/` directory should be discovered successfully; regardless of whether the project has been installed as a package.

## Actual behaviour

Import errors are thrown out in the output tab and test discovery fails. 

**Example output:**
```
python <path_to_home>/.vscode/extensions/ms-python.python-2020.2.64397/pythonFiles/testing_tools/run_adapter.py discover pytest -- --rootdir <path_to_project> -s --cache-clear -o junit_family=xunit1
Test Discovery failed: 
Error: ============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: <path_to_project>
collected 0 items / 4 errors

==================================== ERRORS ====================================
__________________ ERROR collecting <path_to_test_file> ___________________
ImportError while importing test module '<path_to_test_file> '.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
<path_to_test_file>:5: in <module>
    import <module_within_project>
E   ImportError: cannot import name '<module_name>'
```
Running pytest separately, with the same launch arguments works fine in a terminal window, but when executed using vscode's test discovery function, it fails to import unless the project is installed as a package first (i.e. by running `python setup.py install --record record.txt`)

## Steps to reproduce:

1. Clone this sample repository: https://github.com/RobTheFiveNine/vscode-python-bug
2. Create a venv: `virtualenv venv -p python3`
3. Activate it: `source venv/bin/activate`
4. Install pytest: `pip install pytest`
5. In a terminal, to verify pytest works, run `python -m pytest` in the project directory
6. To verify it doesn't work in vscode, open vscode and configure the Python extension to use pytest, see that test discovery fails
7. Open the output tab and view the Python Test Log section to see the errors
8. After seeing it fail, run `python setup.py install --record record.txt` to install the project as a package in the venv, and then click on the tests label in the status bar or relaunch vscode, to find that vscode now discovers the tests successfully

## Logs
```
python <path_to_home>/.vscode/extensions/ms-python.python-2020.2.64397/pythonFiles/testing_tools/run_adapter.py discover pytest -- --rootdir <path_to_project> -s --cache-clear -o junit_family=xunit1
Test Discovery failed: 
Error: ============================= test session starts ==============================
platform linux -- Python 3.6.7, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: <path_to_project>
collected 0 items / 4 errors

==================================== ERRORS ====================================
__________________ ERROR collecting <path_to_test_file> ___________________
ImportError while importing test module '<path_to_test_file> '.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
<path_to_test_file>:5: in <module>
    import <module_within_project>
E   ImportError: cannot import name '<module_name>'
```
