$(document).ready(function() {
 getdata()
})



function getdata() {
$('tbody').find('tr').remove();
    type = $('#sm_type option:selected').val()
    object_id = $('#sm_main option:selected').val()
    rr_id = document.location.href.split('/')[5]
    console.log(rr_id);
    query_url = '/regrepl/getdata/5/0/' + rr_id.toString()

    let dep_salary = 0
    let dir_salary = 0
    let dep_salary_rr = 0
    let dir_salary_rr = 0

    let dep_units = 0
    let dir_units = 0

    let dep_units_rr = 0
    let dir_units_rr = 0


    $.getJSON(query_url,  (data) => {

      $('tbody').append('<tr class="dep" ><td colspan="17">' + data[0].dep__name + '</td></tr>')
      for (var i = 0; i < data.length; i++) {
      pos_free = ""
      pos_dis = ""
      cat_color = ""
      cat_rr_color = ""
      dep_units = dep_units + parseFloat(data[i].units)
      dep_units_rr = dep_units_rr + parseFloat(data[i].units_rr)



      if (data[i].salary == "контракт") {
      salary = data[i].salary
      }
      else {
      dep_salary = dep_salary + parseInt(data[i].salary, 10)
      salary = new Intl.NumberFormat('ru-RU').format(data[i].salary)
      }

      if (data[i].salary_rr == "контракт") {
      salary_rr = data[i].salary_rr
      }
      else {
      dep_salary_rr = dep_salary_rr + parseInt(data[i].salary_rr, 10)
      salary_rr = new Intl.NumberFormat('ru-RU').format(data[i].salary_rr)
      }


      if (data[i].free == true) {
      pos_free = "background: yellow;"
      }
      if (data[i].disabled == true) {
      pos_dis = "text-decoration: line-through;"
      }

      switch (data[i].cat_id) {
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



      switch (data[i].cat_rr_id) {
      case 1:
      cat_rr_color = "color: red; font-weight: bold;  !important"
      break;
      case 2:
      cat_rr_color = "color: #ff69b4; font-weight: bold; !important"
      break;
      case 3:
      cat_rr_color = "color: blue; font-weight: bold; !important"
      break;

      default:

      }



      if (data[i].subdep__name) {
      $('tbody').append('<tr style="' + pos_free + pos_dis + '" onclick="open_for_upd(' + data[i].id + ')"class="notcaption" id=' + data[i].id + '><td class="pname">' +  data[i].name + "(" + data[i].subdep__name + ")" + "</td><td class='units'>" + data[i].units + '</td><td class="level">' + data[i].level + '</td><td style="' + cat_color + '" class="cat">'+ data[i].cat__name + '</td><td class="payment">' + data[i].payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + data[i].units_rr + '</td><td style="' + cat_rr_color + '" class="cat_rr">' + data[i].cat_rr__name + '</td><td сlass="level_rr">' + data[i].level_rr + '</td><td class="payment_rr" >' + data[i].payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + data[i].employer1 + '</td><td class="rc_employer  employer2">' + data[i].employer2 +'</td><td class="rc_employer  employer3">' + data[i].employer3 + '</td><td class="comm">' + data[i].comm +  '</td></tr>')
      }
      else {
      $('tbody').append('<tr style="' + pos_free + pos_dis + '" onclick="open_for_upd(' + data[i].id + ')"class="notcaption" id=' + data[i].id + '><td class="pname">' +  data[i].name  + "</td><td class='units'>" + data[i].units + '</td><td class="level">' + data[i].level + '</td><td style="' + cat_color + '" class="cat">'+ data[i].cat__name + '</td><td class="payment">' + data[i].payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + data[i].units_rr + '</td><td style="'+ cat_rr_color + '" class="cat_rr">' + data[i].cat_rr__name + '</td><td сlass="level_rr">' + data[i].level_rr + '</td><td class="payment_rr">' + data[i].payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + data[i].employer1 + '</td><td class="rc_employer  employer2">' + data[i].employer2 +'</td><td class="rc_employer  employer3">' + data[i].employer3 + '</td><td class="comm">' + data[i].comm +  '</td></tr>')
      }

      if (i == data.length-1) {

      dir_salary = dir_salary + dep_salary
      dir_salary_rr = dir_salary_rr + dep_salary_rr
      dir_units = dir_units + dep_units
      dir_units_rr = dir_units_rr + dep_units_rr

      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td></td> <td></td><td></td><td></td><td></td></tr> ")
      if ($('#sm_type option:selected').val() == 1) {

      $('tbody').append( "<tr class=diritogo><td> Итого по: " + data[i].dir__name + " </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td></td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td> <td></td><td></td><td></td><td></td></tr> ")
      }

      }
      else {

      if (data[i].dep__name != data[i+1].dep__name) {
      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td></td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) + "</td> <td></td><td></td><td></td><td></td></tr> ")

      $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dep__name + '</td></tr>')
      if (data[i].dir__name != data[i+1].dir__name) {
        $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dir__name + '</td></tr>')
      }


      dir_salary = dir_salary + dep_salary
      dir_salary_rr = dir_salary_rr + dep_salary_rr
      dir_units = dir_units + dep_units
      dir_units_rr = dir_units_rr + dep_units_rr

      dep_salary = 0
      dep_salary_rr = 0
      dep_units = 0
      dep_units_rr = 0


      }


      }










      }


    })



    }