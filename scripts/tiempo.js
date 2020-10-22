$(window).on("load", function () {
var lat = 39.036;
var lon = -2.992;
var key = "0a4cd51d5182e09f19dc0824d5cbbc44";
 $.getJSON("https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+key+"&exclude=minutely,alerts&units=metric", getForecast);
});

var getForecast = function(data) {
    console.log(data);
	// Actual
	document.getElementById("curt").innerHTML = Math.round(data.current.temp) + "ºC";
	document.getElementById("1").innerHTML = Math.round(data.current.clouds) + "%";
	document.getElementById("2").innerHTML = Math.round(data.current.humidity) + "%";
	var salidahoy = unixTime(data.current.sunrise);
	var puestahoy = unixTime(data.current.sunset);
	document.getElementById("3").innerHTML = salidahoy;
	document.getElementById("4").innerHTML = data.current.wind_speed.toFixed(1)  + " k/h";	
	document.getElementById("5").innerHTML = Math.round(data.current.uvi);
	document.getElementById("6").innerHTML = puestahoy;
		var iconoahora = data.current.weather[0].icon;
		if (iconoahora == "03d" || iconoahora == "03n" || iconoahora == "04d" || iconoahora == "04n" || iconoahora == "09d" || iconoahora == "09n" || iconoahora == "11d" || iconoahora == "11n" || iconoahora == "13d" || iconoahora == "13n" || iconoahora == "50d" || iconoahora == "50n") {
		var iconoahora = iconoahora.substr(0, 2);;
			}
		var mainiconr = "../archivos/iconostiempo/"+iconoahora+".svg";
		$("#main-icon").attr("src", mainiconr);

    // Horas
	var hora1 = unixTime(data.hourly[2].dt);
	document.getElementById("hour-1").innerHTML = hora1;
	document.getElementById("hora11").innerHTML = Math.round(data.hourly[2].temp) + "ºC";
	document.getElementById("hora12").innerHTML = Math.round(data.hourly[2].pop) + "%";	
		var iconohora1 = data.hourly[2].weather[0].icon;
		if (iconohora1 == "03d" || iconohora1 == "03n" || iconohora1 == "04d" || iconohora1 == "04n" || iconohora1 == "09d" || iconohora1 == "09n" || iconohora1 == "11d" || iconohora1 == "11n" || iconohora1 == "13d" || iconohora1 == "13n" || iconohora1 == "50d" || iconohora1 == "50n") {
		var iconohora1 = iconohora1.substr(0, 2);;
			}
		var iconohora1r = "../archivos/iconostiempo/"+iconohora1+".svg";
		$("#hourly-icon-1").attr("src", iconohora1r);
	
	
	

	var hora2 = unixTime(data.hourly[4].dt);
	document.getElementById("hour-2").innerHTML = hora2;
	document.getElementById("hora21").innerHTML = Math.round(data.hourly[4].temp) + "ºC";
	document.getElementById("hora22").innerHTML = Math.round(data.hourly[4].pop) + "%";	
		var iconohora2 = data.hourly[4].weather[0].icon;
		if (iconohora2 == "03d" || iconohora2 == "03n" || iconohora2 == "04d" || iconohora2 == "04n" || iconohora2 == "09d" || iconohora2 == "09n" || iconohora2 == "11d" || iconohora2 == "11n" || iconohora2 == "13d" || iconohora2 == "13n" || iconohora2 == "50d" || iconohora2 == "50n") {
		var iconohora2 = iconohora2.substr(0, 2);;
			}
		var iconohora2r = "../archivos/iconostiempo/"+iconohora2+".svg";
		$("#hourly-icon-2").attr("src", iconohora2r);

	var hora3 = unixTime(data.hourly[6].dt);
	document.getElementById("hour-3").innerHTML = hora3;
	document.getElementById("hora31").innerHTML = Math.round(data.hourly[6].temp) + "ºC";
	document.getElementById("hora32").innerHTML = Math.round(data.hourly[6].pop) + "%";	
		var iconohora3 = data.hourly[6].weather[0].icon;
		if (iconohora3 == "03d" || iconohora3 == "03n" || iconohora3 == "04d" || iconohora3 == "04n" || iconohora3 == "09d" || iconohora3 == "09n" || iconohora3 == "11d" || iconohora3 == "11n" || iconohora3 == "13d" || iconohora3 == "13n" || iconohora3 == "50d" || iconohora3 == "50n") {
		var iconohora3 = iconohora3.substr(0, 2);;
			}
		var iconohora3r = "../archivos/iconostiempo/"+iconohora3+".svg";
		$("#hourly-icon-3").attr("src", iconohora3r);
	
	var hora4 = unixTime(data.hourly[8].dt);
	document.getElementById("hour-4").innerHTML = hora4;
	document.getElementById("hora41").innerHTML = Math.round(data.hourly[8].temp) + "ºC";
	document.getElementById("hora42").innerHTML = Math.round(data.hourly[8].pop) + "%";	
		var iconohora4 = data.hourly[8].weather[0].icon;
		if (iconohora4 == "03d" || iconohora4 == "03n" || iconohora4 == "04d" || iconohora4 == "04n" || iconohora4 == "09d" || iconohora4 == "09n" || iconohora4 == "11d" || iconohora4 == "11n" || iconohora4 == "13d" || iconohora4 == "13n" || iconohora4 == "50d" || iconohora4 == "50n") {
		var iconohora4 = iconohora4.substr(0, 2);;
			}
		var iconohora4r = "../archivos/iconostiempo/"+iconohora4+".svg";
		$("#hourly-icon-4").attr("src", iconohora4r);
	
	var hora5 = unixTime(data.hourly[10].dt);
	document.getElementById("hour-5").innerHTML = hora5;
	document.getElementById("hora51").innerHTML = Math.round(data.hourly[10].temp) + "ºC";
	document.getElementById("hora52").innerHTML = Math.round(data.hourly[10].pop) + "%";	
		var iconohora5 = data.hourly[10].weather[0].icon;
		if (iconohora5 == "03d" || iconohora5 == "03n" || iconohora5 == "04d" || iconohora5 == "04n" || iconohora5 == "09d" || iconohora5 == "09n" || iconohora5 == "11d" || iconohora5 == "11n" || iconohora5 == "13d" || iconohora5 == "13n" || iconohora5 == "50d" || iconohora5 == "50n") {
		var iconohora5 = iconohora5.substr(0, 2);;
			}
		var iconohora5r = "../archivos/iconostiempo/"+iconohora5+".svg";
		$("#hourly-icon-5").attr("src", iconohora5r);

    // Dias
	var dia1 = unixdia(data.daily[1].dt);
	document.getElementById("day-1").innerHTML = dia1;
	document.getElementById("dia11").innerHTML = Math.round(data.daily[1].temp.max) + "ºC";;
	document.getElementById("dia12").innerHTML = Math.round(data.daily[1].temp.min) + "ºC";;
		var iconodia1 = data.daily[1].weather[0].icon;
		if (iconodia1 == "03d" || iconodia1 == "03n" || iconodia1 == "04d" || iconodia1 == "04n" || iconodia1 == "09d" || iconodia1 == "09n" || iconodia1 == "11d" || iconodia1 == "11n" || iconodia1 == "13d" || iconodia1 == "13n" || iconodia1 == "50d" || iconodia1 == "50n") {
		var iconodia1 = iconodia1.substr(0, 2);;
			}
		var iconodia1r = "../archivos/iconostiempo/"+iconodia1+".svg";
		$("#daily-icon-1").attr("src", iconodia1r);

	var dia2 = unixdia(data.daily[2].dt);
	document.getElementById("day-2").innerHTML = dia2;
	document.getElementById("dia21").innerHTML = Math.round(data.daily[2].temp.max) + "ºC";;
	document.getElementById("dia22").innerHTML = Math.round(data.daily[2].temp.min) + "ºC";;	
		var iconodia2 = data.daily[2].weather[0].icon;
		if (iconodia2 == "03d" || iconodia2 == "03n" || iconodia2 == "04d" || iconodia2 == "04n" || iconodia2 == "09d" || iconodia2 == "09n" || iconodia2 == "11d" || iconodia2 == "11n" || iconodia2 == "13d" || iconodia2 == "13n" || iconodia2 == "50d" || iconodia2 == "50n") {
		var iconodia2 = iconodia2.substr(0, 2);;
			}
		var iconodia2r = "../archivos/iconostiempo/"+iconodia2+".svg";
		$("#daily-icon-2").attr("src", iconodia2r);
	
	var dia3 = unixdia(data.daily[3].dt);
	document.getElementById("day-3").innerHTML = dia3;
	document.getElementById("dia31").innerHTML = Math.round(data.daily[3].temp.max) + "ºC";;
	document.getElementById("dia32").innerHTML = Math.round(data.daily[3].temp.min) + "ºC";;
		var iconodia3 = data.daily[3].weather[0].icon;
		if (iconodia3 == "03d" || iconodia3 == "03n" || iconodia3 == "04d" || iconodia3 == "04n" || iconodia3 == "09d" || iconodia3 == "09n" || iconodia3 == "11d" || iconodia3 == "11n" || iconodia3 == "13d" || iconodia3 == "13n" || iconodia3 == "50d" || iconodia3 == "50n") {
		var iconodia3 = iconodia3.substr(0, 2);;
			}
		var iconodia3r = "../archivos/iconostiempo/"+iconodia3+".svg";
		$("#daily-icon-3").attr("src", iconodia3r);
		
	var dia4 = unixdia(data.daily[4].dt);
	document.getElementById("day-4").innerHTML = dia4;
	document.getElementById("dia41").innerHTML = Math.round(data.daily[4].temp.max) + "ºC";;
	document.getElementById("dia42").innerHTML = Math.round(data.daily[4].temp.min) + "ºC";;
		var iconodia4 = data.daily[4].weather[0].icon;
		if (iconodia4 == "03d" || iconodia4 == "03n" || iconodia4 == "04d" || iconodia4 == "04n" || iconodia4 == "09d" || iconodia4 == "09n" || iconodia4 == "11d" || iconodia4 == "11n" || iconodia4 == "13d" || iconodia4 == "13n" || iconodia4 == "50d" || iconodia4 == "50n") {
		var iconodia4 = iconodia4.substr(0, 2);;
			}
		var iconodia4r = "../archivos/iconostiempo/"+iconodia4+".svg";
		$("#daily-icon-4").attr("src", iconodia4r);

	var dia5 = unixdia(data.daily[5].dt);
	document.getElementById("day-5").innerHTML = dia5;
	document.getElementById("dia51").innerHTML = Math.round(data.daily[5].temp.max) + "ºC";;
	document.getElementById("dia52").innerHTML = Math.round(data.daily[5].temp.min) + "ºC";;
		var iconodia5 = data.daily[5].weather[0].icon;
		if (iconodia5 == "03d" || iconodia5 == "03n" || iconodia5 == "04d" || iconodia5 == "04n" || iconodia5 == "09d" || iconodia5 == "09n" || iconodia5 == "11d" || iconodia5 == "11n" || iconodia5 == "13d" || iconodia5 == "13n" || iconodia5 == "50d" || iconodia5 == "50n") {
		var iconodia5 = iconodia5.substr(0, 2);;
			}
		var iconodia5r = "../archivos/iconostiempo/"+iconodia5+".svg";
		$("#daily-icon-5").attr("src", iconodia5r);	
} 
 
 
function unixTime(transforma) {
    var date = new Date(transforma * 1000);
    var hours = "0" + date.getHours();
	var minutes = "0" + date.getMinutes();
	var seconds = "0" + date.getSeconds();
	var formato = hours.substr(-2) + ':' + minutes.substr(-2);
    return formato;
}

function unixdia(transforma2) {
    var date2 = new Date(transforma2 * 1000);
    var diafin = date2.getDay();
	if (diafin == 1) {
		var diafin2 = "Lunes";
	}
	if (diafin == 2) {
		var diafin2 = "Martes";
	}
	if (diafin == 3) {
		var diafin2 = "Miercoles";
	}
	if (diafin == 4) {
		var diafin2 = "Jueves";
	}
	if (diafin == 5) {
		var diafin2 = "Viernes";
	}
	if (diafin == 6) {
		var diafin2 = "Sabado";
	}
	if (diafin == 0) {
		var diafin2 = "Domingo";
	}	
    return diafin2;
}
