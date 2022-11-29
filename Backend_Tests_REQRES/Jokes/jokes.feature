
  @smoke @regression
  Feature: Verify Jokes module

    @jokes
    Scenario: Verify 'POST /jokes-parade/' creates a new joke

      Given I call the '/jokes-parade/' api
      When I review the response body, status,and headers
      Then I should see status '201' created
      And the response body should be in accordance with the created data