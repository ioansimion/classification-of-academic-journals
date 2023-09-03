const apexcharts_1 = JSON.parse(document.getElementById('apexcharts_1').textContent);
const apexcharts_2 = JSON.parse(document.getElementById('apexcharts_2').textContent);

var options1 = {
    series: apexcharts_1,
    chart: {
        height: 350,
        type: 'line',
        zoom: { enabled: false },
    },
    stroke: { curve: 'straight' },
    title: { text: 'Maximum scores' },
    labels: [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    grid: {
        row: {
            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.5
        },
    },
};
var chart1 = new ApexCharts(document.querySelector("#apexcharts_div_1"), options1);
chart1.render();

var options2 = {
    series: apexcharts_2,
    chart: {
        height: 350,
        type: 'line',
        zoom: { enabled: false },
    },
    stroke: { curve: 'straight' },
    title: { text: 'Average scores' },
    labels: [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    grid: {
        row: {
            colors: ['#f3f3f3', 'transparent'],
            opacity: 0.5
        },
    },
};
var chart2 = new ApexCharts(document.querySelector("#apexcharts_div_2"), options2);
chart2.render();