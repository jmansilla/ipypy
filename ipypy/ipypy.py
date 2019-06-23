from copy import deepcopy
import json

from notebook.services.contents.filemanager import FileContentsManager


class IpypyManager(FileContentsManager):
    """
    ContentsManager that persists to a pure python file.
    """
    def guess_type(self, path, allow_directory=True):
        """
        Guess the type of a file.
        If allow_directory is False, don't consider the possibility that the
        file is a directory.
        """
        if path.endswith('.ipynb'):
            return 'notebook'
        elif allow_directory and self.dir_exists(path):
            return 'directory'
        else:
            return 'file'

    def _get_outputs_uri(self, path):
        return path + '.nboutputs'

    def _split_model(self, model):
        shallow_model = deepcopy(model)
        print(shallow_model.keys())
        outputs = {'type': 'file', 'format': 'text', 'content': {}}
        prefix = 'shasha'
        for i, cell in enumerate(shallow_model['content']['cells']):
            if not cell.get('outputs', []):
                continue
            key = f'{prefix}-{i}'
            outputs['content'][key] = cell['outputs']
            cell['outputs'] = [{'id': key, 'output_type': 'external'}]
        
        outputs['content'] = json.dumps(
            outputs['content'], sort_keys=True, indent=4)
        return shallow_model, outputs

    def _merge_model(self, shallow_model, outputs_model):
        model = deepcopy(shallow_model)
        outputs = json.loads(outputs_model.get('content', '{}'))
        for cell in model['content']['cells']:
            if not cell['outputs']:
                continue
            if cell['outputs'][0]['output_type'] != 'external':
                continue
            key = cell['outputs'][0]['id']
            cell['outputs'] = outputs.get(key, [])
        return model

    def save(self, model, path):
        """Save a file or directory model to path."""
        _type = self.guess_type(path)
        if _type != 'notebook':
            return super().save(model, path)
        else:
            shallow_model, outputs = self._split_model(model)
            super().save(outputs, self._get_outputs_uri(path))
            return super().save(shallow_model, path)

    def get(self, path, content=True, type=None, format=None):
        """Get a file or directory model."""
        result = super().get(path, content, type, format)
        if type is None:
            type = self.guess_type(path)
        if type != 'notebook':
            return result
        if content:
            # look for the outputs file
            outputs_uri = self._get_outputs_uri(path)
            if self.file_exists(outputs_uri):
                outputs_data = self.get(outputs_uri, True, 'file')
                result = self._merge_model(result, outputs_data)
        
        return result

    def is_hidden(self, path):
        """Is path a hidden directory or file?"""
        if path.endswith('.ipynb.db'):
            print('hide path', path)
            return True
        return super().is_hidden(path)
