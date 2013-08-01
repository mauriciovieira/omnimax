#!/usr/bin/env python
import sys
import argparse
import omnimax
import os
import subprocess
import tempfile
import shutil
import yaml
from mako.template import Template


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="the omnimax command to run.")
    parser.add_argument("--debug", help="run the tests in debug mode", action='store_true')
    parser.add_argument("--tags", help="run the tests with these tags")
    parser.add_argument("--behave_opts", help="additional arguments to pass to the behave test runner")
    parser.add_argument("--relish_proj", help="name of the relishapp.com project for publishing documentaiton")
    args = parser.parse_args()
    if args.command == 'matrix':
        matrix(args)
    elif args.command == 'generate':
        generate(args)
    elif args.command == 'test':
        test(args)
    elif args.command == 'publish':
        publish(args)
    else:
        print "Unknown command"
        parser.print_help()
        sys.exit(os.EX_USAGE)


class StatusReport(object):

    def __init__(self, output, yaml, sdks):
        self.output = output
        self.yaml = yaml
        self.sdks = sdks

    def report(self):
        output = self.output
        self.write_header()
        for group_name, group in self.yaml['feature_groups'].iteritems():
            for feature in group['features']:
                self.write_feature(group_name, feature)
        output.flush()
        output.close()

    def write_header(self):
        output = self.output
        header_list = ['Product', 'Feature'] + self.sdks
        header_dashes = map(lambda x: '-', self.sdks)
        line1 = '|'.join(header_list)
        line2 = '|'.join(header_dashes)
        print >>output, line1
        print >>output, line2

    def write_feature(self, feature_group, feature):
        output = self.output
        output.write(feature_group + '|')
        output.write(feature + '|')
        status = map(lambda x: self.determine_status(
            feature_group, feature, x), self.sdks)
        # status = map(lambda x: x, self.sdks)
        status_data = '|'.join(status)
        print >>output, status_data

    def determine_status(self, feature_group, feature, sdk):
        # Just claimed status right no - no status based on test results
        try:
            feature_data = self.yaml['feature_groups'][
                feature_group]['features'][feature]
            if feature_data is None:
                return ''
            if sdk in feature_data['done']:
                return ' - '.join(['Done', feature_data['comments'][sdk]])
            else:
                return ''
        except Exception as e:
            raise e


def matrix(args):
    sdks = omnimax.SDKFactory().sdks
    feature_data = open('features.yaml', 'r').read()
    features = yaml.load(feature_data)
    output_file = 'features/readme.md'
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    output = open(output_file, 'w')
    report = StatusReport(output, features, sdks)
    report.report()
    print output_file + " generated!"


def generate(args):
    tmpdir = tempfile.mkdtemp()
    features_dir = os.path.join(tmpdir, 'features')
    steps_dir = os.path.join(features_dir, 'steps')

    os.mkdir(features_dir)
    render_features('sdks', features_dir, 'templates/features')
    # copy_relative('features', features_dir)
    copy_relative('steps', steps_dir)
    print "Temporary test directory: %s" % features_dir
    return [tmpdir, features_dir]


def publish(args):
    tmpdir, features_dir = generate(args)
    try:
        print "Publishing documentation to relish"
        command = "pushd " + tmpdir + "; relish push " + args.relish_proj + "; popd"
        print "Executing %s" % command
        subprocess.call(command, shell=True)
    finally:
        shutil.rmtree(tmpdir)


def test(args):
    tmpdir, features_dir = generate(args)

    try:
        print "Beginning tests..."
        command_args = ['behave']
        if args.debug:
            command_args.extend(['--format plain', '--no-capture'])
        if args.tags:
            command_args.extend(['--tags ' + args.tags])
        if args.behave_opts:
            command_args.extend([args.behave_opts])
        command_args.append(features_dir)
        print "Executing: %s" % ' '.join(command_args)
        subprocess.call(" ".join(command_args), shell=True)
    finally:
        shutil.rmtree(tmpdir)


def render_features(src, target, templateDir):
    sdks = omnimax.SDKFactory().sdks
    for sdk in sdks:
        solution_root = os.path.join(src, sdk, 'solutions')
        solutions = find_solution_files(solution_root)
        templates = map(lambda x: template_for_solution(x, solution_root, templateDir, sdk), solutions)
        for i in range(len(solutions)):
            template = Template(filename=templates[i])
            solution_src = open(solutions[i], 'r').read()
            output = template.render(language=sdk, solution=solution_src, tags=[sdk])
            output_filename = os.path.basename(templates[i]).replace('.feature', '_' + sdk + '.feature')
            output_file = os.path.join(target, output_filename)
            open(output_file, 'w').write(output)


def template_for_solution(solution_file, srcroot, targetroot, sdk):
    template_file = os.path.splitext(solution_file)[0].replace(srcroot, targetroot)
    return template_file + '.feature'


def find_solution_files(rootdir):
    fileList = []
    for root, subFolders, files in os.walk(rootdir):
        for f in files:
            fileList.append(os.path.join(root, f))
    return fileList


def copy_relative(src, target):
    src = os.path.join(os.getcwd(), src)
    print "Copying %(src)s to %(target)s" % {'src': src, 'target': target}
    shutil.copytree(src, target)


if __name__ == "__main__":
    main(sys.argv[1:])
