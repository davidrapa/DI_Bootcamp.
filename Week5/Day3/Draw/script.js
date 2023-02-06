const grid = document.getElementById("grid");
const palette = document.getElementById("palette");
const colors = document.querySelectorAll(".color");

for (let i = 0; i < 3000; i++) {
  const square = document.createElement("div");
  square.classList.add("square");
  grid.appendChild(square);
}

let selectedColor;

palette.addEventListener("click", (e) => {
  selectedColor = window.getComputedStyle(e.target).backgroundColor;
});

grid.addEventListener("mouseover", (e) => {
  if (e.buttons === 1) {
    e.target.style.backgroundColor = selectedColor;
  }
});
