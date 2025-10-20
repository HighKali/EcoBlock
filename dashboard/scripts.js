function runScript(name) {
  fetch(`/run/${name}`)
    .then(res => res.text())
    .then(data => {
      document.getElementById("output").innerText = data;
      showNotification(`✅ ${name} eseguito`);
    })
    .catch(err => {
      document.getElementById("output").innerText = "❌ Errore: " + err;
      showNotification(`❌ Errore in ${name}`, "error");
    });
}

function mintZsona() {
  fetch("/run/eco_zsona_mint")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function syncZsona() {
  fetch("/run/eco_zsona_sync")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function generateZsonaKeys() {
  fetch("/run/eco_zsona_keys")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function transferZsona(e) {
  e.preventDefault();
  const to = document.getElementById("zsona-to").value;
  const amount = document.getElementById("zsona-amount").value;
  sendZsona();
}

function sendZsona() {
  const to = document.getElementById("zsona-to").value;
  const amount = document.getElementById("zsona-amount").value;
  fetch(`/run/eco_zsona_transfer?args=${to},${amount}`)
    .then(res => res.text())
    .then(msg => alert(msg));
}

function mintZsona() {
  fetch("/run/eco_zsona_mint")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function syncZsona() {
  fetch("/run/eco_zsona_sync")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function generateZsonaKeys() {
  fetch("/run/eco_zsona_keys")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function checkPool() {
  fetch("/run/eco_zsona_pool")
    .then(res => res.text())
    .then(msg => alert(msg));
}

function transferZsona(e) {
  e.preventDefault();
  const to = document.getElementById("zsona-to").value;
  const amount = document.getElementById("zsona-amount").value;
  fetch()
    .then(res => res.text())
    .then(msg => alert(msg));
}
