Feature: login HRM
  Scenario Outline: utline: login to hrm with parameter
    Given lunch chrome
    When open url
    And enter username '<username>' and password '<password>'
    And click login button
    Then user should login

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 |  admin   |
      | admn     | amnam    |