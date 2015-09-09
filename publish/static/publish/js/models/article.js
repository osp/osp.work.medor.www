define([
    'underscore', 
    'backbone'
], function (_, backbone) {
    'use strict';

    var ArticleModel = Backbone.Model.extend({
        url : "/articles",
        idAttribute: '_id',
        defaults : {
            title: "Super cool",
            body: "<p>Hello world</p>",
        }
    });

    return ArticleModel;
});
