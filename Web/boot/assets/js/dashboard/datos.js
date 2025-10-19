fetch("http://127.0.0.1:5000/nota")
.then(response => {
    if (!response.ok){
        throw new Error("Ha fallado la API");
    }
    return response.json();
})
.then(data => {
    puntuacion = document.getElementById("Puntuacion")
    puntuacion.textContent = data["Nota"]
})
.catch(error => {
        console.log("Fallo en el envio de nota", error);
});

fetch("http://127.0.0.1:5000/nota_fecha")
.then(response => {
    if (!response.ok){
        throw new Error("Ha fallado la API");
    }
    return response.json();
})
.then(data => {
    console.log(data)
    const fecha = [data["Fecha"]]
    const nota = [data["Nota"]]
    grafico(fecha,nota)
})


function grafico(fecha,nota) {
  const Fecha = JSON.parse(localStorage.getItem("Fecha"));
  const Nota = JSON.parse(localStorage.getItem("Nota"));
  Fecha.push(fecha)
  Nota.push(nota)
  localStorage.setItem("Nota", JSON.stringify(Nota));
  localStorage.setItem("Fecha", JSON.stringify(Fecha));
  console.log("Datos guardados");
  console.log(Fecha)
  

  

  var ctx2 = document.getElementById("chart-line").getContext("2d");
  
    var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

    gradientStroke2.addColorStop(1, 'rgba(20,23,39,0.2)');
    gradientStroke2.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke2.addColorStop(0, 'rgba(20,23,39,0)'); //purple colors

    new Chart(ctx2, {
      type: "line",
      data: {
        labels: Fecha,
        datasets: [{
          label: "Promedio",
          tension: 0.4,
          borderWidth: 0,
          pointRadius: 0,
          borderColor: "#3A416F",
          borderWidth: 3,
          backgroundColor: gradientStroke2,
          fill: true,
          data: Nota,
          maxBarThickness: 6
        },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5]
            },
            ticks: {
              display: true,
              padding: 10,
              color: '#b2b9bf',
              font: {
                size: 11,
                family: "Inter",
                style: 'normal',
                lineHeight: 2
              },
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
              borderDash: [5, 5]
            },
            ticks: {
              display: true,
              color: '#b2b9bf',
              padding: 20,
              font: {
                size: 11,
                family: "Inter",
                style: 'normal',
                lineHeight: 2
              },
            }
          },
        },
      },
    })
  }