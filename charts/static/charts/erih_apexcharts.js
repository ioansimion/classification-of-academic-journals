const apexcharts_1 = JSON.parse(document.getElementById('apexcharts_1').textContent);
const apexcharts_2 = JSON.parse(document.getElementById('apexcharts_2').textContent);
const apexcharts_3 = JSON.parse(document.getElementById('apexcharts_3').textContent);
const apexcharts_4 = JSON.parse(document.getElementById('apexcharts_4').textContent);
const apexcharts_5 = JSON.parse(document.getElementById('apexcharts_5').textContent);

var options1 = {
    labels: apexcharts_1[0],
    series: apexcharts_1[1],
    chart: {
        type: 'donut',
    },
    title: {
        text: 'Overall discipline coverage'
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
        text: 'Category coverage in 2007'
    },
    xaxis: {
        categories: ["NAT", "INT1", "INT2", "N/A"],
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

var options3 = {
    series: apexcharts_3,
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
        text: 'Category coverage in 2011'
    },
    xaxis: {
        categories: ["NAT", "INT1", "INT2", "N/A"],
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
var chart3 = new ApexCharts(document.querySelector("#apexcharts_div_3"), options3);
chart3.render();

var options4 = {
    series: apexcharts_4,
    chart: {
        type: 'bar',
        height: 600,
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
        text: 'Journal coverage in 2007'
    },
    xaxis: {
        categories: [
            "Anthropology",
            "Archaeology",
            "Art and Art History",
            "Classical Studies",
            "Gender Studies",
            "History",
            "History & Philosophy of Science",
            "Linguistics",
            "Literature",
            "Musicology",
            "Oriental and African studies",
            "Pedagogical & Educational Research",
            "Philosophy",
            "Psychology",
            "Religious Studies and Theology",
        ],
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
var chart4 = new ApexCharts(document.querySelector("#apexcharts_div_4"), options4);
chart4.render();

var options5 = {
    series: apexcharts_5,
    chart: {
        type: 'bar',
        height: 600,
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
        text: 'Journal coverage in 2011'
    },
    xaxis: {
        categories: [
            "Anthropology",
            "Archaeology",
            "Art and Art History",
            "Classical Studies",
            "Gender Studies",
            "History",
            "History & Philosophy of Science",
            "Linguistics",
            "Literature",
            "Musicology",
            "Oriental and African studies",
            "Pedagogical & Educational Research",
            "Philosophy",
            "Psychology",
            "Religious Studies and Theology",
        ],
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
var chart5 = new ApexCharts(document.querySelector("#apexcharts_div_5"), options5);
chart5.render();