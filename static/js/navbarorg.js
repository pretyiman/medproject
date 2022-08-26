//Create function to select elements
// const selectElement = (element) => document.querySelector(element);
const selectElement = (element) => document.querySelector(element);
//Open and close nav on click
// selectElement (element:'.menu-icon').addEventListener(type:'click',listner:() => {
//   selectElement(element:'nav').classList.toggle(token:'active');
// });
document.querySelectorAll('.menu-icon').forEach(item => {
    item.addEventListener('click', event => {
        selectElement('nav').classList.toggle('active');
    })
});
