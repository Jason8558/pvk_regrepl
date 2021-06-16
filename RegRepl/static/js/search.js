function getdata() {


$.getJSON('/regrepl/item/search/3', (data) => {
  $('#head').text(data[0].dir__name)
$('tbody').append('<tr class="dep" ><td colspan="17">' + data[0].dep__name + '</td></tr>')
$.each(data, (i, val) => {
  if (val.salary == "контракт") {
    salary = val.salary
  }
  else {
    salary = new Intl.NumberFormat('ru-RU').format(val.salary)
  }

  if (val.subdep__name) {
    $('tbody').append('<tr onclick="open_for_upd(' + val.id + ')"class="notcaption" id=' + val.id + '><td>' +  val.name + "(" + val.subdep__name + ")" + "</td><td>" + val.units + '</td><td>' + val.level + '</td><td>'+ val.cat__name + '</td><td>' + val.payment + '</td><td>' + salary + '</td><td>' + salary + '</td><td>' + val.units_rr + '</td><td>' + val.cat_rr__name + '</td><td>' + val.level_rr + '</td><td>' + val.payment_rr + '</td><td>' + val.salary_rr + '</td><td>' + val.salary_rr + '</td><td>' + val.employer1 + '</td><td>' + val.employer2 +'</td><td>' + val.employer3 + '</td><td>' + val.comm +  '</td></tr>')
  }
  else {
    $('tbody').append('<tr onclick="open_for_upd(' + val.id + ')"class="notcaption" id=' + val.id + '><td>' +  val.name  + "</td><td>" + val.units + '</td><td>' + val.level + '</td><td>'+ val.cat__name + '</td><td>' + val.payment + '</td><td>' + salary + '</td><td>' + salary + '</td><td>' + val.units_rr + '</td><td>' + val.cat_rr__name + '</td><td>' + val.level_rr + '</td><td>' + val.payment_rr + '</td><td>' + val.salary_rr + '</td><td>' + val.salary_rr + '</td><td>' + val.employer1 + '</td><td>' + val.employer2 +'</td><td>' + val.employer3 + '</td><td>' + val.comm +  '</td></tr>')
  }


  if (val.dep__name != data[i+1].dep__name) {
    $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dep__name + '</td></tr>')
  }

})
})

}
