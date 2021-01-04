# flask-project-templetes 

Using HTML to the same file(templetes.py) is not cool.Consider how complex the code in this view function will become when use similar HTML again and again for different files. This is clearly not an option that will scale as the application grows.

Templates help achieve this separation between presentation and business logic. In Flask, templates are written as separate files, stored in a templates folder that is inside the application package.

>>> <html>
    <head>
        <title>{{ title }} - Littleblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>

We start working on the templates.If make requests with the app running, you will get an exception that Flask cannot find the templates. The templates are using #Jinja2 syntax and have autoescaping enabled by default. This means that unless we mark a value in the code with #Markup or with the |safe filter in the template, Jinja2 will ensure that special characters such as < or > are escaped with their XML equivalents.

We are also using template inheritance which makes it possible to reuse the layout of the website in all pages.

Put the templates into the templates folder.


## jinja
A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). A Jinja template doesn’t need to have a specific extension: .html, .xml, or any other extension is just fine.

A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:

```
{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
#  ... ## for Line Statements
```


#here using conditonal statement and for loops:

>>> <html>
    <head>
        {% if title %}
        <title>{{ title }} - Littleblog</title>
        {% else %}
        <title>Welcome to Littleblog!</title>
        {% endif %}
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
        {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
        {% endfor %}
    </body>
</html>

## markup
Convert the characters &, <, >, ‘, and ” in string s to HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML. Marks return value as markup string.

```
>>> Markup('Hello, <em>World</em>!')
Markup('Hello, <em>World</em>!')

>>> Markup(42)
Markup('42')

>>> Markup.escape('Hello, <em>World</em>!')
Markup('Hello &lt;em&gt;World&lt;/em&gt;!')

>>> class Foo:
    def __html__(self):
        return '<a href="/foo">foo</a>'
>>> Markup(Foo())
Markup('<a href="/foo">foo</a>')
```



# source: 
1. https://flask.palletsprojects.com/en/1.1.x/
2. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

# projects from 
https://blog.miguelgrinberg.com



