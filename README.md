# FastAPI Backend Server with CPython Integration

## System Requirement
1. tested on Python 3.9.13

## Installations
1. Clone the repository to your computer.
2. Create a virtual environment for this project.

    `python -m venv ~/virtualenv/raycastventures`

3. Activate the virtual environment

    `source ~/virtualenv/raycastventures/bin/activate`

4. Install the requirements. Alternatively install these libraries (fastapi, Cython, pytest) using pip.

    `pip install -r requirements.txt`

5. Run `cythonize` command to compile the `concat_impl.pyx` file to generate an extension module (.so file).

    `cythonize -a -i concat_impl.pyx`

6. Running tests with pytest:

    `pytest`

7. To run the fastapi server, run `fastapi dev main.py` then visit http://localhost:8000 in the browser.

## Example URLs used in the test
### Regular strings
    http://localhost:8000/concatenate?str1=abc&str2=xyz

    * str1 = "abc"
    * str2 = "xyz"

### Empty strings
    http://localhost:8000/concatenate?str1=&str2=

    * str1 = ""
    * str2 = ""

### Special characters
    http://localhost:8000/concatenate?str1=abc&str2=xyz%21%40%23%24

    * str1 = "abc"
    * str2 = "xyz!@#$"

### Long strings
    http://localhost:8000/concatenate?str1=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&str2=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    
    * str1 = "aaaaaaaa..."
    * str2 = "bbbbbbbb..."
    
