$(document).ready(function() {
subdeps_get()
})

function open_for_add() {
  $(".newsubdep-frame").css('left', '0')
  $.getJSON('/getdeps/', (data) => {
      $.each(data, (i, val) => {
           $('#nsd_frame').contents().find('#nsd_dep').append('<option value="'+ val.id + '">' + val.name + "/" + val.dirdepartament__name +  '</option>')

})
  })
}

function nsd_send_submit(){
  $(".newsubdep-frame").css('left', '-999px')
  $('#nsd_frame').contents().find('form').submit()
  $('tbody').find('tr').remove()
  $('tbody').append("<tr><td colspan='2'>Данные загружаются ....</td></tr>")
  setTimeout(subdeps_get, 2000)

}

function nsd_frame_cancelbtn(){
  $(".newsubdep-frame").css('left', '-999px')
}

function subdeps_get() {
  $('tbody').find('tr').remove()
$.getJSON('/getsubdeps/', (data) => {
    $.each(data, (i, val) => {
         $('tbody').append("<tr class='notcaption'><td>" + val.name + "</td><td>" + val.departament__name + "</td></tr>")

})
})
}
