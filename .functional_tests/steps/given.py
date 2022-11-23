from behave import given
import json

from content.tests.factory import TextFactory


@given("there are no Texts")
def step_impl(context):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(json.loads(res.content), [])


@given('there is a Text with name "{name}" and body "{body}"')
def step_impl(context, name, body):
    TextFactory(name=name, body=body)
