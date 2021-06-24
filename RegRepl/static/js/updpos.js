let old_background

function open_for_upd(id) {

  old_background = ""
  $('.edit_frame').css('display', 'block')
  item = '/regrepl/item/upd/' + id
  $('#upd_frame').attr('src', item)
old_background =   $('#' + id).css('background')
  change_background(id, '#9dffa9')
  // $('#' + id).css('background', '#9dffa9')
  $('#' + id).css('box-shadow', '0px 0px 13px 0px black')
  $('#' + id)[0].scrollIntoView({behavior: "smooth"})



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





  $('#upd_frame').contents().find('form').submit()

  $('#' + id).css('box-shadow', 'none')
  $('#' + id).css('background', background)
  $('#' + id).css('text-decoration', style)
  $('.edit_frame').css('display', 'none')
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
