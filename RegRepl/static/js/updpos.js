function open_for_upd(id) {
  $('.edit_frame').css('display', 'block')
  item = '/regrepl/item/upd/' + id
  $('#upd_frame').attr('src', item)
  old_background = $('#' + id).css('background')
  $('#' + id).css('background', '#9dffa9')
}

// function save_item(id) {
// console.log(id);
// // nname = $('#upd_frame').contents().find('#id_name').val()
// nname = $('#id_name').val()
// console.log(nname);
// $('#' + id).find('.pname').text(nname)
// console.log($('#' + id).find('.pname').text());
// }

function send_submit() {
  id_ = $('#upd_frame').attr('src')
  id = id_.split('/')[4]
  console.log(id);
  nname = $('#upd_frame').contents().find('#id_name').val()
  units = $('#upd_frame').contents().find('#id_units').val()
  level = $('#upd_frame').contents().find('#id_level').val()
  cat = $('#upd_frame').contents().find('#id_cat option:selected').text()
  payment = $('#upd_frame').contents().find('#id_payment').val()
  salary = $('#upd_frame').contents().find('#id_salary').val()
  units_rr = $('#upd_frame').contents().find('#id_units_rr').val()
  cat_rr = $('#upd_frame').contents().find('#id_cat_rr option:selected').text()
  console.log(cat_rr);
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
  console.log($('#' + id).find('.cat_rr').text());
  $('#' + id).find('.units_rr').text(units_rr)
  $('#' + id).find('.payment_rr').text(payment_rr)
  $('#' + id).find('.salary_rr').text(salary_rr)
  $('#' + id).find('.employer1').text(employer1)
  $('#' + id).find('.employer2').text(employer2)
  $('#' + id).find('.employer3').text(employer3)



  $('#upd_frame').contents().find('form').submit()
  $('#' + id).css('background', 'white')
  $('.edit_frame').css('display', 'none')
}

function close_edit() {
  id_ = $('#upd_frame').attr('src')
  id = id_.split('/')[4]
  $('#' + id).css('background', 'white')
  $('.edit_frame').css('display', 'none')
}
