from behave import when


@when("a Text is created")
def step_impl(context):
    raise NotImplementedError("STEP: When a Text is created")


@when('the Text has name "{name}"')
def step_impl(context, name):
    raise NotImplementedError('STEP: When the Text has name "test Text"')
