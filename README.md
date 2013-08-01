omnimax
=======

Omnimax is an experimental framework that aims to make creating [living
documentation](https://www.relishapp.com/relish/relish/docs/living-documentation) easy for any SDK or framework.  It can
be used for a single tool, but Omnimax primarily targeted at SDKs that have been ported to several languages or frameworks.  It will turn merge generic documentation with framework-specific sample code.  The hope is that this will help generate a comparison between ports (e.g.: a report showing which features are implemented by each port), and also help ensure that important high-level features have a test, documentation, and sample code.

Omnimax is still new and highly experimental, so as long as the version for now please remember the [Semantic Versioning
Specification](http://semver.org/):
> Major version zero (0.y.z) is for initial development. Anything may change at any time.

Usage
====
See demo/ for some samples.  The results are published to https://relishapp.com/maxlinc/omnimax/docs.  The CI server is
not currently public.

In order to setup an SDK:

* pip install omnimax
* Create an sdks/ folder.
* Create a folder for each sdk you wish to include.
* Create a bootstrap.sh for each SDK which handles dependency management (e.g.: pip, bundler, npm) or other setup.
* Create a run.sh for each SDK that accepts code via stdin and then executes it within the SDK.

Create tests/documentation:

* Create templates/features/*.feature
* Create a [Mako templates](http://www.makotemplates.org/) to generate a Gherkin-style feature file (specifically [Behave](http://pythonhosted.org/behave/)).  Currently these variables are available:
    * language: will be replaced with the name of the SDK (detected from the folder name)
    * tags: adds tags that apply to the feature.  Currently just the language name, but tags will be detected from other sources (like features.yaml) in the future.
    * solution: this is replaced with the solution code for the SDK.

Adding sample code to create complete a test:

* Create a solutions/ folder within your SDK.
* Create a file based on the test you are implementing.  Maintain the same relative path as the feature file, just replacing the file suffix. For example, templates/features/my_feature_group/my_feature.feature may become sdks/my_ruby_framework/solutions/my_feature_groups/my_feature.rb.

Execution
=========

You can perform a few actions via the omnimax-cli.py binary distributed with the python egg.  This includes:

* test: merges the templates/samples and uses behave to run the resulting feature files.
* publish: merges the templates/samples and publishes documentation to relishapp.com based on the feature files.
* matrix: generates a matrix from features.yaml to generate a feature matrix comparing the SDKs
generate: merges the templates/samples to BDD files

All of the commands except the generate command merge the templates into a temporary directory which is removed when the command finishes.  Generate does not clean up the temporary directory.