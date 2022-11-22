from behave import when
import json


@when('a Text is posted with name "{name}" and body "{body}"')
def step_impl(context, name, body):
    url = "/api/texts/"
    res = context.test.client.post(url, {"body": body})
    context.test.assertEqual(res.status_code, 201)
