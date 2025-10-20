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
    const Fechas = []
    const Notas = []
    const fecha = data["Fecha"]
    const nota = data["Nota"]
    Fechas.push(fecha)
    Notas.push(nota)
    grafico(Fechas,Notas)
})

fetch("http://127.0.0.1:5000")
.then(response => {
    if (!response.ok){
        throw new Error("Ha fallado la API");
    }
    return response.json();
})
.then(data => {
    const tabla = document.getElementById("contenedor");
    data.forEach(element => {
      const division = document.createElement("div");
      const nombre = document.createElement("h6");
      division.className = "d-flex flex-column justify-content-center";
      nombre.className = "mb-0 text-sm";
      nombre.textContent = element.Nombre || element.nombre;
      division.appendChild(nombre);
      tabla.appendChild(division);
    });
})



function grafico(fecha,nota) {
  
  var ctx2 = document.getElementById("chart-line").getContext("2d");
  
    var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);

    gradientStroke2.addColorStop(1, 'rgba(20,23,39,0.2)');
    gradientStroke2.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke2.addColorStop(0, 'rgba(20,23,39,0)'); //purple colors

    new Chart(ctx2, {
      type: "line",
      data: {
        labels: fecha,
        datasets: [{
          label: "Promedio",
          tension: 0.4,
          borderWidth: 0,
          pointRadius: 0,
          borderColor: "#3A416F",
          borderWidth: 3,
          backgroundColor: gradientStroke2,
          fill: true,
          data: nota,
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
  };