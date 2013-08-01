import subprocess
import StringIO


def execute_file(script, wrapper=None, cwd=None):
    print "About to execute %s" % script
    args = [wrapper, script]
    args = [x for x in args if x is not None]
    p = subprocess.Popen(args, cwd=cwd,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         stdin=subprocess.PIPE)
    captured_output = StringIO.StringIO()
    for line in iter(p.stdout.readline, b''):
        print(">>> " + line.rstrip())
        print >>captured_output, line
    output = captured_output.getvalue()
    captured_output.close()
    return output


def execute(executable, exec_input, cwd=None):
    p = subprocess.Popen([executable], cwd=cwd,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         stdin=subprocess.PIPE)
    return p.communicate(exec_input)[0]
