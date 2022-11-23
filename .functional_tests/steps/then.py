from behave import then
import json


@then('there are "{count}" Texts')
def step_impl(context, count):
    res = context.test.client.get("/api/texts/")
    obj = json.loads(res.content)

    context.test.assertEqual(len(obj), int(count))


@then('there are "{count}" Words')
def step_impl(context, count):
    res = context.test.client.get("/api/words/")
    obj = json.loads(res.content)

    context.test.assertEqual(len(obj), int(count))


@then('the Text has body "{body}"')
def step_impl(context, body):
    res = context.test.client.get("/api/texts/")
    obj = json.loads(res.content)
    print(obj)
    context.test.assertEqual(obj[0].get("body"), body)


@then('the Text will have name "{name}"')
def step_impl(context, name):
    res = context.test.client.get("/api/texts/")
    obj = json.loads(res.content)
    context.test.assertEqual(obj[0].get("name"), name)


@then('the Word will have status = "{status}"')
def step_impl(context, status):
    url = "/api/words/1/"
    res = context.test.client.get(url)
    obj = json.loads(res.content)

    context.test.assertEqual(obj.get("status"), status)
