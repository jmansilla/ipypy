# ipypy

    Store Jupyter Notebooks in a more repo and coding friendly way.

Have you ever noticed that a Jupuyter Notebook nowadays is a json file? Containing together the metadata of the notebook itself, the list of cells, and for each cell, not only the *source* (what was written on it), but also the *outputs*, and *metadata* for each cell.

This project attemps to propose an alternative for that. 

## How

You can pick between a SplitCodeManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but with source information extracted)
  * my_file.ipypy (a pure code file that stores only the actual source code)

Or, a SplitOutputManager, which stores each notebook in:
  * my_file.ipynb (the usual notebook file, but without the cells output)
  * my_file.nbout (a json file that stores only the outputs of each cell)


## Benefits

* You can now import your notebook from another file
* You can now use standard coding tools and practices for manipulating Notebooks code:
  * testing
  * import code defined in there
  * editable naturally by any editor
  * refactoring
  * tracking changes
  * ...
* The source code of your notebook, can be versioned in a repository, where diffs, and history is readable. Now makes sense. It's code.
* (Work In Progress) You can choose to simply ignore the metadata files (.ipynb) in the repository, or keep them versioned. It should be up to you.

## Warning

We are in beta. Once you open a notebook with this extension enabled, and later save it, your notebook will be saved in a format a bit incompatible.

## Installation

    $ pip install ipypy

You will also need to configure your jupyter so it uses `ipypy`, by editing your jupyter config file, or from command line

    $ jupyter lab --NotebookApp.contents_manager_class="ipypy.SplitCodeManager"
