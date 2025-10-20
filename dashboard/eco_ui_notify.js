function showNotification(message, type = "info") {
  const box = document.createElement("div");
  box.className = `eco-notify ${type}`;
  box.innerText = message;
  document.body.appendChild(box);
  setTimeout(() => box.remove(), 4000);
}
