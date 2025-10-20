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
