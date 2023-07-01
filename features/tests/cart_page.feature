Feature: Test Scenarios for Cart Empty

  Scenario: User see empty cart
    Given Open Amazon page
    When Open Cart page
    Then Verify cart has "0" item(s)