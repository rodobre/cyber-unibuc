function show_menu(event)
{
	event.preventDefault();
	let child_elements = document.getElementsByClassName('navbar_ul')[0].children;
	console.log(child_elements);

	for(let i = 1; i < child_elements.length; ++i)
	{
		let child = child_elements.item(i);
		console.log(child);
		if(child.classList.contains("navbar_show"))
			child.classList.remove("navbar_show");
		else
			child.classList.add("navbar_show");
	}
}

let navbar_ul = document.getElementsByClassName('navbar_ul')[0];
