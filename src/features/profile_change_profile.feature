@android
Feature: Change User Profile User
  In order to personalize my profile
  As a regular app user
  I want to change my personal data in the app

  @camera
  Scenario: Change User Photo at Profile Page
    Given user is at Profile Page
    When user takes a picture with the device camera
    Then Account Page is shown
    And small picture is shown next to the name

  @names
  Scenario Outline: Change First and Last Name at Profile Page
    Given user is at Profile Page
    When user changes first name with <first_name>, last name with <last_name> and taps Done button
    Then Account Page is shown
    And old name was changed with <first_name> <last_name>
    Examples:
      | first_name | last_name |
      | Ana        | Garcia    |