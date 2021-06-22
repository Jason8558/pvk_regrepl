$(document).ready(function() {
  $.getJSON('/getdirs/', (data) => {
    
      $.each(data, (i, val) => {
           $('#sm_main').append('<option value="' + val.id + '">' + val.name + "</option>"  )
})
  })

})


function select_search_type() {
   $('#sm_main').find('option').remove();

switch ($('#sm_type option:selected').val()) {
  case '1':
  $.getJSON('/getdirs/', (data) => {
      $.each(data, (i, val) => {
           $('#sm_main').append('<option value="' + val.id + '">' + val.name + "</option>"  )
})
  })
    break;
  case '2':
  $.getJSON('/getdeps/', (data) => {
      $.each(data, (i, val) => {
           $('#sm_main').append('<option value="' + val.id + '">' + val.name + "</option>"  )

})
  })
  default:

  }
}





function getdata() {
  $('tbody').find('tr').remove();
type = $('#sm_type option:selected').val()
object_id = $('#sm_main option:selected').val()
rr_id = document.location.href.split('/')[6]
query_url = '/regrepl/getdata/' + type.toString() + "/" + object_id.toString() + "/" + rr_id.toString()
let dep_salary = 0
let dep_units = 0
let dep_units_rr = 0
let dir_salary = 0

  $.getJSON(query_url,  (data) => {
    $('#head').text(data[0].dir__name)
  $('tbody').append('<tr class="dep" ><td colspan="17">' + data[0].dep__name + '</td></tr>')
  $.each(data, (i, val) => {
    pos_free = ""
    pos_dis = ""
    cat_color = ""
    dep_units = dep_units + parseFloat(val.units)
    dep_units_rr = dep_units + parseFloat(val.units_rr)

    if (val.salary == "контракт") {
      salary = val.salary
    }
    else {
      dep_salary = dep_salary + parseInt(val.salary, 10)
      salary = new Intl.NumberFormat('ru-RU').format(val.salary)
    }



    if (val.salary_rr == "контракт") {
      salary_rr = val.salary_rr
    }
    else {
      salary_rr = new Intl.NumberFormat('ru-RU').format(val.salary_rr)
    }

    if (val.free == true) {
      pos_free = "background: yellow;"
    }
    if (val.disabled == true) {
      pos_dis = "text-decoration: line-through;"
    }

    switch (val.cat_id) {
      case 1:
        cat_color = "color: red; font-weight: bold;  !important"
        break;
      case 2:
        cat_color = "color: #ff69b4; font-weight: bold; !important"
        break;
      case 3:
        cat_color = "color: blue; font-weight: bold; !important"
        break;

      default:

    }


    if (val.subdep__name) {
      $('tbody').append('<tr style="' + pos_free + pos_dis + '" onclick="open_for_upd(' + val.id + ')"class="notcaption" id=' + val.id + '><td class="pname">' +  val.name + "(" + val.subdep__name + ")" + "</td><td class='units'>" + val.units + '</td><td class="level">' + val.level + '</td><td style="' + cat_color + '" class="cat">'+ val.cat__name + '</td><td class="payment">' + val.payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + val.units_rr + '</td><td class="cat_rr">' + val.cat_rr__name + '</td><td сlass="level_rr">' + val.level_rr + '</td><td class="payment_rr" >' + val.payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + val.employer1 + '</td><td class="rc_employer  employer2">' + val.employer2 +'</td><td class="rc_employer  employer3">' + val.employer3 + '</td><td class="comm">' + val.comm +  '</td></tr>')
    }
    else {
      $('tbody').append('<tr style="' + pos_free + pos_dis + '" onclick="open_for_upd(' + val.id + ')"class="notcaption" id=' + val.id + '><td class="pname">' +  val.name  + "</td><td class='units'>" + val.units + '</td><td class="level">' + val.level + '</td><td style="' + cat_color + '" class="cat">'+ val.cat__name + '</td><td class="payment">' + val.payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + val.units_rr + '</td><td class="cat_rr">' + val.cat_rr__name + '</td><td сlass="level_rr">' + val.level_rr + '</td><td class="payment_rr">' + val.payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + val.employer1 + '</td><td class="rc_employer  employer2">' + val.employer2 +'</td><td class="rc_employer  employer3">' + val.employer3 + '</td><td class="comm">' + val.comm +  '</td></tr>')
    }



    if ( typeof data[i+1].dep__name === undefined) { console.log("aaaaa");}
    if (val.dep__name != data[i+1].dep__name) {
      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td></td><td>"+ dep_units +"</td><td></td><td></td><td></td><td></td> <td></td> <td></td><td></td><td></td><td></td></tr> ")

      $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dep__name + '</td></tr>')
      dir_salary = dir_salary + dep_salary
      dep_salary = 0
      dep_units = 0
    }



  })
console.log('here');
  switch ($('#sm_type option:selected').val()) {
    case '1':
      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td></td><td>"+ dep_units +"</td><td></td><td></td><td></td><td></td> <td></td> <td></td><td></td><td></td><td></td></tr> ")
      break;
    case '2':

    default:

    }

  })



}
