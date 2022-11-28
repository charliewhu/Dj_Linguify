from behave import then
import json


@then('there are "{count}" Texts')
def step_impl(context, count):
    res = context.test.client.get("/api/texts/")

    context.test.assertEqual(len(res.data), int(count))


@then('there are "{count}" Words')
def step_impl(context, count):
    res = context.test.client.get("/api/words/")

    context.test.assertEqual(len(res.data), int(count))


@then('the Text has body "{body}"')
def step_impl(context, body):
    res = context.test.client.get("/api/texts/")

    context.test.assertEqual(res.data[0].get("body"), body)


@then('the Text will have name "{name}"')
def step_impl(context, name):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(res.data[0].get("name"), name)


@then('the Word will have status = "{status}"')
def step_impl(context, status):
    url = "/api/words/1/"
    res = context.test.client.get(url)

    context.test.assertEqual(res.data.get("status"), status)


@then('the Texts related Words have "{attr}" attribute')
def step_impl(context, attr):
    raise NotImplementedError('STEP: Then the Texts related Words have "id" attribute')
