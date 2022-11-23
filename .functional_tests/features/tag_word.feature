Feature: Tagging a Word
    As a User with 1 Text
    I want to tag a Word
    So that my unknown Words are tagged for later

    Scenario: tagged Word should have status=Tagged

        Given there is a Text with name "test name" and body "test body"
        When the first Word "test" is tagged
        Then the Word will have status = "Tagged"