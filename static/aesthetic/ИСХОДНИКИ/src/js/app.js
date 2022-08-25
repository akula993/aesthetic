import * as flsFunctions from "./modules/functions.js";
import './components.js';

flsFunctions.isWebp();


// Import swiper
import Swiper, { Navigation, Pagination, Autoplay, Mousewheel, EffectFade, Thumbs, Scrollbar } from 'swiper';
Swiper.use([Navigation, Pagination, Autoplay, Mousewheel, EffectFade, Thumbs, Scrollbar]);

// Инициализация слайдера intro-main__slider
const introMainSlider = document.querySelector('.intro-main__slider');
var mySwiperIntroMain = new Swiper(introMainSlider, { 	
  slidesPerView: 1,	
  spaceBetween: 10,    
  speed: 800,
  effect: 'fade',
  autoplay: {
    delay: 6000,
  }, 
  fadeEffect: {
    crossFade: true
  },  
  pagination: {
		el: '.intro-main .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.intro-main .intro-main__arrow-next',
    prevEl: '.intro-main .intro-main__arrow-prev',
  }, 
});


// Инициализация слайдера about-main__card-slider
const aboutMainSlider = document.querySelector('.about-main__card-slider');
var mySwiperAboutMain = new Swiper(aboutMainSlider, { 	
  slidesPerView: 1,	
  spaceBetween: 10,    
  speed: 800,
  effect: 'fade',
  autoplay: {
    delay: 2000,
  }, 
  fadeEffect: {
    crossFade: true
  },  
  pagination: {
		el: '.about-main .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.about-main .about-main__arrow-next',
    prevEl: '.about-main .about-main__arrow-prev',
  }, 
});


// Инициализация слайдера intro-product__slider
const productIntroSlider = document.querySelector('.intro-product__slider');
var mySwiperProductIntro = new Swiper(productIntroSlider, { 	
  slidesPerView: 1,	
  spaceBetween: 10,    
  speed: 800,
  effect: 'fade',   
  fadeEffect: {
    crossFade: true
  },  
  pagination: {
		el: '.intro-product .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.intro-product .intro-main__arrow-next',
    prevEl: '.intro-product .intro-main__arrow-prev',
  }, 
});


// Инициализация слайдера reviews__slider
const producReviewsSlider = document.querySelector('.reviews__slider');
var mySwiperProductReviews = new Swiper(producReviewsSlider, { 	
  slidesPerView: 3,	
  spaceBetween: 30,    
  speed: 800,
  pagination: {
		el: '.reviews .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.reviews .navigation__arrow-next',
    prevEl: '.reviews .navigation__arrow-prev',
  }, 
  breakpoints: {  
    0: {     
      slidesPerView: 1,	       
    },  
    768: {
      slidesPerView: 2,	    
    } ,     
    992: {
      slidesPerView: 3,	       
    },  
  },
});


// Инициализация слайдера repair-items__slider
const productRepairSlider = document.querySelector('.repair-items__slider');
var mySwiperProductRepair = new Swiper(productRepairSlider, { 	
  slidesPerView: 3,	
  spaceBetween: 30,    
  speed: 800,
  pagination: {
		el: '.repair-items .pagination-main',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.repair-items .navigation__arrow-next',
    prevEl: '.repair-items .navigation__arrow-prev',
  }, 
  breakpoints: {  
    0: {     
      slidesPerView: 1,	       
    },  
    768: {
      slidesPerView: 2,	    
    } ,     
    992: {
      slidesPerView: 3,	       
    },  
  },
});



// Инициализация слайдера slider-inner__slider
document.querySelectorAll('.repair-items__slide').forEach(n => {
  const sliderSm = new Swiper(n.querySelector('.slider-inner__slider'), {
    slidesPerView: 1,	
    spaceBetween: 30,    
    speed: 800,
    effect: 'fade',
    fadeEffect: {
      crossFade: true
    },  
    pagination: {
      el: n.querySelector('.repair-items .pagination'),
      clickable: true,
      type: 'bullets',
    },  
    navigation: {
      nextEl: n.querySelector('.repair-items__slide-top .about-main__arrow-next'),
      prevEl: n.querySelector('.repair-items__slide-top .about-main__arrow-prev'),
    }, 
  });
});


// Инициализация слайдера recommended__slider
const productRecommendedSlider = document.querySelector('.recommended__slider');
var mySwiperProductRecommended = new Swiper(productRecommendedSlider, { 	
  slidesPerView: 3,	
  spaceBetween: 30,    
  speed: 800,
  pagination: {
		el: '.recommended .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.recommended .navigation__arrow-next',
    prevEl: '.recommended .navigation__arrow-prev',
  }, 
  breakpoints: {  
    0: {     
      slidesPerView: 2,	       
    },  
    768: {
      slidesPerView: 2,	    
    } ,     
    992: {
      slidesPerView: 3,	       
    },  
  },
});



// Инициализация слайдера recommended__slider_sm
const productRecommendedSliderSm = document.querySelector('.recommended__slider_sm');
var mySwiperProductRecommendedSm = new Swiper(productRecommendedSliderSm, { 	
  slidesPerView: 2,	
  spaceBetween: 30,    
  speed: 800,
  pagination: {
		el: '.recommended .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.recommended .navigation__arrow-next',
    prevEl: '.recommended .navigation__arrow-prev',
  }, 
  breakpoints: {  
    0: {     
      slidesPerView: 2,	       
    },  
    768: {
      slidesPerView: 2,	    
    } ,     
    992: {
      slidesPerView: 3,	       
    },  
  },
});

// Инициализация слайдера archives__slider
const archivesSlider = document.querySelector('.archives__slider');
var mySwiperArchives = new Swiper(archivesSlider, { 	
  slidesPerView: 1,	
  spaceBetween: 10,    
  speed: 800,   
  pagination: {
		el: '.archives .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.archives .navigation__arrow-next',
    prevEl: '.archives .navigation__arrow-prev',
  }, 
});
// Инициализация слайдера articles-main__slider
const articlesMainSlider = document.querySelector('.articles-main__slider');
var mySwiperArticlesMain = new Swiper(articlesMainSlider, { 	
  slidesPerView: 1,	
  spaceBetween: 30,    
  speed: 800,   
  pagination: {
		el: '.archives .pagination',
		clickable: true,
		type: 'bullets',
	},  
  navigation: {
    nextEl: '.archives .navigation__arrow-next',
    prevEl: '.archives .navigation__arrow-prev',
  }, 
});


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

















