from behave import when
import json


@when('a Text is posted with name "{name}" and body "{body}"')
def step_impl(context, name, body):
    url = "/api/texts/"
    res = context.test.client.post(url, {"name": name, "body": body})

    context.test.assertEqual(res.status_code, 201)


@when('the first Word "{word}" is tagged')
def step_impl(context, word):
    url = "/api/words/1/"
    res = context.test.client.put(url, {"name": word, "status": "Tagged"})

    context.test.assertEqual(res.status_code, 200)
