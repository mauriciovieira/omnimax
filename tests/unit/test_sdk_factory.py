import omnimax
import os
import unittest
import fake_filesystem


class SDKFactoryTest(unittest.TestCase):

    def setUp(self):
        self.filesystem = fake_filesystem.FakeFilesystem()
        self.os_path = os.path
        sdk_dir = './sdks'
        self.sdks = ['java', 'rails', 'ruby', 'whatever']
        self.filesystem.CreateDirectory(sdk_dir)
        for sdk in self.sdks:
            self.filesystem.CreateDirectory(os.path.join(sdk_dir, sdk))
        self.os = fake_filesystem.FakeOsModule(self.filesystem)

    def tearDown(self):
        os.path = self.os_path

    def test_sdks(self):
        factory = omnimax.SDKFactory(self.os)
        self.assertEquals(factory.sdks, self.sdks)

    def test_factory_returns_basesdk(self):
        factory = omnimax.SDKFactory(self.os)
        sdk = factory.factory('java')
        self.assertEquals(type(sdk), omnimax.sdk.BaseSDK)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
