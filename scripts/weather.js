let request = new XMLHttpRequest();
request.open("GET", "https://wttr.in/Utrecht?format=3");
request.send();
request.onload = () => {
    console.log(request);
    document.getElementById('weather').innerHTML = request.responseText;
}