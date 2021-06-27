Feature: Test that login feature is working normally
  Scenario: User can log in and log out successfully with valid username and password
    Given I am on the login page
    When I enter valid username and password
    And I click Login button
    Then I am on dashboard page
    When I hover the cursor to profile dropdown menu
    And I click Logout button
    Then I am on login page
    And I see logout message in message box

  Scenario: User can not log in with non-existing username and existing password
    Given I am on the login page
    When I enter non-existing username and existing password
    And I click Login button
    Then I am still on the login page
    And I see incorrect username or password message in message box
    But I might also be on security check page

  Scenario: User can not log in with existing username and non-existing password
    Given I am on the login page
    When I enter existing username and non-existing password
    And I click Login button
    Then I am still on the login page
    And I see incorrect username or password message in message box
    But I might also be on security check page

  Scenario: User can not log in with non-existing username and non-existing password
    Given I am on the login page
    When I enter non-existing username and non-existing password
    And I click Login button
    Then I am still on the login page
    And I see incorrect username or password message in message box
    But I might also be on security check page

  Scenario: User can not log in with existing username and empty password
    Given I am on the login page
    When I enter existing username and empty password
    And I click Login button
    Then I am still on the login page
    And I see no password message in message box
    But I might also be on security check page

  Scenario: User can not log in with non-existing username and empty password
    Given I am on the login page
    When I enter non-existing username and empty password
    And I click Login button
    Then I am still on the login page
    And I see no password message in message box
    But I might also be on security check page

  Scenario: User can not log in with empty username and empty password
    Given I am on the login page
    When I enter empty username and empty password
    And I click Login button
    Then I am still on the login page
    And I see  no password message in message box
    But I might also be on security check page

  Scenario: User can not log in with empty username and existing password
    Given I am on the login page
    When I enter empty username and existing password
    And I click Login button
    Then I am still on the login page
    And I see no username message in message box
    But I might also be in security check page

  Scenario: User can not log in with empty username and non-existing password
    Given I am on the login page
    When I enter empty username and non-existing password
    And I click Login button
    Then I am still on the login page
    And I see no username message in message box
    But I might also be in security check page

  Scenario: Password field is marked and username field is not marked in login page
    Given I am on the login page
    When I enter a character in username field and a character in password field
    Then I can see the character in username field
    And I can only see a dot in password field

  Scenario: User can press enter key to log in successfully with valid username and password
    Given I am on the login page
    When I enter valid username and password
    And I press enter key
    Then I am on dashboard page

  Scenario: User is still on dash board page by clicking back button in browser after logging in to dashboard page
    Given I am on the login page
    When I enter valid username and password
    And I click Login button
    Then I am on dashboard page
    When I click back button in browser
    Then I am still on dashboard page

  Scenario: User is still on login page by clicking back button in browser after logging out to login page
    Given I am on the login page
    When I enter valid username and password
    And I click Login button
    Then I am on dashboard page
    When I hover the cursor to profile dropdown menu
    And I click Logout button
    Then I am on login page
    And I see logout message in message box
    When I click back button in browser
    Then I am still on login page

  Scenario: User can update password by clicking lost password link
    Given I am on the login page
    When I click lost password link
    Then I am on forget password page
    And I can enter email in the page
    And I can click send instructions button

  Scenario: User can log in successfully with valid email and password if email is changed to upper case
    Given I am on the login page
    When I enter valid email in upper case and valid password
    And I click Login button
    Then I am on dashboard page

  Scenario: User can not log in with valid username and password if password is changed to upper case
    Given I am on the login page
    When I enter valid username and changed password in upper case
    And I click Login button
    Then I am still on the login page
    And I see incorrect username or password message in message box
    But I might also be on security check page
