$(document).ready(function() {
deps_get()
})

function open_for_add() {
  $(".newdep-frame").css('left', '0')
  $.getJSON('/getdirs/', (data) => {
      $.each(data, (i, val) => {
           $('#nd_frame').contents().find('#nd_dir').append('<option value="'+ val.id + '">' + val.name + '</option>')

})
  })
}

function nd_send_submit(){
  $(".newdep-frame").css('left', '-999px')
  $('#nd_frame').contents().find('form').submit()
  $('tbody').find('tr').remove()
  $('tbody').append("<tr><td colspan='2'>Данные загружаются ....</td></tr>")
  setTimeout(deps_get, 2000)

}

function nd_frame_cancelbtn(){
  $(".newdep-frame").css('left', '-999px')
}

function deps_get() {
  $('tbody').find('tr').remove()
$.getJSON('/getdeps/', (data) => {
    $.each(data, (i, val) => {
         $('tbody').append("<tr class='notcaption'><td>" + val.name + "</td><td>" + val.dirdepartament__name + "</td></tr>")

})
})
}
