from behave import then
import json


@then('there are "{count}" Texts')
def step_impl(context, count):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(len(json.loads(res.content)), int(count))


@then('the Text will have name "{name}"')
def step_impl(context, name):
    res = context.test.client.get("/api/texts/")
    obj = json.loads(res.content)
    context.test.assertEqual(obj[0].name, name)


@then('the Text has body "{body}"')
def step_impl(context, body):
    res = context.test.client.get("/api/texts/")
    obj = json.loads(res.content)
    context.test.assertEqual(obj[0].body, body)
