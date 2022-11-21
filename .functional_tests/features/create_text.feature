Feature: Creating a Text
    As a User with 0 Texts
    I want to create a Text
    So that I can view it later

    Scenario: Created Text should show in the list

        Given there are "0" Texts
        When a Text is created
        And the Text has name "test Text"
        Then there are "1" Texts
        And the Text will have name "test Text"