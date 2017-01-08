import os.path
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.files.base import ContentFile
from babeljs import transformer


class BabelStaticFileStorage(StaticFilesStorage):
    def _transform_js(self, content):
        return ContentFile(transformer.transform_string(content.read().decode()))

    def _save(self, name, content):
        if os.path.splitext(name)[1] == '.js':
            content = self._transform_js(content)
        return super(BabelStaticFileStorage, self)._save(name, content)
