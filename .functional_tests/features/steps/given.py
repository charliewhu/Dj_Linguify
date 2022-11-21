from behave import given


@given("there are no Texts")
def step_impl(context):
    res = context.test.client.get("/api/texts/")
    context.test.assertEqual(res.content, [])
