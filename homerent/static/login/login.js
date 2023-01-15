document.getElementById("id_username").placeholder = "Your Username";
document.getElementById("id_password").placeholder = "Your Password";

const eyeoff = document.querySelector(".eyeicon"),
  input = document.getElementById("id_password");
grad = document.querySelector(".grad");
eyeoff.addEventListener("click", () => {
  eyeoff.classList.toggle("none");
  grad.classList.toggle("pause");
  input.type === "password" ? (input.type = "text") : (input.type = "password");
});
for (let i = 0; i < 800; i++) {
  let cube = `
<div class="cube"></div>
            `;
  document.querySelector(".cubes").insertAdjacentHTML("afterbegin", cube);
}
