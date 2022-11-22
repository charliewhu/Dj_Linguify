from behave import given
import json


@given("there are no Texts")
def step_impl(context):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(json.loads(res.content), [])
