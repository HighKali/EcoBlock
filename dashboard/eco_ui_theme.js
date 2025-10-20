document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.createElement("button");
  themeToggle.textContent = "🌓 Tema";
  themeToggle.style.position = "fixed";
  themeToggle.style.top = "10px";
  themeToggle.style.right = "10px";
  themeToggle.onclick = () => {
    document.body.classList.toggle("light");
    if (document.body.classList.contains("light")) {
      document.body.style.backgroundColor = "#ffffff";
      document.body.style.color = "#000000";
    } else {
      document.body.style.backgroundColor = "#0f1117";
      document.body.style.color = "#ffffff";
    }
  };
  document.body.appendChild(themeToggle);
});
