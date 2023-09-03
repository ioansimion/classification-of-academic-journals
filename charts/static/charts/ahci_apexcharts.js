const apexcharts_1 = JSON.parse(document.getElementById('apexcharts_1').textContent);
const apexcharts_2 = JSON.parse(document.getElementById('apexcharts_2').textContent);

var options1 = {
    labels: apexcharts_1[0],
    series: apexcharts_1[1],
    chart: {
        type: 'donut',
    },
    title: {
        text: 'Overall category coverage'
    },
    plotOptions: {
        pie: {
            donut: {
                size: '50%',
                background: 'transparent',
            },
        }
    },
};
var chart1 = new ApexCharts(document.querySelector("#apexcharts_div_1"), options1);
chart1.render();

var options2 = {
    series: apexcharts_2,
    chart: {
        type: 'bar',
        height: 500,
        stacked: true,
        stackType: '100%'
    },
    plotOptions: {
        bar: {
            horizontal: true,
        },
    },
    stroke: {
        width: 1,
        colors: ['#fff']
    },
    title: {
        text: 'Category coverage in each year'
    },
    xaxis: {
        categories: [2011, 2012, 2013, 2014, 2015],
    },
    tooltip: {
        y: {
            formatter: val => val + " journals"
        }
    },
    fill: {
        opacity: 1
    },
    legend: {
        position: 'top',
        horizontalAlign: 'left',
        offsetX: 40
    }
};
var chart2 = new ApexCharts(document.querySelector("#apexcharts_div_2"), options2);
chart2.render();