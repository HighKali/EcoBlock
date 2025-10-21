const socket = io();

socket.emit("request_sync_status");

socket.on("sync_status", (data) => {
  document.getElementById("sync-time").textContent = new Date(data.last_sync).toLocaleTimeString();
  document.getElementById("dex-volume").textContent = data.volume;
  document.getElementById("dex-apy").textContent = data.apy + "%";
});

const connectBtn = document.getElementById("connectBtn");
const walletStatus = document.getElementById("walletStatus");

connectBtn.onclick = async () => {
  if (typeof window.ethereum !== 'undefined') {
    try {
      const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
      walletStatus.innerHTML = `✅ Wallet connesso: ${accounts[0]}`;
    } catch (err) {
      walletStatus.innerHTML = `❌ Connessione fallita: ${err.message}`;
    }
  } else {
    walletStatus.innerHTML = "⚠️ MetaMask non rilevato";
  }
};
