// Developer RequireJS configuration.

// Summary of third-party packages:
// RequireJS for module management
// Underscore for utilities
// jQuery for DOM manipulation
// Handlebars for templating
// Backbone for Models, Collections, and Views

// Define the paths to modules and shim non-AMD modules.
/*global require:true */
require.config({
    baseUrl: "/static",
    paths: {
      'text': 'vendor/require/text',
      'underscore': 'vendor/underscore/underscore',
      'jquery': 'vendor/jquery/jquery',
      'handlebars': 'vendor/handlebars/handlebars',
      'backbone': 'vendor/backbone/backbone',
      'bootstrap': 'vendor/bootstrap/js/bootstrap',
      'xdomainajax': 'vendor/xdomainajax/jquery.xdomainajax',
      'stfd': 'searchthedocs/src'
    },
    shim: {
        'underscore': {
            exports: '_'
        },
        'jquery': {
          exports: '$'
        },
        'handlebars': {
          exports: 'Handlebars'
        },
        'backbone': {
            deps: ['underscore', 'jquery'],
            //Once loaded, use the global 'Backbone' as the module value.
            exports: 'Backbone'
        },
        'bootstrap': {
            deps: ['jquery']
        },
        'xdomainajax': {
            deps: ['jquery']
        }
    }
});

