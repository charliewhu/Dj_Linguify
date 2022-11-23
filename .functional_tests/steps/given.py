from behave import given
import json


@given("there are no Texts")
def step_impl(context):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(json.loads(res.content), [])


@given('there is a Text with name "{name}" and body "{body}"')
def step_impl(context, name, body):
    raise NotImplementedError(
        'STEP: Given there is a Text with name "test name" and body "test body"'
    )
