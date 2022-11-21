from behave import given


@given('there are "{count}" Texts')
def step_impl(context, count):
    texts = Text.objects.count()
    context.test.assertEqual(texts, count)
