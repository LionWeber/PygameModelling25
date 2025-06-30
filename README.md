# **PyGame Modelling Workshop 2023**

**Pyg**ame **Mod**elling **W**orkshop 20**25** (pygmodw25).

This is the offcicial repo of the pygame modelling course for collective systems workshop 2025 Berlin.

## Welcome to the Workshop
During this workshop you will learn about using a python-based game engine (pygame) for agent-based modelling and simulation tasks to model collective behavior and to collect analyze and visualize the resulting data.
To use the provided code base you will need the following:

### 1. Prerequisites
1. **Operating System:** The code has been tested on Ubuntu 18, Windows 10, and MacOS
2. **Python 3.7+:** You will need to have a python version >=3.7.0. You can check the version of your python interpreter with `python --version`. In case you have multiple python base versions (e.g. 2.x and 3.x) you might need to use `python3 --version`. In case your python (3) version is lower than 3.7 or you don't have python3 installed on your system yet, please follow [this guide](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install python 3.7 on Ubuntu, Windows or Mac.
3. **pip:** To install all the requirements of the code we will use pip. Please be sure to have a pip version for python 3+ (and not for python 2). You can check this with `pip --version` or sometimes `pip3 --version` in case of multiple python base versions (e.g. 2.x and 3.x) and by that multiple pip versions. The resulting line should end with "(python 3.x)" where x is the minor version of your python interpreter and should be larger or equal than 7. In case you have multiple minor versions (e.g. 3.5 and 3.7, use `python3.7 -m pip --version` or any minor version larger or equal to 7). In case you don't have pip installed yet use this guide to install pip on [Windows](https://www.liquidweb.com/kb/install-pip-windows/), [Ubuntu](https://www.odoo.com/forum/help-1/how-to-install-pip-in-python-3-on-ubuntu-18-04-167715) or [Mac](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/#macos).
4. **GIT:** to access the code you will need git installed on your system. In case this is not yet done, please install it using [this guide](https://github.com/git-guides/install-git).

**At this point you have python3.7+, pip (for the same python version) and git installed on your system.**

### 2. Installation and Test
5. **Clone this repo:** Open the terminal and use the following command to clone the repo 
  
```bash
git clone https://github.com/scioip34/PygameModelling23.git
```
  
6. **Create/activate new virtual environment**: We highly recommend using a virtual environment for the workshop so that you don't have version mismatches with other projects. We recommend using [venv](https://docs.python.org/3/library/venv.html) and we suppose you are using venv in the instructions. If you decide to use another virtual environment (such as pipenv or conda) or not to use any, some differences may show up during the installation.

On Linux/MacOS:
```bash
# Move into the newly created/cloned directory
cd PygameModelling23

# Create a new virtual environment in the folder venv
# it can happen that you need to use python or python3.x instead of python3 according to
# your installation where x is your python's minor version
python3 -m venv ./venv

# Note: On Debian/Ubuntu systems you may receive an error message stating that you need 
# to install the python3-venv package in order to be able to create the environment. 
# In this case, executing 'sudo apt install python3.X-venv' with X indicating your 
# Python's minor version, should resolve the issue. 


# Activate the virtual environment
source ./venv/bin/activate
```
On Windows:
```bash
# Move into the newly created/cloned directory
cd PygameModelling23

# Create a new virtual environment in the folder venv
# it can happen that you need to use python or python3.x instead of python3 according to
# your installation where x is your python's minor version. It can happen that you have to
# use the "py" command instead of the python/python3 commands.
py -m venv .\venv

# Activate the virtual environment
.\venv\Scripts\activate.bat
```

7. **Install jupyter notebook**: We collected the tasks and related information into a jupyter notebook. To be able to use it install jupyter inside the virtual environment then open jupyter notebook.

```bash
pip install jupyter
jupyter notebook
```

8. **Open the provided notebook**: Then open the `InstallAndTest.ipynb` from the user interface of jupyter and run the cells in the notebook. This will install all dependencies in your virtual environment and test if the installation was successful. After running the last cell you should see a short simulation of randomly moving agents implemented in pygame. (Note that we suppose you have opened juptyer from the folder of the code base. This is important when you run the cells of the installation notebook)

**At this point you are ready for the workshop! Happy coding!**

### 3. During the Workshop
1. You will have to start by activating your `venv` you have created during the preparation and start `jupyter` inside. Don't forget to replace the path in the command to the path where you have cloned the repo.

On Linux/MacOS:
```bash
# Move into the created/cloned directory
cd path/to/cloned/repo/PygameModelling23

# Activate the virtual environment
source ./venv/bin/activate

# Start jupyter notebook
jupyter notebook
```

On Windows:
```bash
# Move into the newly created/cloned directory
cd path\to\cloned\repo\PygameModelling23

# Activate the virtual environment
.\venv\Scripts\activate.bat

# start jupyter notebook
jupyter notebook
```
2. From the user interface of jupyter open the provided course track notebooks starting with `Track1...` and `Track2...`.
3. Follow the instructions in the notebook and enjoy the workshop!
