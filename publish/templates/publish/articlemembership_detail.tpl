<!DOCTYPE HTML>
<html lang="fr" class="normal{% if object.is_even %} facing{% endif %}">
<head>
    <meta charset="utf-8">
    <title>{{ object.article.title }}</title>

    <link rel="stylesheet" href="../../css/main.less" type="text/less">
    <link rel="stylesheet" href="css/styles.less" type="text/less">
</head>
<body>
    <!-- PAGES -->
    <div id="pages">
        {% load publish_tags %}
        {% for i in object.page_number|times %}
        <!-- Page {{ i }} -->
        <div id="page-{{ i }}" class="paper">
            <div class="page">
                <div class="body flow-main"></div>
            </div>
        </div>
        {% endfor %}
    </div>

    <div id="stories">
        <article id="flow-main" data-src="../../stories/{{ object.article.slug }}.html"></article>
    </div>

    <!-- JAVASCRIPT -->
    <script src="../../vendors/less/dist/less.min.js"></script>
    <script src="../../js/stories.js"></script>
</body>
</html>
