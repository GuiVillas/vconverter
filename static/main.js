/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
          nav = document.getElementById(navId)
 
    toggle.addEventListener('click', () =>{
        nav.classList.toggle('show_menu')
 
        toggle.classList.toggle('show_icon')
    })
 }
 
 showMenu('nav_toggle','nav_menu')