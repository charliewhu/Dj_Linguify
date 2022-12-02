from behave import then


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


@then('the Words "{word1}" and "{word2}" are listed in the response')
def step_impl(context, word1, word2):
    words = [i["word"] for i in context.res]
    context.test.assertIn(word1, words)
    context.test.assertIn(word2, words)


@then('the Texts related Words have "{key}" key')
def step_impl(context, key):
    word_dict = context.res[0]
    context.test.assertIn(key, word_dict)
