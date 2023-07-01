Scenario: User can add product to the cart
    Given Open Amazon page
    When Search for Corner Desk
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)