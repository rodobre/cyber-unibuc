fetch('/api/session_check', { method: "POST" })
	.then(function(response) {
		let status_code = response.status;
		if(response.status == 200)
		{
			let login_href_mod = document.querySelector('#login_href'),
				register_href_mod = document.querySelector('#register_href');

			login_href_mod.href = "/profile";
			register_href_mod.href = "/logout";

			login_href_mod.innerHTML = localStorage.getItem('username');
			register_href_mod.innerHTML = 'logout';
		}
	});