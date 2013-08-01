import difflib
from behave import *


@then(u'the output should match')
def impl(context):
    expected = str(context.text).strip()
    actual = context.output.strip()
    diff = difflib.ndiff(actual.splitlines(), expected.splitlines())
    assert_message = "Output did not match expected.  Diff:\n" + "\n".join(list(diff))
    assert actual == expected, assert_message
