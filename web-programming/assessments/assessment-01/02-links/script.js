const headerLogo = document.querySelector("#logo");

document.addEventListener("scroll", () => {
  headerLogo.style.height = window.scrollY > 0 ?  "3rem" : "5rem"
})