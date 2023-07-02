Feature: Test Scenarios for Sign In

  Scenario: User sees sign in page
    Given Open Amazon page
    When Click Orders
    Then Verify Sign In page opens


Scenario: Sign in page can be opened from SignIn popup
  Given Open Amazon page
  When Click on button from Signin popup
  Then Verify Sign In page opens