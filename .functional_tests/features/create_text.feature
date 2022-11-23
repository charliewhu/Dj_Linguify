Feature: Creating a Text
    As a User with 0 Texts
    I want to create a Text
    So that I can view it later

    Scenario: Created Text should show in the list

        Given there are no Texts
        When a Text is posted with name "test name" and body "test Text content"
        Then there are "1" Texts
        And the Text has body "test Text content"
        And the Text will have name "test name"

    Scenario: Created Text should create Words

        Given there are no Texts
        When a Text is posted with name "test1" and body "test"
        And a Text is posted with name "test2" and body "test"
        Then there are "2" Texts
        And there are "1" Words