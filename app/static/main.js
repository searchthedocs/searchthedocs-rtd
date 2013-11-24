// Main Module for searchthedocs demo
define(function (require) {
  var _ = require('underscore'),
    $ = require('jquery'),
    // The xdomainajax plugin is required if we wish to load content
    // from another domain.
    xdomainajax = require('xdomainajax'),
    LocalContentView = require('stfd/local_content'),
    RemoteContentView = require('stfd/remote_content'),
    SearchTheDocsView = require('stfd/searchthedocs');

  var searchthedocs_main = function() {

    var search_options = {
      default_endpoint: 'sections',
      endpoints: {
        sections: {
          ContentViewClass: LocalContentView,
          data_type: 'jsonp',
          default_params: {format: 'jsonp'},
          api_url: 'http://readthedocs.org/api/v2/search/section/',
          content_url_format:
            'http://{{domain}}.readthedocs.org/en/'
            + '{{version}}/{{path}}.html#{{page_id}}',
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
            }
          },
      }
    }
  };

    window.searchtd = new SearchTheDocsView({
      brand: 'searchthedocs',
      brand_href: '#',
      search_options: search_options
    });

   $('#searchthedocs-container').append(searchtd.render().el);

  };

  return searchthedocs_main;

});

