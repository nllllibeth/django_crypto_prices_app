setTimeout(function() {
    var el = $('#container');
    el.html('<div class="container"></div>');
    onLoad(el);
  }, 2000);
  
  function onLoad(element) {
    $(element).addClass('loaded');
  }