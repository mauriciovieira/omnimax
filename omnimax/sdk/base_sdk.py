import os
from omnimax.execute import execute, execute_file


class BaseSDK(object):

    def __init__(self, identifier):
        self.identifier = identifier
        self.sdk_path = os.path.join(os.getcwd(), 'sdks', self.identifier)

    def bootstrap(self):
        print execute_file(os.path.join(os.getcwd(), self.sdk_path, 'bootstrap.sh'),
                           cwd=self.sdk_path, wrapper='bash')

    def run(self, srccode):
        wrapper = os.path.join(self.sdk_path, 'run.sh')
        return execute(wrapper, srccode, cwd=self.sdk_path)
