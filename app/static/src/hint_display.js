define(function(require) {
  var _ = require('underscore');
  var $ = require('jquery');
  require('bootstrap');
  var hint_rules = require('hint_rules');

  window.hints_shown_this_session = [];

  var check_hint_rules = function(tracking_params) {
    var hints = {};

    // Check each hint rule, and if the hint rule matches, push the hint
    // meta into the hints array.
    _.each(hint_rules, function(hint_rule, hint_name) {
      var hint_meta = hint_rule(tracking_params);
      if (hint_meta) {
        hints[hint_name] = hint_meta;
      }
    });

    return hints;
  };

  var display_hints = function(options) {
    var tracking_params = options.tracking_params;
    hints_meta = check_hint_rules(tracking_params);

    // Apply display rules for every matching hint.
    _.each(hints_meta, function(hint_meta, hint_name) {

      // Don't show same hint more than once in session
      if (!_.contains(hints_shown_this_session, hint_name)) {


        var $el = $(hint_meta.el);
        // Invoke the "hint_type" (tooltip, etc) method on the selected el.
        // Pass the hint options to the method.
        if (hint_meta.hint_method === 'tooltip') {

          setTimeout(function() {
            hints_shown_this_session.push(hint_name);
            $el.tooltip(hint_meta.hint_options);
            $el.tooltip('show');
          }, 100);

          Backbone.on(hint_meta.remove_event, _.once(function() {
            $el.tooltip('destroy');
          }));
        } else if (hint_meta.hint_method === 'inline') {
          setTimeout(function() {
            hints_shown_this_session.push(hint_name);
            var hint_el = '<p class="tooltip-inner tooltip-inline">' + hint_meta.hint_options.title + '</p>';
            $(hint_el)
              .hide()
              .appendTo($el)
              .slideDown('slow');
          }, 100);

          Backbone.on(hint_meta.remove_event, _.once(function() {
            $hint_el.remove();
          }));
        }

      }
    });

  };

  var throttled_display_hints = _.debounce(display_hints, 500);

  return throttled_display_hints;

});

