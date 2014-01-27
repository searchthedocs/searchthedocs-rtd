// Main Module for searchthedocs demo
define(function (require) {
  var _ = require('underscore');
  var Backbone = require('backbone');
  var $ = require('jquery');
    // The xdomainajax plugin is required if we wish to load content
    // from another domain.
  var xdomainajax = require('xdomainajax');
  var LocalContentView = require('stfd/local_content');
  var RemoteContentView = require('stfd/remote_content');
  var SearchRouter = require('stfd/router');
  var highlight_search_words = require('highlight_search_words');
  var display_hints = require('hint_display');

  // Create class map for view class lookup by string name.
  // Custom classes can be added here, then used in the search_options hash.
  // This also allows the search_options hash to remain pure data, allowing
  // dynamic configuration by the server.
  var class_map = {
    LocalContentView: LocalContentView,
    RemoteContentView: RemoteContentView
  }

  var searchthedocs_main = function() {

    var search_options = {
      default_endpoint: 'sections',
      endpoints: {
        sections: {
          content_view_class_string: 'LocalContentView',
          data_type: 'jsonp',
          default_params: {format: 'jsonp'},
          api_url: 'http://readthedocs.org/api/v2/search/section/',
          // API URL which is expected to return a list of all domains.
          domain_list_url: '/projects/search/autocomplete/',
          content_url_format:
            'http://{{domain}}.readthedocs.org/en/'
            + '{{version}}/{{path}}.html?highlight={{search}}#{{page_id}}',
          param_map: {
            search: 'q',
            domain: 'project'
          },
          result_format: {
            records_path: 'results.hits.hits',
            record_format: {
              // Fields used in sidebar display
              domain: 'fields.project',
              title: 'fields.title',
              content: 'fields.content',
              // Fields used to build record_url
              version: 'fields.version',
              path: 'fields.path',
              page_id: 'fields.page_id'
            },
            domain_facets_path: 'results.facets.project.terms',
            domain_facets_format: {
              domain: 'term',
            }

          },
      }
    }
  };

    window.search_router = new SearchRouter({
      container: '#searchthedocs-container',
      brand: 'searchthedocs',
      brand_href: '#',
      // This is used when linking to the full page of the content.
      content_link_text: 'See full page in project docs',
      search_options: search_options,
      class_map: class_map
    });

   Backbone.history.start({pushState: true});

   // Trigger highlight on content load.
   Backbone.on('content_loaded', function(doc_obj) {
     // Add the class to the content pane required for CSS scoping.
     $('.stfd-content-pane').addClass('rst-content');
     // Apply highlighig to wherever the search term appears in the content.
     if (doc_obj.search) {
        highlight_search_words(doc_obj.search);
     }
    });

   Backbone.on('view_loaded', function() {
     display_hints({
       'tracking_params': {
         'visit_number': 1,
       }
     });
   });

  };

  return searchthedocs_main;

});

