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
  $('#sm_btw_container').css('display', '')
  $('#sm_main').css('display', '')
  $('#sm_position').css('display', 'none')
  $.getJSON('/getdirs/', (data) => {
      $.each(data, (i, val) => {
           $('#sm_main').append('<option value="' + val.id + '">' + val.name + "</option>"  )
})
  })
    break;
  case '2':
  $('#sm_btw_container').css('display', 'none')
  $('#sm_main').css('display', '')
  $('#sm_position').css('display', 'none')
  $.getJSON('/getdeps/', (data) => {
      $.each(data, (i, val) => {
           $('#sm_main').append('<option value="' + val.id + '">' + val.name + "/" + val.dirdepartament__name+ "</option>"  )

})
  })
break;
  case '3':
  $('#sm_btw_container').css('display', '')
  $('#sm_main').css('display', 'none')
  $('#sm_position').css('display', '')
  break;

  case '4':
  $('#sm_btw_container').css('display', '')
      $('#sm_main').css('display', '')
      $('#sm_position').css('display', 'none')
      $('#sm_main').append('<option value="1">Руководители</option><option value="2">Специалисты</option><option value="3">Рабочие</option>' )
     break;

     case '6':
     $('#sm_btw_container').css('display', '')
         $('#sm_main').css('display', 'none')
         $('#sm_position').css('display', 'none')

        break;

  case '7':
  $('#sm_btw_container').css('display', '')
      $('#sm_main').css('display', '')
      $('#sm_position').css('display', 'none')
      $('#sm_main').append('<option value="1">ПКГО</option><option value="2">ЕМР</option>' )
     break;

  default:

  }
}

function getdata() {
  $('#sm_havebetween').prop('checked', false)
    $('tbody').find('tr').remove();
    type = $('#sm_type option:selected').val()
    object_id = $('#sm_main option:selected').val()
    rr_id = document.location.href.split('/')[6]
    console.log($('#sm_type option:selected').val());
    if ($('#sm_type option:selected').val() == 3) {

              query_url = '/regrepl/getdata/getpos/' + rr_id.toString() +"/"+ $('#sm_position').val()
    }
    else {
      if ($('#sm_type option:selected').val() == 6) {
              query_url = '/regrepl/getdata/' + type.toString() + "/0/" + rr_id.toString()
      }
      else {
            query_url = '/regrepl/getdata/' + type.toString() + "/" + object_id.toString() + "/" + rr_id.toString()
      }
    }





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
      background = ""
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
      background = "background: yellow;"
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
      subdep = "(" + data[i].subdep__name + ")"
      console.log(subdep); }
      else {
      subdep = ""
      }

        if ($('#sm_type option:selected').val() == 6) {
          background = "background:"}



      $('tbody').append('<tr style="'+ background +  pos_dis + '" onclick="open_for_upd(' + data[i].id + ',' + data[i].bound_regrepl_id + ')"class="notcaption" id=' + data[i].id + '><td class="pname">' +  data[i].name + subdep + "</td><td class='units'>" + data[i].units + '</td><td class="level">' + data[i].level + '</td><td style="' + cat_color + '" class="cat">'+ data[i].cat__name + '</td><td class="payment">' + data[i].payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + data[i].units_rr + '<td сlass="level_rr">' + data[i].level_rr + '</td><td style="' + cat_rr_color + '" class="cat_rr">' + data[i].cat_rr__name + '</td>><td class="payment_rr" >' + data[i].payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + data[i].employer1 + '</td><td class="rc_employer  employer2">' + data[i].employer2 +'</td><td class="rc_employer  employer3">' + data[i].employer3 + '</td><td class="comm">' + data[i].comm +  '</td></tr>')


      if (i == data.length-1) {

      dir_salary = dir_salary + dep_salary
      dir_salary_rr = dir_salary_rr + dep_salary_rr
      dir_units = dir_units + dep_units
      dir_units_rr = dir_units_rr + dep_units_rr

      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td></td><td></td><td></td><td></td></tr> ")
      if ($('#sm_type option:selected').val() == 1) {

      $('tbody').append( "<tr class=diritogo><td> Итого по: " + data[i].dir__name + " </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td><td></td><td></td><td></td></tr> ")
      }
      if ($('#sm_type option:selected').val() == 3) {

      $('tbody').append( "<tr class=diritogo><td> Итого </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td><td></td><td></td><td></td></tr> ")
      }

      if ($('#sm_type option:selected').val() == 4) {

      $('tbody').append( "<tr class=diritogo><td>" + $('#sm_main option:selected').text() +" итого </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td><td></td><td></td><td></td></tr> ")
      }

      if ($('#sm_type option:selected').val() == 6) {

      $('tbody').append( "<tr class=diritogo><td>Итого по свободным ставкам </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td><td></td><td></td><td></td></tr> ")
      }

      if ($('#sm_type option:selected').val() == 7) {

      $('tbody').append( "<tr class=diritogo><td>Итого по "+ $('#sm_main option:selected').text()  +" </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td></td> <td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td><td></td><td></td><td></td></tr> ")
      }

      }
      else {
      if (data[i].dep__name != data[i+1].dep__name) {
      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td></td> <td></td><td></td><td></td><td></td></tr> ")

      $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dep__name + '</td></tr>')

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

function  have_between() {

  if ($('#sm_havebetween').prop('checked') == true) {
    $('.itogo').css('display', 'none')
    $('.dep').css('display', 'none')
  }
  else {
    $('.itogo').css('display', '')
    $('.dep').css('display', '')
  }
}
