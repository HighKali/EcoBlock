async function updateChart() {
  const res = await fetch("http://127.0.0.1:8040/rewards");
  const data = await res.json();
  const labels = Object.keys(data);
  const values = Object.values(data);
  const ctx = document.getElementById("chart").getContext("2d");
  if (window.minerChart) {
    window.minerChart.data.labels = labels;
    window.minerChart.data.datasets[0].data = values;
    window.minerChart.update();
  } else {
    window.minerChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'ZSONA Reward',
          data: values,
          backgroundColor: '#00ff88'
        }]
      },
      options: {
        animation: { duration: 1000 },
        scales: { y: { beginAtZero: true } }
      }
    });
  }
}
setInterval(updateChart, 5000);
