let username = localStorage.getItem('username');
let greeting = document.getElementById('greeting');

if(username == null)
	greeting.innerHTML = 'Hello stranger!';
else
	greeting.innerHTML = 'Hello ' + localStorage.getItem('username') + '!';