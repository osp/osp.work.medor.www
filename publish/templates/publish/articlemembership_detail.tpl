<!DOCTYPE HTML>
<html lang="en" class="normal">
<head>
    <meta charset="utf-8">
    <title>{{ object.article.title }}</title>

    <link rel="stylesheet" href="../../css/main.less" type="text/less">
    <link rel="stylesheet" href="css/generated.css">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- PAGES -->
    <div id="pages">
        {% load publish_tags %}
        {% for i in object.page_number|times %}
        <!-- Page {{ i }} -->
        <div id="page-{{ i }}" class="paper">
            <div class="page">
                <div class="header"></div>

                <div class="body recipient"></div>

                <div class="footer"></div>
            </div>
        </div>
        {% endfor %}
    </div>

    <div id="stories">
        <article id="flow-{{ object.article.slug }}" data-src="https://{{ request.get_host }}{% url 'article-membership-detail-html' object.id %}"></article>
    </div>

    <!-- JAVASCRIPT -->
    <script src="../../vendors/less/dist/less.min.js"></script>
    <script src="../../js/stories.js"></script>
</body>
</html>
