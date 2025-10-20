setInterval(() => {
  fetch("/api/zsona").then(r => r.json()).then(data => {
    document.getElementById("zsona-balance-value").textContent = data.balance;
  });
}, 5000);
