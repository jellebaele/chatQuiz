const mastheadAvatar = document.querySelector(".masthead-avatar");
const images = document.querySelectorAll(".grid-image");
const frmSubmit = document.querySelector('#loginForm');
const testBtn = document.querySelector("#test");

let currSelectedAvater = '';
let avatarSelected = false;

images.forEach(img => {
    img.addEventListener('click', () => {
        avatarSelected = true;
        document.querySelector("#avatar").value = img.src;
        mastheadAvatar.src = img.src;
        img.classList.add("grid-image-selected");
        if (currSelectedAvater && currSelectedAvater !== img) {
            currSelectedAvater.classList.remove("grid-image-selected")
        }
        currSelectedAvater = img;
        console.log(currSelectedAvater.src);
    })
});

frmSubmit.addEventListener("submit", submitLogin = (e) => {
    if (!avatarSelected) {
        e.preventDefault();

        const ul = document.createElement("ul");
        const li = document.createElement("li");
        li.setAttribute("class", "error-element");
        li.innerHTML = "No avatar selected, please select one";
        ul.appendChild(li);
        document.querySelector("#header-pick-avatar").appendChild(ul);
    }
});
