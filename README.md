# ipypy

Store Jupyter Notebooks in a more repo and coding friendly way.

You can pick between a SplitCodeManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but with source information extracted)
  * my_file.ipypy (a pure code file that stores only the actual source code)

Or, a SplitOutputManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but without the cells output)
  * my_file.nbout (a json file that stores only the outputs of each cell)

This way, you can pay better attention to the actual code modifications of your notebooks while reviewing changes.

## Installation

    $ pip install ipypy

You will also need to configure your jupyter so it uses `ipypy`, by editing your jupyter config file, or from command line

    $ jupyter lab --NotebookApp.contents_manager_class="ipypy.SplitCodeManager"
