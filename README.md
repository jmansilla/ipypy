# ipypy

Store Jupyter Notebooks in a more repo and coding friendly way.

You can pick between a SplitCodeManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but with source information extracted)
  * my_file.ipypy (a pure code file that stores only the actual source code)

Or, a SplitOutputManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but without the cells output)
  * my_file.nbout (a json file that stores only the outputs of each cell)

This way, you can pay better attention to the actual code modifications of your notebooks while reviewing changes.

## Benefits

* You can now import your notebook from another file
* You can now use standard coding tools and practices for manipulating code:
  * testing
  * editors
  * refactoring
  * ...
* The source code of your notebook, in a code versioning repository, now makes sense. It's code.
* You can choose to simply ignore the metadata files (.ipynb) in the repository, or keep them versioned. It's up to you.

## Warning

We are in beta. Once you open a notebook with this extension enabled, and later save it, your notebook will be saved in a format a bit incompatible.

## Installation

    $ pip install ipypy

You will also need to configure your jupyter so it uses `ipypy`, by editing your jupyter config file, or from command line

    $ jupyter lab --NotebookApp.contents_manager_class="ipypy.SplitCodeManager"
