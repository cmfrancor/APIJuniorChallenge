
  @smoke @regression
  Feature: Users creations and registration

    @users
    Scenario: Verify creating random user with 'POST /users' creates a new user,
    after that update it with 'PUT /users/{id}'

      Given I call the '/users' users api to 'create'
      When I review the response body, status,and headers
      Then the status should be '201'
      And I call the '/users' users api to 'update'
      And I review the response body, status,and headers
      And the status should be '200'


    @register
    Scenario: Verify 'POST /register' creates a new user and 'GET /users/{id}'
    get a information about the user you just created

      Given I call the '/register' register api with 'valid' email and 'valid' password
      When I review the response body, status,and headers
      Then the status should be '200'
      And I call the '/users/' api with the last created user
      And I review the response body, status,and headers
      And the status should be '200'
      And the response body should have the name and job of the created user

      @invalid_register
      Scenario Outline: Verify 'POST /register' shows error message when creating a user with invalid data
        Given I call the '/register' register api with '<email_data>' email and '<password_data>' password
        When I review the response body, status,and headers
        Then the status should be '400'
        And the error should be '<error>'

        Examples:
      | email_data    | password_data| error                                        |
      | valid         | invalid      | Missing password                             |
      | invalid       | valid        | Note: Only defined users succeed registration|
      | invalid       | invalid      | Missing password                             |

