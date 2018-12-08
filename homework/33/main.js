$(clickMe).on('click', function() {
  let _$target = $(popover)
  if (_$target.toggleClass('show').hasClass('show')) {
    setTimeout(function() {
      $(document).one('click', function() {
        _$target.removeClass('show')
      })
    }, 0)
  }
})

popover.addEventListener('click', function(e){
  e.stopPropagation()
})
