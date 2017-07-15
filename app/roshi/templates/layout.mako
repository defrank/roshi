## layout.mako
<%!
    from datetime import datetime
%>
<!DOCTYPE html5>
<html lang="en">
    <head>
        <%block name="head">
            <meta charset="utf-8">
            <%block name="viewport">
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </%block>
            <title><%block name="title">${config['NAME'].title()}</%block></title>
            <%block name="seo">
                <meta name="description" content="">
                <meta name="author" content="">
            </%block>
            <%block name="include_css">
            </%block>
            <%block name="include_js">
            </%block>
        </%block>
    </head>

    <body>
        <header>
            <%block name="header" />
        </header>

        ${self.body()}

        <footer>
            <%block name="footer">
                <p>&copy; ${datetime.utcnow().year}</p>
            </%block>
        </footer>
    </body>
</html>
