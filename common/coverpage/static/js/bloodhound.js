
var states = new Bloodhound({
  remote: '/search/autocomplete/?q=%QUERY',
  datumTokenizer: function(d) {
    return Bloodhound.tokenizers.whitespace(d.value);
  },
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  limit: 15
});

// kicks off the loading/processing of `local` and `prefetch`
states.initialize();

$('#bloodhound .typeahead').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'states',
  displayKey: 'value',
  // `ttAdapter` wraps the suggestion engine in an adapter that                                        
  // is compatible with the typeahead jQuery plugin
  source: states.ttAdapter()
});


$('#search_input').bind('typeahead:selected', function(obj, datum, name) {      
  $("form").submit();
});
