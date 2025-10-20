function notify(message, type = "info") {
  const colors = {
    success: "#00ffcc",
    error: "#ff4444",
    info: "#cccccc"
  };
  const toast = document.createElement("div");
  toast.textContent = message;
  toast.style.position = "fixed";
  toast.style.bottom = "20px";
  toast.style.right = "20px";
  toast.style.background = colors[type] || colors.info;
  toast.style.color = "#000";
  toast.style.padding = "10px 20px";
  toast.style.borderRadius = "8px";
  toast.style.boxShadow = "0 0 10px rgba(0,0,0,0.3)";
  toast.style.zIndex = "9999";
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}
