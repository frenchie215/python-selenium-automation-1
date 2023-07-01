# Created by francesgibson at 2/23/23
Feature: Amazon search tests

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text matcha
    When Click on search button
    Then Verify that text "matcha" is shown




  Scenario: User can add product to the cart
    Given Open Amazon page
    When Input text Corner Office Desk
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    