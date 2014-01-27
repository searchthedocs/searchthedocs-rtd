define(function(require) {
  var _ = require('underscore');
  var $ = require('jquery');
  require('bootstrap');
  var hint_rules = require('hint_rules');

  var check_hint_rules = function(tracking_params) {
    var hints = [];

    // Check each hint rule, and if the hint rule matches, push the hint
    // meta into the hints array.
    _.each(hint_rules, function(hint_rule) {
      var hint_meta = hint_rule(tracking_params);
      if (hint_meta) {
        hints.push(hint_meta);
      }
    });

    return hints;
  };

  var display_hints = function(options) {
    var tracking_params = options.tracking_params;
    hints_meta = check_hint_rules(tracking_params);

    // Apply display rules for every matching hint.
    _.each(hints_meta, function(hint_meta) {
      var $el = $(hint_meta.el);
      // Invoke the "hint_type" (tooltip, etc) method on the selected el.
      // Pass the hint options to the method.
      $el[hint_meta.hint_method](hint_meta.hint_options);
      console.log(hint_meta)
      console.log($el)
      console.log($el[hint_meta.hint_method]);
      $el[hint_meta.hint_method](hint_meta.hint_options);
    });

  };

  return display_hints;

});

