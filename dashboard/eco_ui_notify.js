function notify(msg, type="info") {
  const toast = document.createElement("div");
  toast.textContent = msg;
  toast.style.position = "fixed";
  toast.style.bottom = "20px";
  toast.style.right = "20px";
  toast.style.padding = "10px 20px";
  toast.style.background = type === "error" ? "#ff4d4d" : "#00ffc8";
  toast.style.color = "#0f1117";
  toast.style.borderRadius = "8px";
  toast.style.boxShadow = "0 0 10px rgba(0,255,200,0.3)";
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}
