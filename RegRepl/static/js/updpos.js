let old_background
let change_place = false
let old_dep = ''
$(document).ready(function() {
// console.log(document.location.href.split('/'));
  if (document.location.href.split('/')[5] == 'upd') {
    $.getJSON('/getdirs/', (data) => {
        $.each(data, (i, val) => {
             $('#urp_dir').append('<option value="' + val.id + '">' + val.name + "</option>"  )
  })
    })

    $.getJSON('/getdeps/', (data) => {

        $.each(data, (i, val) => {
             $('#urp_dep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
  })
    })

    $.getJSON('/getsubdeps/', (data) => {

        $.each(data, (i, val) => {
             $('#urp_subdep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
    })
    })
  }
  else {
    $.getJSON('/getdirs/', (data) => {
        $.each(data, (i, val) => {
             $('#nrp_dir').append('<option value="' + val.id + '">' + val.name + "</option>"  )
             change_dir()
  })
    })
  }


})

function open_for_upd(id, rr_id) {
close_edit()

  query_url = '/regrepl/getdata/5/0/' + rr_id.toString()

  old_background = ""

  item = '/regrepl/item/upd/' + id
  $('#upd_frame').attr('src', item)
old_background =   $('#' + id).css('background')
  change_background(id, '#9dffa9')

  $('#' + id).css('box-shadow', '0px 0px 13px 0px black')
  $('#' + id)[0].scrollIntoView({behavior: "smooth"})

$('.edit_frame').css('display', 'block')
$.getJSON(query_url, (data) => {
  $.each(data, (i, val) => {
      if (val.id == id) {
          dir = val.dir_id
          dep = val.dep
          if (val.subdep) {
            subdep = val.subdep
          }
          else {
            subdep = 0
          }
      }
})


setTimeout(function(){
  set_workplace(dir, dep, subdep);
}, 1000);


})

console.log(change_place);
}

function set_workplace(dir, dep, subdep) {


  $('#upd_frame').contents().find('#urp_dir option').filter(function() {
    return ($(this).val() == dir); //To select Blue
  }).prop('selected', true);


    filter_deps(dir);

setTimeout(function(){
  $('#upd_frame').contents().find('#urp_dep option').filter(function() {
    return ($(this).val() == dep); //To select Blue
  }).prop('selected', true); }, 1000)


    filter_subdeps(dep);

setTimeout(function(){
  $('#upd_frame').contents().find('#urp_subdep option').filter(function() {
    return ($(this).val() == subdep); //To select Blue
  }).prop('selected', true);}, 1000)

setTimeout(function(){
old_dep = $('#upd_frame').contents().find('#urp_dep option:selected').text()
console.log(old_dep);}, 1000)



}

function free_position() {

  if ($('#id_free').prop('checked') == true) {
    $('#id_units_rr').val("0")
    $('#id_payment_rr').val("0")
    $('#id_level_rr').val("0")
      $('#id_salary_rr').val("0")
      $('#id_employer1').val("")
      $('#id_employer2').val("")
      $('#id_employer3').val("")
  }


}

function close_edit() {
  id_ = $('#upd_frame').attr('src')
  id = id_.split('/')[4]

  change_background(id, old_background)

  $('#' + id).css('box-shadow', 'none')
  $('.edit_frame').css('display', 'none')
}

function change_background(row_id, color) {
  $('#' + row_id).css('background', color)
}

function change_dir() {
  change_place = true
  if (document.location.href.split('/')[5] == 'upd') {

    $('#urp_dir').css('background','pink')
    filter_deps($('#urp_dir option:selected').val())
  }
  else {
  filter_deps($('#nrp_dir option:selected').val())}
}

function change_dep() {
  change_place = true
  if (document.location.href.split('/')[5] == 'upd') {

    console.log(change_place);
    // $('#urp_subdep').find('option').remove()
    $('#urp_dep').css('background','pink')
    filter_subdeps($('#urp_dep option:selected').val())
  }
  else {
  filter_subdeps($('#nrp_dep option:selected').val())
}
}

function change_subdep() {
  change_place = true
  $('#urp_subdep').css('background','pink')
}

function filter_deps(dir_id) {
 $('#nrp_dep').find('option').remove()
 $('#urp_dep').find('option').remove()
 $('#upd_frame').contents().find('#urp_dep').find('option').remove()

  $.getJSON('/getdeps/', (data) => {
    $.each(data, (i, val) => {

    if (val.dirdepartament__id == dir_id) {
      if (document.location.href.split('/')[5] == 'upd') {
          $('#urp_dep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
          }
      else {
        $('#nrp_dep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
      }
      if (document.location.href.split('/')[4] == 'create' || document.location.href.split('/')[4] == 'item') {
        $('#upd_frame').contents().find('#urp_dep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
      }
      else {
        $('#nrp_dep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
      }
    }

    })
  })
}

function filter_subdeps(dep_id) {
    console.log(dep_id);
  $('#nrp_subdep').find('option').remove()
    $('#urp_subdep').find('option').remove()
      $('#upd_frame').contents().find('#urp_subdep').find('option').remove()
    $('#urp_subdep').append('<option value="">НЕТ СЕКТОРА</option>')
    $('#nrp_subdep').append('<option value="">НЕТ СЕКТОРА</option>')
    $('#upd_frame').contents().find('#urp_subdep').append('<option value="">НЕТ СЕКТОРА</option>')

  $.getJSON('/getsubdeps/', (data) => {

      $.each(data, (i, val) => {

        if (val.departament__id == dep_id) {



          if (document.location.href.split('/')[5] == 'upd')  {


                  $('#urp_subdep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
             }
             else {
           $('#nrp_subdep').append('<option value="' + val.id + '">' + val.name + "</option>"  )  }
         }
        if (document.location.href.split('/')[4] == 'create' || document.location.href.split('/')[4] == 'item') {

            $('#upd_frame').contents().find('#urp_subdep').append('<option value="' + val.id + '">' + val.name + "</option>"  )
        }

             else {
           $('#nrp_subdep').append('<option value="' + val.id + '">' + val.name + "</option>"  )  }



})
  })
}

function send_submit() {

  id_ = $('#upd_frame').attr('src')
  id = id_.split('/')[4]

if ($('#upd_frame').contents().find('#id_free').prop('checked') == true) {
    background = 'yellow'
}
else {
    background = 'white'
}

if ($('#upd_frame').contents().find('#id_disabled').prop('checked') == true) {
    style = 'line-through'
}
else {
    style  = 'none'
}

  nname = $('#upd_frame').contents().find('#id_name').val()
  units = $('#upd_frame').contents().find('#id_units').val()
  level = $('#upd_frame').contents().find('#id_level').val()
  cat = $('#upd_frame').contents().find('#id_cat option:selected').text()
  payment = $('#upd_frame').contents().find('#id_payment').val()
  salary = $('#upd_frame').contents().find('#id_salary').val()
  dir = $('#upd_frame').contents().find('#urp_dir option:selected').text()
  dep = $('#upd_frame').contents().find('#urp_dep option:selected').text()
  subdep = $('#upd_frame').contents().find('#urp_subdep option:selected').text()
  units_rr = $('#upd_frame').contents().find('#id_units_rr').val()
  cat_rr = $('#upd_frame').contents().find('#id_cat_rr option:selected').text()
  payment_rr = $('#upd_frame').contents().find('#id_payment_rr').val()
  salary_rr = $('#upd_frame').contents().find('#id_salary_rr').val()
  employer1 = $('#upd_frame').contents().find('#id_employer1').val()
  employer2 = $('#upd_frame').contents().find('#id_employer2').val()
  employer3 = $('#upd_frame').contents().find('#id_employer3').val()
  $('#' + id).find('.pname').text(nname)
  $('#' + id).find('.units').text(units)
  $('#' + id).find('.level').text(level)
  $('#' + id).find('.cat').text(cat)
  $('#' + id).find('.payment').text(payment)
  $('#' + id).find('.salary').text(salary)
  $('#' + id).find('.cat_rr').text(cat_rr)

  $('#' + id).find('.units_rr').text(units_rr)
  $('#' + id).find('.payment_rr').text(payment_rr)
  $('#' + id).find('.salary_rr').text(salary_rr)
  $('#' + id).find('.employer1').text(employer1)
  $('#' + id).find('.employer2').text(employer2)
  $('#' + id).find('.employer3').text(employer3)

  if (old_dep != dep) {
        background = 'pink'
        $('#' + id).find('.comm').text('Был совершен перевод в: ' + dir + ' / ' + dep + ' / ' + subdep )
  }

// if (change_place == 1) {
//     background = 'pink'
//     $('#' + id).find('.comm').text('Был совершен перевод в: ' + dir + ' / ' + dep + ' / ' + subdep )
// }



  $('#upd_frame').contents().find('form').submit()

  $('#' + id).css('box-shadow', 'none')
  $('#' + id).css('background', background)
  $('#' + id).css('text-decoration', style)
  $('.edit_frame').css('display', 'none')
}
