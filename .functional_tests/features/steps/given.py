from behave import given


@given('there are "{count}" Texts')
def step_impl(context, count):
    res = context.test.client.get("/texts/")
    context.test.assertEqual(len(res.content), count)
