define(function(require) {
  var _ = require('underscore');
  var $ = require('jquery');
  require('bootstrap');
  var hint_rules = require('hint_rules');

  window.hints_shown_this_session = [];

  var check_hint_rules = function(options) {
    var hints = {};

    // Check each hint rule, and if the hint rule matches, push the hint
    // meta into the hints array.
    _.each(hint_rules, function(hint_rule, hint_name) {
      var hint_meta = hint_rule(options);
      if (hint_meta) {
        hints[hint_name] = hint_meta;
      }
    });

    return hints;
  };

  var display_hints = function(options) {
    console.log(options);
    hints_meta = check_hint_rules(options);

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

          Backbone.on(hint_meta.success_event, _.once(function() {
            $el.tooltip('destroy');
          }));
        } else if (hint_meta.hint_method === 'inline') {
          var hint_el = '<p class="tooltip-inner tooltip-inline">'
            + hint_meta.hint_options.title + '</p>';
          $hint_el = $(hint_el);
          setTimeout(function() {
            hints_shown_this_session.push(hint_name);
            $hint_el
              .hide()
              .insertAfter($el)
              .slideDown('slow');
          }, 100);

          Backbone.on(hint_meta.hide_event, function(search_obj) {
            // If there are no domains matching the stem, hide this event
            // until that condition becomes true again.
            console.log(search_obj);
            if (!search_obj.domains_matching_stem.length > 0) {
              // Remove the hint from the set of shown hints, since we should
              // be able to show it again.
              hints_shown_this_session = _.without(
                hints_shown_this_session,
                hint_name
              );
              $hint_el.remove();
            }
          });

          Backbone.on(hint_meta.success_event, _.once(function() {
            $hint_el.remove();
          }));
        }

      }
    });

  };

  var throttled_display_hints = _.debounce(display_hints, 500);

  return throttled_display_hints;

});

