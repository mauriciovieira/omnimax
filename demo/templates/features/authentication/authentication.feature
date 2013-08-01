Feature: Rackspace Authentication (${language})
  This is a simple test to authenticate to Rackspace.
  
  % for tag in tags:
  @${tag}
  % endfor
  Scenario: Authenticate (${language})
    Given I am setup to run example code for ${language}
    When I execute the following code:
"""${language}
${solution}
"""
    Then the output should match
    """
    Authenticated
    """

