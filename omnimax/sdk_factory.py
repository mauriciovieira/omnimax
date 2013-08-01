import os
import omnimax.sdk


class SDKFactory(object):

    def __init__(self, fs=os):
        self.fs = fs
        self.sdks = fs.walk('sdks').next()[1]
        self.sdk_dict = dict(map(lambda x: [x, omnimax.sdk.BaseSDK(x)],
                                 self.sdks))

    def factory(self, language):
        return self.sdk_dict[language]
