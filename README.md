

# Run Coverage

To generate a coverage html file:

```bash
coverage run manage.py test
coverage html
```

To omit certain files from html, run:

```bash
coverage html --omit="<filename>"
```