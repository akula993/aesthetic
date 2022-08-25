// Burger
const btnMenu = document.querySelector('#toggle');
const menu = document.querySelector('.header__nav');
const bodyEl = document.querySelector('body');
let navItemAll = document.querySelectorAll('.header__nav-item');

const menuLine1 = document.querySelector('.top-bun');
const menuLine2 = document.querySelector('.meat');
const menuLine3 = document.querySelector('.bottom-bun');

const toggleMenu = function () {
	menu.classList.toggle('open');
}
const toggleBurger = function () {
	btnMenu.classList.toggle('active');
}
const toggleMenuLine = function () {
	menuLine1.classList.toggle('active');
	menuLine2.classList.toggle('active');
	menuLine3.classList.toggle('active');
}
const bodyOverflow = function () {
	bodyEl.classList.toggle('hidden');
}
btnMenu.addEventListener('click', function (e) {
	e.stopPropagation();
	toggleMenu();
	toggleBurger();
	bodyOverflow();
	toggleMenuLine();
});
navItemAll.forEach((el) => {
	el.addEventListener("click", function () {
		if (menu.classList.contains("open")) {
			toggleMenu();
			toggleBurger();
			bodyOverflow();
		}
	});
})


// Modal Cards Select Styles
let selectSingle = document.querySelector('.__select');

if(selectSingle) {

  let selectSingle_title = selectSingle.querySelector('.__select__title');
let selectSingle_labels = selectSingle.querySelectorAll('.__select__label');
// Toggle menu
selectSingle_title.addEventListener('click', () => {
	if ('active' === selectSingle.getAttribute('data-state')) {
		selectSingle.setAttribute('data-state', '');
	} else {
		selectSingle.setAttribute('data-state', 'active');
	}
});

// Close when click to option
for (let i = 0; i < selectSingle_labels.length; i++) {
	selectSingle_labels[i].addEventListener('click', (evt) => {
		selectSingle_title.textContent = evt.target.textContent;
		selectSingle.setAttribute('data-state', '');
	});
}
}

document.addEventListener('DOMContentLoaded', () => {
	const hero = document.querySelector('.header');
	const header = document.querySelector('.header__bottom');
	const mainEl = document.querySelector('.main');

	const headerFixed = () => {
		let scrollTop = window.scrollY;
		let heroCenter = hero.offsetHeight / 2;

		if (scrollTop >= heroCenter) {
			header.classList.add('fixed')
			mainEl.style.marginTop = `${header.offsetHeight}px`;
		} else {
			header.classList.remove('fixed')
			mainEl.style.marginTop = `0px`;
		}
	};

	headerFixed();

	window.addEventListener('scroll', () => {
		headerFixed();
    console.log(header.offsetHeight);
	});
});