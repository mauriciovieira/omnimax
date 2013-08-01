import omnimax
import os
import unittest
from mock import MagicMock, patch


class BaseSDKTest(unittest.TestCase):
    def setUp(self):
        self.sdk_dir = os.getcwd() + '/sdks/ruby'

    def test_bootstrap(self):
        mock = MagicMock()
        with patch('omnimax.sdk.base_sdk.execute_file', mock):
            sdk = omnimax.sdk.BaseSDK('ruby')
            sdk.bootstrap()
        mock.assert_called_with(self.sdk_dir + '/bootstrap.sh', wrapper='bash', cwd=self.sdk_dir)

    def test_run(self):
        mock = MagicMock()
        code = "some SDK code"
        with patch('omnimax.sdk.base_sdk.execute', mock):
            sdk = omnimax.sdk.BaseSDK('ruby')
            sdk.run(code)
        mock.assert_called_with(self.sdk_dir + '/run.sh', code, cwd=self.sdk_dir)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
