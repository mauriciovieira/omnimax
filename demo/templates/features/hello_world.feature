Feature: Hello World (${language})
    This is a simple test to make sure the [Hello world program](http://en.wikipedia.org/wiki/Hello_world_program) works for the language of each SDK.
    It does not demonstrate the use of the SDK itself, but it does make sure the framework is able to successfully bootstrap the SDK, including finding a suitable
    tools (repl, compiler, whatever), running the dependency management tools (in bootstrap.sh) without errors, and finally execute the code.
  
  % for tag in tags:
  @${tag}
  % endfor
  Scenario: Hello World (${language})
    Given I am setup to run example code for ${language}
    When I execute the following code:
"""${language}
${solution}
"""
    Then the output should match
    """
    Hello, world!
    """

