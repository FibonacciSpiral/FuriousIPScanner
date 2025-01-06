Listen up! Everything you need to know to get this project running on your PC is contained here!

1) Install miniconda by running the script for either windows or linux depending on your OS. If you have anaconda or miniconda installed already, please omit this step.
	* Note: If you use Anaconda rather than miniconda, you may end up with an environment that has far more packages than you need. This will result in a slower executable if you choose to create one from your main.py

2) After miniconda is installed, all you need to do is configure the environment. There is a file called environment.yml included here in this setup folder. Please open an anaconda prompt window. On windows, you click start and find Anaconda Prompt in your list of applications.
3) Once the window is open please type the following (you may pass in the full path to enviroment.yml by dragging and dropping the file into the prompt window):
	conda create -n furiousEnv --file environment.yml
4) Now you may activate the environment by typing:
	conda activate furiousEnv
5) Here is how to get pycharm configured:
	a) If you don't already have Pycharm, download it. Community addition is perfect.

	b) Open the project folder as a pycharm project.

	c) Navigate to File->Settings->Project: [Name of project]->Python Interpreter

	d) Now you must select the correct interpreter.

	e) To select the interpreter:
		* click Add Interpreter.
		* Then Add Local Interpreter. 
		* Click Conda Environment.
		* Click Use existing environment.
		* On the same line as Conda executable, you must navigate to the conda.bat file in miniconda. 
		* The path to your conda executable may be found simply by opening anaconda prompt and type this: where conda.bat
		* Keep in mind that anaconda prompt may have multiple environments. If you are asking it "where conda.bat", make sure you have completed step 4 that way conda knows what environment executable to look for.
		* Now you should be able to press the "Load Environments" button.
		* Now you should be able to see the name of the environment you made. Make sure you select that one.
		* Now press OK. You should see all the package information load without error.
		* Now the project should run without any error. If there are errors, ask someone for help.

6) Now that you have your environment configured, just remember to update the environment.yml if you add new python package dependencies.
	* Open miniconda prompt.
	* Make sure you are on furiousEnv by typing: conda activate furiousEnv
	* Use this command: conda env update --prefix ./env --file environment.yml  --prune

Now for some extras:

To create a brand new environment (for example if you are building a brand new project)
	1) Make sure miniconda is installed and open by following steps 1 and 2 from above.
	2) Type >conda create -n <environment name> python=3.10
		* Keep in mind you can specify whatever version of python you want! Try to keep it at the latest available though.
	3) Type >activate <environment name>

To add new packages to your environment:
	1) Open the Anaconda Prompt.
	2) Type >activate <environment name>
		* Example >activate furiousEnv
	3) Use pip install <package name>

To create a brand new environment.yml from scratch:
	1) Open the Anaconda Prompt.
	2) Type >activate <environment name>
		* Example >activate furiousEnv
	3) Type >conda env export > environment.yml
