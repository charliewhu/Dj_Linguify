from behave import then


@then('there are "{count}" Texts')
def step_impl(context, count):
    raise NotImplementedError('STEP: Then there are "1" Texts')


@then('the Text will have name "{name}"')
def step_impl(context, name):
    raise NotImplementedError('STEP: Then the Text will have name "test Text"')


@then('the Text has body "{body}"')
def step_impl(context, body):
    raise NotImplementedError('STEP: Then the Text has body "test Text content"')
