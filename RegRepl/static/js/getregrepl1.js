$(document).ready(function() {
 getdata()
})



function getdata() {


    type = $('#sm_type option:selected').val()
    object_id = $('#sm_main option:selected').val()
    rr_id = document.location.href.split('/')[5]

    query_url = '/regrepl/getdata/5/0/' + rr_id.toString()
    let all_salary = 0
    let all_salary_rr = 0
    let all_units = 0
    let all_units_rr = 0
    let all_temp_pos = 0

    let dep_salary = 0
    let dir_salary = 0
    let dep_salary_rr = 0
    let dir_salary_rr = 0

    let dep_units = 0
    let dir_units = 0

    let dep_units_rr = 0
    let dir_units_rr = 0

    let dep_temp_pos = 0
    let dir_temp_pos = 0
    first_sector = true

    $.getJSON(query_url,  (data) => {

      $('tbody').append('<tr class="dir" ><td colspan="17"><a name="'+ data[0].dir_id +'"></a>' + data[0].dir__name + '</td></tr>')
      $('#goto').append('<p><a href="#'+ data[0].dir_id +'">'+ data[0].dir__name +'</p>')

      $('tbody').append('<tr class="dep" ><td colspan="17">' + data[0].dep__name + '</td></tr>')


      for (var i = 0; i < data.length; i++) {

      pos_free = ""
      pos_dis = ""
      cat_color = ""
      cat_rr_color = ""
      idd = ""



      dep_units = dep_units + parseFloat(data[i].units)
      dep_units_rr = dep_units_rr + parseFloat(data[i].units_rr)

      all_units = all_units + parseFloat(data[i].units)
      all_units_rr = all_units_rr + parseFloat(data[i].units_rr)

      if(data[i].name == 'Директор предприятия') {
        idd = 'director'
      }


      if (data[i].employer2 != '') {
        dep_temp_pos = dep_temp_pos + 1
        all_temp_pos = all_temp_pos + 1

      }

      if (data[i].salary == "контракт") {
      salary = data[i].salary
      }
      else {
      all_salary = all_salary + parseInt(data[i].salary, 10)
      dep_salary = dep_salary + parseInt(data[i].salary, 10)
      salary = new Intl.NumberFormat('ru-RU').format(data[i].salary)
      }

      if (data[i].salary_rr == "контракт") {
      salary_rr = data[i].salary_rr
      }
      else {
      all_salary_rr = all_salary_rr + parseInt(data[i].salary_rr, 10)
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





      $('tbody').append('<tr style="' + pos_free + pos_dis + '" onclick="open_for_upd(' + data[i].id + ',' + data[i].bound_regrepl_id + ')"class="notcaption" id=' + data[i].id + '><td class="pname">' +  data[i].name +  "</td><td class='units'>" + data[i].units + '</td><td class="level">' + data[i].level + '</td><td style="' + cat_color + '" class="cat">'+ data[i].cat__name + '</td><td class="payment ' + idd + '">' + data[i].payment + '</td><td class="salary">' + salary + '</td><td class="salary">' + salary + '</td><td class="units_rr">' + data[i].units_rr +  '</td><td сlass="level_rr">' + data[i].level_rr + '</td><td style="' + cat_rr_color + '" class="cat_rr">' + data[i].cat_rr__name  +  '</td><td  class="payment_rr ' + idd + ' " >' + data[i].payment_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="salary_rr">' + salary_rr + '</td><td class="rc_employer  employer1">' + data[i].employer1 + '</td><td class="rc_employer  employer2">' + data[i].employer2 +'</td><td class="rc_employer  employer3">' + data[i].employer3 + '</td><td class="comm">' + data[i].comm +  '</td></tr>')

if (i != data.length-1) {
      if (data[i+1].subdep__name &&  data[i].subdep__name != data[i+1].subdep__name ) {
        $('tbody').append( "<tr class='subdep'><td colspan='17'>"+ data[i+1].subdep__name +"</td></tr> ")}
}

      if (i == data.length-1) {

      dir_salary = dir_salary + dep_salary
      dir_salary_rr = dir_salary_rr + dep_salary_rr
      dir_units = dir_units + dep_units
      dir_units_rr = dir_units_rr + dep_units_rr
      dir_temp_pos = dir_temp_pos + dep_temp_pos

      $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td></td> <td></td><td>временных: "+ dep_temp_pos +"</td><td></td><td></td></tr> ")


      $('tbody').append( "<tr class=diritogo><td> Итого по: " + data[i].dir__name + " </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td></td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td> <td></td><td>временных: "+ dir_temp_pos +"</td><td></td><td></td></tr> ")

      $('tbody').append( "<tr class=all_itog><td> Итого по предприятию (филиалу): </td> <td>" + all_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(all_salary) + "</td><td></td><td>"+ all_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(all_salary_rr)+"</td> <td></td> <td></td><td>временных: "+ all_temp_pos +"</td><td></td><td></td></tr> ")
      }
      else {


      if (data[i].dep__name != data[i+1].dep__name) {
        $('tbody').append( "<tr class='itogo'><td> Итого </td> <td>"+ dep_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary) + "</td><td></td><td>"+ dep_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) +"</td> <td>" + new Intl.NumberFormat('ru-RU').format(dep_salary_rr) + "</td> <td></td><td>временных: "+ dep_temp_pos +"</td><td></td><td></td></tr> ")


          if (data[i].dir__name != data[i+1].dir__name) {
              dir_salary = dir_salary + dep_salary
              dir_salary_rr = dir_salary_rr + dep_salary_rr
              dir_units = dir_units + dep_units
              dir_units_rr = dir_units_rr + dep_units_rr
              dir_temp_pos = dir_temp_pos + dep_temp_pos
              $('tbody').append( "<tr class=diritogo><td> Итого по: " + data[i].dir__name + " </td> <td>" + dir_units +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary) + "</td><td></td><td>"+ dir_units_rr +"</td><td></td><td></td><td></td><td>" + new Intl.NumberFormat('ru-RU').format(dir_salary_rr)+"</td> <td></td> <td></td><td>временных: "+ dir_temp_pos +"</td><td></td><td></td></tr> ")
              $('tbody').append('<tr class="dir"  ><td colspan="17"><a name='+  data[i+1].dir_id +'></a>' + data[i+1].dir__name + '</td></tr>')
              $('#goto').append('<p><a href="#'+ data[i+1].dir_id +'">'+ data[i+1].dir__name +'</p>')
              dir_salary = 0
              dir_salary_rr = 0
              dir_units = 0
              dir_units_rr = 0
              dir_temp_pos = 0
              dep_salary = 0
              dep_salary_rr = 0
              dep_units = 0
              dep_units_rr = 0
              dep_temp_pos = 0

          }

      $('tbody').append('<tr class="dep"  ><td colspan="17">' + data[i+1].dep__name + '</td></tr>')

        dir_salary = dir_salary + dep_salary
        dir_salary_rr = dir_salary_rr + dep_salary_rr
        dir_units = dir_units + dep_units
        dir_units_rr = dir_units_rr + dep_units_rr
        dir_temp_pos = dir_temp_pos + dep_temp_pos

        dep_salary = 0
        dep_salary_rr = 0
        dep_units = 0
        dep_units_rr = 0
        dep_temp_pos = 0



      }



      }










      }


    })

setTimeout(() => $('#loading').remove(), 2000)
// styling for excel
setTimeout(() => $('.dep').css('background', 'lightblue'), 3000)
setTimeout(() => $('.dep').css('text-align', 'center'), 3000)
setTimeout(() => $('.dep td').css('border', '1px solid black'), 3000)

setTimeout(() => $('.subdep').css('color', 'red'), 3000)
setTimeout(() => $('.subdep').css('text-align', 'center'), 3000)
setTimeout(() => $('.subdep td').css('border', '1px solid black'), 3000)
setTimeout(() => $('.subdep td').css('text-decoration', 'underline'), 3000)

setTimeout(() => $('.dir').css('background', 'blue'), 3000)
setTimeout(() => $('.dir').css('text-align', 'center'), 3000)
setTimeout(() => $('.dir').css('font-size', '12pt'), 3000)
setTimeout(() => $('.dir').css('color', 'white'), 3000)
setTimeout(() => $('.dir').css('font-weight', 'bold'), 3000)
setTimeout(() => $('.dir td').css('border', '1px solid black'), 3000)

setTimeout(() => $('.itogo').css('background', 'gray'), 3000)
setTimeout(() => $('.itogo').css('border', '1px solid white'), 3000)
setTimeout(() => $('.diritogo').css('background', 'darkgray'), 3000)
setTimeout(() => $('.diritogo').css('border', '1px solid white'), 3000)

setTimeout(() => $('.all_itog').css('font-size', '14pt'), 3000)
setTimeout(() => $('.all_itog').css('background', 'green'), 3000)
setTimeout(() => $('.all_itog').css('font-weight', 'bold'), 3000)
setTimeout(() => $('.all_itog').css('border', '1px solid white'), 3000)

setTimeout(() => $('.director').text(''), 3000)

setTimeout(() => $('.all_itog').css('border', '1px solid white'), 3000)

setTimeout(() => $('.notcaption').css('border', '1px solid lightgrey'), 3000)

setTimeout(() => $('#goto p a').click(function(){
  $('#goto').css('display','none')
}),3000)

setTimeout(() => $('#goto-click').click(function(){
  $('#goto').css('display','block')
}),3000)


    }
