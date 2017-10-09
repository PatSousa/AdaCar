const mynav = document.querySelector("#navbar");

function fixNav() {
    console.log(window.scrollY)
    console.log(topOfNav)
    if(window.scrollY >= topOfNav) {
      document.body.style.paddingTop = nav.offsetHeight + 'px';
      document.body.classList.add('fixed-nav');
    } else {
      document.body.classList.remove('fixed-nav');
      document.body.style.paddingTop = 0;
    }
}

window.addEventListener('scroll', fixNav);