Feature: Best seller tests

  Scenario: User can open Best Sellers page on Amazon
    Given Open Amazon page
    When Click on Hamburger icon
    When Click on Best Sellers link
    Then Verify that header has 5 links