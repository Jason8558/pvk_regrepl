function set_head() {
  tablew = $('#regrepl_table').css('width')
  tableh = $('#regrepl_table thead').css('height')
  console.log(tableh);
  headcells = $('.headcopy td')
  tablecells = $('.verticalrow td')
  $('.lock_table_head').css('width', tablew )
  $('.lock_table_head').css('height', tableh )
  for (var i = 0; i < tablecells.length; i++) {
    headcells[i].style.width = window.getComputedStyle(tablecells[i]).width
  }
}

$(window).on('scroll', function () {
  head = $("#regrepl_table thead")
  pos = head[0].getBoundingClientRect().y
  if (pos < -203) {
      $('.lock_table_head').css('display', 'block')
      set_head()
  }
  else {
    $('.lock_table_head').css('display', 'none')
  }
})

function del_space() {
  text = $('#id_salary').val()
  text2 = $('#id_salary_rr').val()


  text = text.split(' ')
  console.log(text);
  if (text.length > 1) {
    text = text[0].toString() + text[1].toString()
    $('#id_salary').val(text)
  }

  if (text2) {
    text2 = text2.split(' ')
    if (text2.length > 1) {
      text2 = text2[0].toString() + text2[1].toString()
      $('#id_salary_rr').val(text2)
    }
  }

}
