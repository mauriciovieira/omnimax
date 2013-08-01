import os
import subprocess
from behave import *
import omnimax


@given(u'I am setup to run example code for {sdk_name}')
def step1(context, sdk_name):
    sdk = omnimax.SDKFactory().factory(sdk_name)
    context.sdk = sdk
    sdk.bootstrap()


@when('I execute the following code')
def step2(context):
    if os.environ.get('KATA_MODE') == 'true':
        if not hasattr(context, 'text'):
            test_name = context.feature.filename.split("features/", 1)[1]
            test_name = test_name.replace('_' + context.language, '')
            g = generator.Generator(context.language, test_name)
            g.kata()
    if os.environ.get('KATA_MODE') == 'shell':
        p = subprocess.Popen(['groovysh'], stdout=subprocess.PIPE)
        p.wait()
        context.output = p.stdout.read()
    else:
        assert hasattr(context, 'text') is True, 'No code'
        context.output = context.sdk.run(context.text)
    print context.output


@then('It should succeed')
def step3(context):
    assert True
